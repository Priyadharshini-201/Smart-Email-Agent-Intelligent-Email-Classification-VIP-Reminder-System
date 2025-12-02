# agents/report_generator.py

import matplotlib.pyplot as plt
import os

def generate_report(emails):
    categories = [email['category'] for email in emails]
    report = {}
    for cat in categories:
        report[cat] = report.get(cat, 0) + 1

    # Save textual report
    os.makedirs('memory/reports', exist_ok=True)
    with open('memory/reports/report.txt', 'w') as f:
        for k, v in report.items():
            f.write(f"{k}: {v}\n")

    # Generate chart
    os.makedirs('memory/charts', exist_ok=True)
    plt.figure(figsize=(6,4))
    plt.bar(report.keys(), report.values(), color='skyblue')
    plt.title("Email Categories")
    plt.savefig('memory/charts/categories_chart.png')
    plt.close()
