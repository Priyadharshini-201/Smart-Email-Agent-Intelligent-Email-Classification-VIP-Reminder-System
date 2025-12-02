from datetime import datetime, timedelta
import os

REMINDER_FILE = "memory/reminders.txt"
os.makedirs(os.path.dirname(REMINDER_FILE), exist_ok=True)

VIP_SENDERS = ["ceo@example.com", "boss@example.com", "client@example.com"]

def check_vip(email):
    urgent_keywords = ["URGENT", "Important", "Deadline"]
    is_vip = email["sender"] in VIP_SENDERS
    is_urgent = any(word.lower() in email["subject"].lower() for word in urgent_keywords)
    return is_vip or is_urgent

def generate_reminders(emails_memory, hours_pending=24):
    reminders = []
    now = datetime.now()
    for email in emails_memory:
        email_date = datetime.strptime(email["date"], "%Y-%m-%d")
        if check_vip(email) and now - email_date <= timedelta(hours=hours_pending):
            reminders.append(f"Reminder: '{email['subject']}' from {email['sender']} (Category: {email['category']})")
    # Save reminders
    with open(REMINDER_FILE, "w") as f:
        for r in reminders:
            f.write(r + "\n")
    return reminders
