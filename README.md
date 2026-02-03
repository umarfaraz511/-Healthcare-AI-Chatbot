# 🏥 Healthcare AI Chatbot

> Multilingual medical assistant powered by Google Gemini 2.5 AI

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Google Gemini](https://img.shields.io/badge/AI-Gemini%202.5-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A production-ready healthcare chatbot providing instant medical guidance in **English**, **Urdu (اردو)**, and **Arabic (العربية)**.

## ✨ Features

- 🤖 **AI-Powered** - Google Gemini 2.5 Flash for accurate responses
- 🌍 **Multilingual** - English | Urdu | Arabic support
- ⚡ **Real-Time** - Instant medical guidance
- 💬 **Dual Mode** - Terminal app + Telegram bot
- 📊 **Comprehensive** - Symptoms, diseases, nutrition, first aid


## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/umarfaraz511/healthcare-chatbot.git
cd healthcare-chatbot

# Install dependencies
pip install -r requirements.txt

# Create .env file
TELEGRAM_BOT_TOKEN=your_telegram_token
GEMINI_API_KEY=your_gemini_key

# Run Terminal Mode
python terminal_mode.py

# OR Run Telegram Bot
python main.py
```

<img width="707" height="326" alt="health care chatbot terminal 1" src="https://github.com/user-attachments/assets/7a41b651-b9ed-491c-969c-110f3731fbe4" />



<img width="863" height="456" alt="healthcare 2 correct" src="https://github.com/user-attachments/assets/348ee115-8679-479d-bc41-83240e151780" />
<img width="950" height="464" alt="healthcare 3" src="https://github.com/user-attachments/assets/f2f6cfcb-c5e5-4e2e-b937-b57b635d5568" />


## 💬 Demo

**English:** "What are symptoms of diabetes?"  
**Urdu:** "بخار کی علامات کیا ہیں؟"  
**Arabic:** "ما هي أعراض السكري؟"

All answered instantly with accurate medical information!

## 🛠️ Tech Stack

- **Python 3.11** - Core language
- **Google Gemini 2.5** - AI model
- **Telegram Bot API** - Messaging platform
- **Langdetect** - Language detection
- **Asyncio** - Async processing


## 📁 Structure
```
healthcare-chatbot/
├── main.py              # Telegram bot
├── terminal_mode.py     # Terminal interface
├── config/settings.py   # Configuration
├── src/
│   ├── bot.py          # Bot handlers
│   ├── ai_handler.py   # AI integration
│   ├── language_handler.py
│   └── prompts.py
└── requirements.txt

## 🎯 Commands

**Terminal Mode:**
- `/language` - Switch language
- `/quit` - Exit

**Telegram Bot:**
- `/start` - Begin
- `/language` - Change language

## ⚠️ Disclaimer

This bot provides general health information only. **Not a substitute for professional medical advice.*

## 👤 Author

**Umar Faraz** - ML Engineer & Web Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](www.linkedin.com/in/umar-faraz-700457280)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/umarfaraz5111)

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ for accessible healthcare

</div>
<img width="707" height="326" alt="health care chatbot terminal 1" src="https://github.com/user-attachments/assets/7a41b651-b9ed-491c-969c-110f3731fbe4" />



<img width="863" height="456" alt="healthcare 2 correct" src="https://github.com/user-attachments/assets/348ee115-8679-479d-bc41-83240e151780" />
<img width="950" height="464" alt="healthcare 3" src="https://github.com/user-attachments/assets/f2f6cfcb-c5e5-4e2e-b937-b57b635d5568" />



