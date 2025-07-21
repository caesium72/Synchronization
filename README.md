# 🚀 Telegram Link Extractor Bot

![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange?logo=openai)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-API-green?logo=googlesheets)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 What Is This?

The **Telegram Link Extractor Bot** is an automated Python-powered Telegram bot that:

- Listens to your chosen Telegram channel or group.
- Detects and extracts all URLs from incoming messages.
- Cleans links by removing emojis and formatting issues.
- Uses **OpenAI's GPT-3.5** to generate short, catchy, and descriptive titles for each link.
- Logs every link with its generated title and timestamp into a Google Sheet for easy tracking, analysis, or sharing.

---

## ⚡ Why Use This Bot?

- Save time manually collecting and naming links from Telegram channels.
- Automatically organize valuable URLs with meaningful titles.
- Perfect for content curation, research, or community management.
- Leverages the power of AI to generate high-quality titles.
- Stores all data in Google Sheets, accessible anywhere.

---

## 🛠 Features

| Feature                     | Description                                       |
|-----------------------------|-------------------------------------------------|
| Real-time Telegram monitoring | Captures new messages as they arrive             |
| Link extraction              | Finds all HTTP/HTTPS/WWW links in messages       |
| Emoji cleaning              | Removes distracting emojis from URLs             |
| AI-powered title generation | Uses OpenAI GPT-3.5 for link title generation    |
| Google Sheets logging        | Automatically logs data with timestamps          |
| Safe and secure              | Uses `.env` and `.gitignore` to protect secrets  |

---

## 📸 Preview

![Bot Workflow](https://your-image-link.com/telegram-bot-flow.png)

*Example workflow: Telegram message → Link extraction → Title generation → Google Sheet logging*

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed
- Telegram API credentials:
  - `API_ID`
  - `API_HASH`
  - `BOT_TOKEN`
- OpenAI API key
- Google Cloud Service Account JSON (`credentials.json`)
- Google Sheet ID to store logs

---

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
