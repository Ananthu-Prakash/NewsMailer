# 📰 Automated News Fetcher & Email Notifier

A Python automation script that retrieves the latest news articles about **Tesla** using the **NewsAPI**, formats the results, and sends them directly to your inbox using **Gmail SMTP**.

This project demonstrates how to integrate **APIs**, **HTTP requests**, and **email automation** in Python.

---

## 🚀 Features

- 🔍 Fetches the latest Tesla news from **NewsAPI.org**
- 📰 Extracts article titles and descriptions
- 📧 Compiles all articles into a neatly formatted email
- 🚀 Automatically sends the email to a configured recipient
- 🛡️ Uses Gmail SMTP with SSL for secure email sending

---

## 🗂️ Project Structure

```
News_Fetcher/
│
├── news_email.py         # Main script (fetches news + sends email)
├── send_email.py         # Email helper function
├── README.md             # Documentation
```

---

## ⚠️ Important Security Note

Google **no longer allows normal Gmail passwords** for SMTP.  
You MUST use a **Gmail App Password**.

### How to create a Gmail app password:
1. Enable **2-Step Verification**
2. Visit → https://myaccount.google.com/apppasswords
3. Generate a 16-character app password
4. Use that password in your script

🔐 Do **not** commit real passwords or API keys to GitHub. Use environment variables instead.

---

## 🎯 How It Works

1. Sends request to NewsAPI for the latest Tesla-related articles.
2. Parses JSON to extract titles & descriptions.
3. Builds a formatted email body.
4. Sends the email via Gmail SMTP.

---

## 📦 Requirements

Install dependencies:

```bash
pip install requests
```

---

## ▶️ Run the Script

```bash
python news_email.py
```

---

## 🧩 Possible Enhancements

- Support for multiple topics
- Save articles to a local database
- Send daily summaries instead of full articles
- Schedule automation with cron or Windows Task Scheduler

---


## 🪪 License

This project is released under the **MIT License**.  
