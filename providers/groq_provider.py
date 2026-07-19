import os

import requests

API_KEY = os.getenv("GROQ_API_KEY", "PUT_YOUR_REAL_GROQ_API_KEY_HERE")
URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "openai/gpt-oss-120b"

SYSTEM_PROMPT = (
    "You are Jarvis, an advanced AI assistant. Be accurate and helpful. "
    "If a request or constraint is impossible or contradictory, say so "
    "directly instead of guessing or producing an answer that only "
    "appears to satisfy it."
)


def generate_reply(text: str) -> str:
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        data = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
            "reasoning_effort": "medium",
        }
        response = requests.post(URL, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Provider error: {e}"
