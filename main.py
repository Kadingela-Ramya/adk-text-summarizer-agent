from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import os
import re

app = Flask(__name__)
CORS(app)

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def fallback_summarize(text):
    """
    Simple local fallback summarizer:
    returns the first 2 sentences or first ~60 words.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    if len(sentences) >= 2:
        return " ".join(sentences[:2])
    words = text.split()
    return " ".join(words[:60])

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Text Summarization Agent is running!"
    })

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "Please provide text to summarize"}), 400

        prompt = f"Summarize the following text in 2-3 lines:\n\n{text}"

        try:
            # Primary: Gemini
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            summary = response.text
            source = "gemini"

        except Exception as gemini_error:
            # Fallback if quota/model fails
            summary = fallback_summarize(text)
            source = "fallback"
            print("Gemini failed, using fallback:", gemini_error)

        return jsonify({
            "input_text": text,
            "summary": summary,
            "source": source
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)