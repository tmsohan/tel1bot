# 🤖 Telegram Personal Chat Bot

A simple Telegram chatbot built with Python using the **python-telegram-bot** library.

---

# ✨ Features

* Responds to `/start`
* Answers personal questions
* Birthday information
* Favorite food
* Favorite color
* Family information
* Favorite subject
* Village location
* Simple keyword-based conversation
* User activity logging with `log.py`

---

# 🛠️ Technologies Used

* Python 3
* python-telegram-bot
* python-dotenv
* Logging
* Git
* GitHub

---

# 📂 Project Structure

```text
tel1bot/
│── bot.py
│── log.py
│── requirements.txt
│── .env
│── .gitignore
│── README.md
│
└── logs/
    └── bot.log
```

---

# 📦 Installation

### Clone the repository

```bash
git clone git@github.com:tmsohan/tel1bot.git
```

### Go to the project directory

```bash
cd tel1bot
```

### Create a virtual environment

```bash
python3 -m venv venv
```

### Activate the virtual environment

**Linux / Kali**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

### Run the bot

```bash
python bot.py
```

---

# 📋 Logging System

This project includes a dedicated **log.py** module that records user activity.

The following information is logged:

* User ID
* Username
* First Name
* Messages sent to the bot
* Date and Time

The log file is automatically created at:

```text
logs/bot.log
```

### View the log

Display the entire log:

```bash
cat logs/bot.log
```

Watch new log entries in real time:

```bash
tail -f logs/bot.log
```

---

# 🚀 Future Plans

* AI Chat Integration
* Individual Human Thinking Analysis (LLM)
* SQLite Database
* Admin Commands
* Advanced Logging System
* Docker Support
* 24/7 VPS Deployment

---

# 👨‍💻 Author

**T.M. Sohan**

GitHub: https://github.com/tmsohan
LinKedin: https://www.linkedin.com/in/t-m-sohanul-islam-568053229/
