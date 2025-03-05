# 📩 Monday Motivation Email Bot

A simple Python script that **sends a random motivational quote** via email every **Monday**.

---

## ✨ Features
- Runs **automatically on Mondays**.
- Sends a **random motivational quote** from a text file.
- Uses **SMTP** to send emails.

---

## 🛠 Setup Instructions

### 1️⃣ Install Dependencies

Ensure you have Python installed, then install the required package:

```bash
pip install smtplib
```

---

### 2️⃣ Configure Email Credentials

In the script, update these variables with your **email credentials**:

```python
MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
SENDER_EMAIL = "recipient@example.com"
```

🔹 If using **Gmail**, enable **App Passwords** instead of your real password.  
🔹 If using another email provider (Yahoo, Outlook, etc.), check their **SMTP settings**.

---

### 3️⃣ Prepare Quotes File

Create a **quotes.txt** file in the same directory as the script:

📄 `quotes.txt`
```
"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
"Success is not final, failure is not fatal: It is the courage to continue that counts."
"Opportunities don't happen, you create them."
```

Each line should contain a **separate motivational quote**.

---

### 4️⃣ Run the Script

You can manually execute the script:

```bash
python monday_motivation.py
```

OR schedule it to run **every Monday**:
- **Windows (Task Scheduler)**
- **Linux/macOS (Cron Job)**

---

## 🚀 How It Works

1. **Checks the current day** (only runs on Mondays).
2. **Reads quotes from `quotes.txt`**.
3. **Randomly selects one** and formats an email.
4. **Sends the email** using `smtplib`.

---

## 🔒 Security Tips
- **Use App Passwords** instead of your real email password.
- Store credentials in **environment variables** instead of hardcoding them.
