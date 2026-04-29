# AI Smart-Distiller & Workflow Automator

**FAST-NUCES — Artificial Intelligence Project**
Group: Ghulam Mujtaba Qureshi (24K-0535) · Syed Muhammad Muzammil (24K-0887) · Muzammil Ali (24K-1023)
Instructor: Atif Luqman

---

## What This Project Does

Paste any long text (meeting notes, article, project brief) into the web app.
The AI extracts:
- **Summary** — 2–3 sentence core message
- **Tasks** — action items and responsibilities
- **Deadlines** — dates with context

Then automatically routes the structured data to **Google Sheets**, **Discord**, or **Email** via an n8n webhook.

---

## Quick Start (Demo Mode — No Keys Needed)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app (from the src/ folder)
cd src
streamlit run app.py
```

The app runs in **Demo Mode** by default — all AI responses and webhook calls are simulated. It works perfectly for demonstration.

---

## Going Live (Real API Keys)

### Step 1 — Get an OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Click **Create new secret key**
3. Copy the key (starts with `sk-proj-...`)

### Step 2 — Set up n8n
1. Go to https://n8n.io → sign up free
2. Create a new workflow → add a **Webhook** node
3. Copy the **Webhook URL**
4. Add nodes: **Google Sheets** / **Discord** / **Send Email** after the webhook
5. Activate the workflow

### Step 3 — Add keys to config.py
```python
OPENAI_API_KEY  = "sk-proj-YOUR_KEY_HERE"
N8N_WEBHOOK_URL = "https://yourname.app.n8n.cloud/webhook/YOUR_ID"
```

### Step 4 — Run
```bash
cd src
streamlit run app.py
```

---

## Project Structure

```
ai_smart_distiller/
├── src/
│   ├── app.py          ← Streamlit frontend (main entry point)
│   ├── extractor.py    ← LLM extraction logic (OpenAI + mock)
│   ├── webhook.py      ← n8n webhook integration (real + mock)
│   ├── mock_mode.py    ← Detects whether keys are configured
│   └── config.py       ← API keys (fill these in)
├── docs/
│   └── report.docx     ← Project documentation
├── requirements.txt
└── README.md
```

---

## How It Works (Technical)

```
User pastes text
      ↓
Streamlit (app.py)
      ↓
OpenAI API — gpt-4o-mini with System Role Prompt
      ↓
Structured JSON { summary, tasks, deadlines }
      ↓
n8n Webhook (HTTP POST)
      ↓
Google Sheets / Discord / Email
```

The LLM uses a strict **System Role Prompt** that enforces JSON output — it identifies deadlines by semantic context, not just keyword matching.

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| Streamlit | Web frontend (Python) |
| OpenAI API (gpt-4o-mini) | NLU & structured extraction |
| n8n | Workflow automation & API routing |
| Python requests | HTTP communication |
| JSON | Data exchange format |

---

## References
- OpenAI API Documentation: https://platform.openai.com/docs
- Streamlit Documentation: https://docs.streamlit.io
- n8n Documentation: https://docs.n8n.io
