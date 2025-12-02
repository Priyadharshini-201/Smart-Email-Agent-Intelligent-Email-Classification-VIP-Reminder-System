import os
import matplotlib.pyplot as plt

REPORT_DIR = "memory/reports"
CHART_DIR = "memory/charts"
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)

def generate_report(emails_memory):
    # Text report
    report_file = os.path.join(REPORT_DIR, "report.txt")
    with open(report_file, "w") as f:
        f.write("--- Email Agent Report ---\n\n")
        for email in emails_memory:
            f.write(f"Date: {email['date']}, Sender: {email['sender']}, Category: {email['category']}, Subject: {email['subject']}, VIP: {email['VIP']}\n")

    # Chart
    categories = [email['category'] for email in emails_memory]
    counts = {cat: categories.count(cat) for cat in set(categories)}
    
    plt.figure(figsize=(6,4))
    plt.bar(counts.keys(), counts.values(), color='skyblue')
    plt.title("Email Categories Count")
    plt.savefig(os.path.join(CHART_DIR, "categories_chart.png"))
    plt.close()
    
    return report_file, os.path.join(CHART_DIR, "categories_chart.png")
