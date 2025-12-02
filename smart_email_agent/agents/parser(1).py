def parse_email_row(row):
    return {
        "sender": row["sender"],
        "subject": row["subject"],
        "body": row["body"],
        "date": row["date"]
    }
