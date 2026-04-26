<div align="center">

<img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-1.33+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Google_Sheets-API-34A853?style=for-the-badge&logo=google-sheets&logoColor=white"/>
<img src="https://img.shields.io/badge/Gmail-SMTP-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>

<br><br>

# 🧠 AI Smart-Distiller

### *An Intelligent Information Pipeline — Extract. Structure. Automate.*

> Paste any long-form text → AI extracts insights → Data is automatically pushed to **Google Sheets** and **Email** — in seconds.

<br>

![AI Smart-Distiller Demo](https://raw.githubusercontent.com/muzammil-zaidi/AI-Smart-Distiller/main/assets/demo.png)

</div>

---

## 📌 Overview

**AI Smart-Distiller** is a multi-page Streamlit application that solves the real-world problem of **information overload**. Students and professionals constantly deal with long meeting transcripts, project briefs, and articles. Manually reading them, finding deadlines, writing summaries, and typing everything into spreadsheets is slow and error-prone.

This tool automates the entire pipeline using a Large Language Model:

```
Input Text  →  GPT-4o-mini (OpenAI API)  →  Structured JSON
                                                    │
                              ┌─────────────────────┴─────────────────────┐
                              ▼                                           ▼
                     📊 Google Sheets                              📧 Gmail SMTP
                  (Row appended via gspread)                 (HTML report delivered)
```

> **90% faster** than doing it manually — from 45 minutes to ~30 seconds per document.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **AI Extraction** | Uses GPT-4o-mini to extract summary, action items, and deadlines from any text |
| 📊 **Google Sheets** | Appends structured data as a new row automatically via the Sheets API |
| 📧 **Email Reports** | Sends a beautifully formatted HTML email report via Gmail SMTP |
| 🗂️ **Multi-page UI** | Clean 4-page Streamlit app — Home, Distiller, Automation, About |
| ⚙️ **Status Dashboard** | Live system status showing which integrations are configured |
| 🚪 **Exit Screen** | Presentation-ready thank-you screen with team credits |

---

## 🗂️ Project Structure

```
ai_smart_distiller/
├── src/
│   ├── Home.py                  # Landing page & system status dashboard
│   ├── config.py                # API keys & settings (fill this in)
│   ├── extractor.py             # OpenAI API extraction logic
│   ├── sheets.py                # Google Sheets integration (gspread)
│   ├── mailer.py                # Gmail SMTP email sender
│   ├── mock_mode.py             # Configuration status helpers
│   ├── fa_icons.py              # Font Awesome icon helper
│   └── pages/
│       ├── 1_Distiller.py       # Text input & AI extraction UI
│       ├── 2_Automation.py      # Sheets + Email automation UI
│       └── 3_About.py           # Project info, team, setup guide
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A Gmail account (for email automation)
- An OpenAI account (for real AI extraction)
- A Google Cloud project (for Google Sheets)

### 1. Clone the Repository

```bash
git clone https://github.com/muzammil-zaidi/AI-Smart-Distiller.git
cd AI-Smart-Distiller
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Windows users:** If you get a permission error, use:
> ```bash
> pip install --user -r requirements.txt
> ```

### 3. Run the App

```bash
cd src
python -m streamlit run Home.py
```

Open your browser at `http://localhost:8501`

---

## ⚙️ Configuration Guide

### 🤖 OpenAI API Key
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign in → **API Keys** → **Create new secret key**
3. Copy the key (starts with `sk-proj-...`) and paste it in `config.py`

> You need billing credits to use the API. GPT-4o-mini costs approximately **$0.15 per 1M input tokens** — very cheap for this use case.

### 📊 Google Sheets Integration
1. Go to [console.cloud.google.com](https://console.cloud.google.com) and create a new project
2. Enable **Google Sheets API** and **Google Drive API**
3. Go to **IAM & Admin → Service Accounts** → Create a service account
4. Download the **JSON key file** and note its path
5. Create a new Google Sheet named **"AI Distiller Output"**
6. **Share** the sheet with the service account email (e.g. `myapp@myproject.iam.gserviceaccount.com`) with **Editor** access
7. Set `GOOGLE_SERVICE_ACCOUNT_JSON` to the path of the downloaded JSON file

### 📧 Gmail SMTP Setup
1. Go to [myaccount.google.com](https://myaccount.google.com) → **Security**
2. Enable **2-Step Verification**
3. Search for **App Passwords** → Select app: **Mail** → Generate
4. Copy the **16-character password** (e.g. `abcd efgh ijkl mnop`)
5. Paste it as `EMAIL_PASSWORD` in `config.py`

> **Note:** Use an App Password, not your regular Gmail password. App Passwords bypass 2FA for programmatic access.

---

## 🧠 How It Works

### AI Extraction (Prompt Engineering)

The system uses a carefully engineered **system prompt** that instructs GPT-4o-mini to return a strict JSON object:

```json
{
  "summary": "2-3 sentence summary of the document.",
  "tasks": [
    "Action item 1",
    "Action item 2"
  ],
  "deadlines": [
    { "date": "May 1, 2026", "context": "Final report submission" }
  ]
}
```

**Why LLM over keyword search?**

A simple regex/keyword search would find every date in a document — including dates mentioned in passing (*"the company was founded in 1998"*). The LLM **understands context**: it distinguishes a deadline from a historical reference, identifies implicit action items not in numbered lists, and generates summaries that capture intent rather than just words.

### Automation Pipeline

```
User clicks "Run Automation"
        │
        ├──► sheets.py ──► gspread.authorize() ──► ws.append_row([timestamp, summary, tasks, deadlines])
        │
        └──► mailer.py ──► smtplib.SMTP_SSL("smtp.gmail.com", 465) ──► server.sendmail()
```

---

## 📸 Screenshots

| Page | Description |
|---|---|
| **Home** | Dashboard with feature cards, navigation, and live system status |
| **Distiller** | Text input area with AI extraction results in Summary / Tasks / Deadlines tabs |
| **Automation** | Destination selector with real-time pipeline status |
| **About** | Project overview, team cards, and setup guide |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.12** | Core language |
| **Streamlit** | Multi-page web interface |
| **OpenAI API** (`gpt-4o-mini`) | Natural language understanding & JSON extraction |
| **gspread** | Google Sheets read/write via Service Account |
| **google-auth** | OAuth2 credentials for Google APIs |
| **smtplib** | Gmail SMTP for email delivery |
| **Font Awesome** | UI icons (via CDN) |
