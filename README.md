# ADK Text Summarizer Agent 🤖

An AI-powered text summarization agent built with **Google ADK** and **Gemini 2.0 Flash**, deployed as a serverless container on **Google Cloud Run**.

## What It Does
Accepts any text via a REST API and returns a concise 2-3 line summary using Gemini AI.

## Tech Stack
- 🧠 **Model** — Gemini 2.0 Flash
- ⚙️ **Framework** — Google ADK + Flask
- ☁️ **Deployment** — Google Cloud Run
- 🐍 **Language** — Python 3.10

## API Usage

**Health Check:**
GET /

**Summarize Text:**
POST /summarize
Content-Type: application/json

{
  "text": "Your long text here..."
}

**Response:**
{
  "summary": "Concise summary here.",
  "source": "gemini"
}

## Run Locally

git clone https://github.com/Kadingela-Ramya/adk-text-summarizer-agent.git
cd adk-text-summarizer-agent
pip install -r requirements.txt
set GEMINI_API_KEY=your-api-key
python main.py

## Deployment
Deployed on Google Cloud Run — publicly accessible via HTTP endpoint.
