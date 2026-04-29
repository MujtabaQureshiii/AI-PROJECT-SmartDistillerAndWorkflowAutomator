import json
import re
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

SYSTEM_PROMPT = """You are an expert information extractor. Given any text, you MUST return ONLY a valid JSON object — no markdown, no explanation, no extra text. The JSON must have exactly these three keys:

{
  "summary": "A concise 2-3 sentence summary of the entire text.",
  "tasks": [
    "Task or action item 1"
  ],
  "deadlines": [
    {"date": "April 15, 2026", "context": "What is due on this date"}
  ]
}

Rules:
- summary: 2-3 sentences only, capture the core message.
- tasks: list every explicit action item or responsibility. Empty list [] if none.
- deadlines: extract every date that represents a deadline or scheduled event with its context. Empty list [] if none.
- Distinguish deadline dates from dates merely mentioned in passing.
- Return ONLY the JSON. No code fences. No commentary."""


def extract_insights(text: str) -> dict:
    try:
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": f"Extract insights from this text:\n\n{text}"}
            ],
            temperature=0.1,
            max_tokens=1000
        )
        raw = response.choices[0].message.content.strip()
        raw = re.sub(r"^```json\s*|```$", "", raw, flags=re.MULTILINE).strip()
        return json.loads(raw)
    except Exception as e:
        return {
            "summary": f"Error calling Groq API: {str(e)}",
            "tasks": [],
            "deadlines": [],
            "error": str(e)
        }