import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.utils import formataddr
from dotenv import load_dotenv
import os

# Load .env configuration
load_dotenv()
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
sender_name = os.getenv("SENDER_NAME")
csv_filename = os.getenv("CSV_FILENAME")
department = os.getenv("DEPARTMENT")
university = os.getenv("UNIVERSITY")

# Read student data
data = pd.read_csv(csv_filename, dtype={'gmail': str})

# Email template with placeholders
template = """Dear Student,

Your result has been recorded as: {mark}.

If you have any concerns, feel free to reach out to me.

Sincerely,
{sender_name}
{department}
{university}
"""

# Loop through and send emails
for _, row in data.iterrows():
    mark = row.get('mark')
    recipient = row.get('gmail')

    # Validate recipient email
    if not isinstance(recipient, str) or pd.isna(recipient):
        print(f"Skipped invalid email: {recipient}")
        continue

    # Format email body
    message_body = template.format(
        mark=mark,
        sender_name=sender_name,
        department=department,
        university=university
    )

    msg = MIMEText(message_body, 'plain', 'utf-8')
    msg['Subject'] = 'Exam Result'
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient
    msg['Reply-To'] = sender_email

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")
