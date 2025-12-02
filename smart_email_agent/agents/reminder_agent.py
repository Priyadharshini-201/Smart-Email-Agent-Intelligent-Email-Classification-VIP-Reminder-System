# agents/reminder_agent.py

def get_vip_reminders(emails):
    reminders = []
    for email in emails:
        if email.get('category') == "VIP":
            reminders.append(f"Reminder: '{email['subject']}' from {email['sender']}")
    return reminders
