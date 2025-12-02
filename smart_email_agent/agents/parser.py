# agents/parser.py

import pandas as pd

def load_emails(file_path):
    df = pd.read_csv(file_path)
    emails = df.to_dict(orient='records')
    return emails
