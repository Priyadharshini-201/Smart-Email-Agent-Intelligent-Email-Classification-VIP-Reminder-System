import pandas as pd
from utils import load_emails, load_memory, save_memory
from agents.parser import parse_email_row
from agents.classifier import classify_email
from agents.report import generate_report
from agents.reminder_agent import generate_reminders, check_vip

# Load dataset
df = load_emails("sample_data/emails.csv")
print("Columns:", df.columns.tolist())

# Load memory
memory = load_memory()

# Process emails
for idx, row in df.iterrows():
    email = parse_email_row(row)
    if any(mem['subject'] == email['subject'] for mem in memory):
        continue
    email['category'] = classify_email(email)
    email['VIP'] = check_vip(email)
    memory.append(email)
    print(f"Processed: {email['subject']} -> {email['category']} | VIP: {email['VIP']}")

# Save memory
save_memory(memory)

# Generate report
report_file, chart_file = generate_report(memory)
print(f"Report saved at: {report_file}")
print(f"Chart saved at: {chart_file}")

# Generate reminders
reminders = generate_reminders(memory, hours_pending=48)
print("\n--- VIP / Urgent Email Reminders ---")
for r in reminders:
    print(r)
