import os
import smtplib
import pandas as pd
import yaml
from email.mime.text import MIMEText
from email.utils import formataddr
from dotenv import load_dotenv

# 1) Load environment variables (credentials only)
load_dotenv()
sender_email    = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

# 2) Load YAML configuration
with open("config.yaml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

sender_name  = cfg["sender_name"]
csv_filename = cfg["csv_filename"]
department   = cfg["department"]
university   = cfg["university"]
exclude_cols = set(cfg["exclude"])
template     = cfg["template"]

# 3) Read student data
data = pd.read_csv(csv_filename, dtype={"gmail": str})

# 4) Determine which columns are marks
mark_columns = [c for c in data.columns if c not in exclude_cols]

# 5) Loop through rows and send personalized emails
for _, row in data.iterrows():
    recipient    = row.get("gmail")
    student_name = row.get("Names")

    # Skip invalid email
    if not isinstance(recipient, str) or pd.isna(recipient):
        print(f"Skipped invalid email: {recipient}")
        continue

    # Build the marks table
    lines = []
    for subj in mark_columns:
        val = row.get(subj)
        if pd.isna(val):
            continue
        lines.append(f"{subj}: {val}")
    if not lines:
        print(f"No marks for {student_name} <{recipient}>, skipping.")
        continue

    marks_table = "\n".join(lines)

    # Fill in the template
    message_body = template.format(
        student_name=student_name,
        marks_table=marks_table,
        sender_name=sender_name,
        department=department,
        university=university
    )

    # Build and send the email
    msg = MIMEText(message_body, "plain", "utf-8")
    msg["Subject"]  = "Exam Results"
    msg["From"]     = formataddr((sender_name, sender_email))
    msg["To"]       = recipient
    msg["Reply-To"] = sender_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print(f"Email sent to {student_name} <{recipient}>")
    except Exception as e:
        print(f"Failed to send email to {student_name} <{recipient}>: {e}")
