<p align="center">
  <img src="AI-Project-Banner.png" alt="Banner" width="1000"/>
</p>

<div align="center">

<img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-1.33+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/n8n-Workflow_Automation-EA4B71?style=for-the-badge&logo=n8n&logoColor=white"/>
<img src="https://img.shields.io/badge/Google_Sheets-API-34A853?style=for-the-badge&logo=google-sheets&logoColor=white"/>
<img src="https://img.shields.io/badge/Discord-Webhook-5865F2?style=for-the-badge&logo=discord&logoColor=white"/>

<br><br>

# 🧠 AI Smart-Distiller & Workflow Automator

### *An Intelligent Information Pipeline — Extract. Structure. Automate.*

> Paste any long-form text → AI extracts structured insights → Data is automatically routed to **Google Sheets**, **Discord**, or **Email** via an **n8n** automation workflow — in seconds.

<br>

</div>

---

## 📌 Overview

**AI Smart-Distiller** is a Streamlit web application that tackles the real-world problem of **information overload**. Students and professionals constantly deal with long meeting transcripts, project briefs, and articles. Manually reading them, finding deadlines, writing summaries, and typing everything into spreadsheets is slow and error-prone.

This system automates the entire pipeline in under 30 seconds:

```
User pastes text
       │
       ▼
Streamlit (app.py)
       │
       ▼
OpenAI API — gpt-4o-mini + System Role Prompt
       │
       ▼
Structured JSON  { summary, tasks, deadlines }
       │
       ▼
n8n Webhook  (HTTP POST)
       │
  ┌────┴────────────────┐
  ▼                     ▼                   ▼
📊 Google Sheets   💬 Discord         📧 Email
```

> **~90% faster** than doing it manually — from 45 minutes to ~30 seconds per document.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **AI Extraction** | GPT-4o-mini extracts summary, tasks & deadlines from any text using a strict JSON system prompt |
| ⚡ **n8n Automation** | Routes extracted data via webhook to Google Sheets, Discord, and Email simultaneously |
| 📊 **Google Sheets** | Automatically logs structured data as a new row in your spreadsheet |
| 💬 **Discord Notifications** | Posts an insight summary to your configured Discord channel |
| 📧 **Email Reports** | Sends a formatted email report to configured recipients |
| 🎭 **Demo Mode** | Runs fully with simulated AI & webhook responses — no API keys needed |
| 🌐 **Streamlit UI** | Clean, lightweight Python web interface — no frontend code required |

---

## 🚀 Quick Start — Demo Mode (No Keys Needed)

The app runs in **Demo Mode** by default. All AI responses and n8n webhook calls are simulated — it works perfectly for demonstration without any API keys.

```bash
# 1. Clone the repository
git clone https://github.com/muzammil-zaidi/AI-Smart-Distiller.git
cd AI-Smart-Distiller

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
cd src
streamlit run app.py
```

> **Windows users:** If you get a permission error during install, use:
> ```bash
> pip install --user -r requirements.txt
> ```
> Then run with `python -m streamlit run app.py`

Open your browser at **http://localhost:8501** — the app loads instantly in Demo Mode.

---

## ⚙️ Going Live — Real API Keys

### Step 1 — OpenAI API Key

1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign in → **Create new secret key**
3. Copy the key (starts with `sk-proj-...`)

> ⚠️ You need billing credits on your OpenAI account. GPT-4o-mini costs ~$0.15 per 1M tokens — very cheap for this use case.

---

### Step 2 — Set Up n8n Automation

n8n is the automation backbone of this project. It receives the extracted JSON from Streamlit via a webhook and routes it to your chosen destinations.

#### Option A — n8n Cloud (Recommended — Free Tier Available)

1. Go to [n8n.io](https://n8n.io) → Sign up for a free cloud account
2. Click **New Workflow**
3. Add a **Webhook** node as the first node:
   - Method: `POST`
   - Click **Copy Webhook URL** — save this URL
4. Add destination nodes after the Webhook:

**For Google Sheets:**
- Add a **Google Sheets** node
- Connect your Google account
- Select your spreadsheet and sheet
- Map fields: `summary`, `tasks`, `deadlines`, `timestamp`

**For Discord:**
- Add a **Discord** node
- Add your bot token or webhook URL
- Map the message body using `{{ $json.summary }}`

**For Email:**
- Add a **Send Email** node (or use Gmail node)
- Configure SMTP or connect your Gmail account
- Build the email body from `{{ $json.summary }}`, `{{ $json.tasks }}`, etc.

5. Connect all nodes in sequence after the Webhook
6. Click **Activate** (toggle in top-right)
7. Copy the **Production Webhook URL**

#### Option B — n8n Self-Hosted (Docker)

```bash
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

Access at `http://localhost:5678` and follow the same workflow steps above.

---

### Step 3 — Configure Keys

Open `src/config.py` and fill in your credentials:

```python
# ── OpenAI ─────────────────────────────────────────────────
OPENAI_API_KEY = "sk-proj-YOUR_KEY_HERE"
OPENAI_MODEL   = "gpt-4o-mini"

# ── n8n Webhook ─────────────────────────────────────────────
N8N_WEBHOOK_URL = "https://yourname.app.n8n.cloud/webhook/YOUR_ID"
```

### Step 4 — Run

```bash
cd src
streamlit run app.py
```

The **Demo Mode** banner disappears automatically once keys are detected. The app now uses real OpenAI extraction and sends live data through your n8n workflow.

---

## 🗂️ Project Structure

```
ai_smart_distiller/
├── src/
│   ├── app.py          ← Streamlit frontend (main entry point)
│   ├── extractor.py    ← LLM extraction logic (OpenAI API + mock fallback)
│   ├── webhook.py      ← n8n webhook integration (real HTTP POST + mock)
│   ├── mock_mode.py    ← Detects whether API keys are configured
│   └── config.py       ← API keys — fill these in to go live
├── docs/
│   └── report.docx     ← Full project documentation
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works — Technical Deep Dive

### AI Extraction (Prompt Engineering)

The system uses a carefully engineered **System Role Prompt** that instructs GPT-4o-mini to act as a structured information extractor and return only a strict JSON object:

```json
{
  "summary": "2–3 sentence summary of the document.",
  "tasks": [
    "Action item 1",
    "Action item 2"
  ],
  "deadlines": [
    { "date": "May 1, 2026", "context": "Final report submission deadline" }
  ]
}
```

**Why LLM over keyword search?**

A simple regex search would find every date in a document — including historical ones (*"the company was founded in 1998"*). GPT-4o-mini **understands context**: it distinguishes a deadline from a passing reference, identifies implicit action items not formatted as numbered lists, and generates summaries that capture intent — not just keywords.

---

### n8n Webhook Integration

When the user clicks **Distill & Automate**, the app:

1. Sends the extracted JSON to the n8n webhook via `HTTP POST`
2. n8n receives the payload and routes it to all connected nodes
3. Each node (Sheets, Discord, Email) processes its part in parallel
4. n8n returns `HTTP 200 OK` — displayed in the app as confirmation

```python
# webhook.py — simplified
import requests
payload = { "summary": "...", "tasks": [...], "deadlines": [...] }
response = requests.post(N8N_WEBHOOK_URL, json=payload)
# → n8n handles the rest
```

This architecture means adding a new destination (e.g. Slack, Notion, Trello) only requires adding a new node in n8n — **no code changes needed**.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.12** | Core programming language |
| **Streamlit** | Web frontend — multi-page Python app |
| **OpenAI API** (gpt-4o-mini) | NLU & structured JSON extraction |
| **n8n** | Workflow automation — webhook routing to all destinations |
| **requests** | HTTP communication between Streamlit and n8n |
| **JSON** | Data exchange format between all components |
| **Google Sheets** (via n8n) | Structured data logging |
| **Discord** (via n8n) | Real-time team notifications |
| **Email / Gmail** (via n8n) | Formatted insight reports |

---

## 🔄 Demo Mode vs Live Mode

| Feature | Demo Mode | Live Mode |
|---|---|---|
| OpenAI extraction | Simulated (smart mock) | Real GPT-4o-mini API call |
| n8n webhook | Simulated (fake HTTP 200) | Real webhook POST to n8n |
| Google Sheets | Not updated | Row appended automatically |
| Discord | Not posted | Message posted to channel |
| Email | Not sent | Email delivered to inbox |
| API keys required | ❌ No | ✅ Yes |

Demo Mode is fully functional for class demonstrations — the UI, extraction tabs, and automation status all work perfectly.

---

## 👥 Team

| Member | Roll No | Role |
|---|---|---|
| **Muzammil Zaidi** | 24K-0887 | n8n Automation & Workflow Design |
| **Ghulam Mujtaba** | 24K-0535 | UI Design & Project Lead |
| **Muzammil Ali** | 24K-1023 | Backend Logic & API Integration |

---

## 📚 References

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [n8n Documentation](https://docs.n8n.io)
- [n8n Webhook Node Guide](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)
- [n8n Google Sheets Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/)

---
