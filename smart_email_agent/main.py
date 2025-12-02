# main.py

from agents.parser import load_emails
from agents.classifier import classify_email
from agents.reminder_agent import get_vip_reminders
from agents.report import generate_report
import os
import json

# Load emails
emails = load_emails('sample_data/emails.csv')
print("Columns:", list(emails[0].keys()))

# Classify emails
for email in emails:
    email['category'] = classify_email(email)

# Save memory
os.makedirs('memory', exist_ok=True)
with open('memory/email_memory.json', 'w') as f:
    json.dump(emails, f, indent=2)

# Print VIP reminders
reminders = get_vip_reminders(emails)
print("\n--- VIP / Urgent Email Reminders ---")
for r in reminders:
    print(r)

# Generate report & chart
generate_report(emails)
print("\nReport saved in memory/reports/report.txt")
print("Chart saved in memory/charts/categories_chart.png")
