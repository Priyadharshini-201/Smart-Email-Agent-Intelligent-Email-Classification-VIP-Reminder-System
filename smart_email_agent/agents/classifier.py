# agents/classifier.py

def classify_email(email_dict):
    """
    Rule-based email classification: works without OpenAI API.
    """
    subject = email_dict["subject"].lower()
    body = email_dict["body"].lower()
    sender = email_dict["sender"].lower()

    # VIP detection
    if "urgent" in subject or "important" in subject or "ceo" in sender or "boss" in sender:
        return "VIP"

    # Meeting detection
    elif "meeting" in subject or "sync" in subject:
        return "Meeting"

    # Project-related
    elif "project" in subject or "report" in body:
        return "Project"

    # Follow-up / Invoice
    elif "invoice" in subject or "pending" in body:
        return "Follow-up"

    else:
        return "General"
