import os
import json
import pandas as pd

MEMORY_FILE = "memory/email_memory.json"

def load_memory():
    os.makedirs("memory", exist_ok=True)
    if os.path.exists(MEMORY_FILE):
        return json.load(open(MEMORY_FILE))
    return []

def save_memory(mem):
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

def load_emails(csv_file="sample_data/emails.csv"):
    return pd.read_csv(csv_file)
