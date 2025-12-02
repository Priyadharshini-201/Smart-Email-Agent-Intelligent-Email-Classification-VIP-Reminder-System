import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_email(email_dict):
    prompt = f"""
Categorize this email into: VIP, Follow-up, Meeting, Project, General.
Sender: {email_dict['sender']}
Subject: {email_dict['subject']}
Body: {email_dict['body']}
Return only the category.
"""
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()
