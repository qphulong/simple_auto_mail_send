from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import yaml
from pydantic import BaseModel
from typing import Dict, List

# Define Pydantic models for the request
class Student(BaseModel):
    student_name: str
    email: str
    marks: Dict[str, int]

class EmailRequest(BaseModel):
    gmail: str
    app_password: str
    template: str
    scores: List[Student]
    template_vars: Dict[str, str]
    subject: str  # Added subject field

# Initialize FastAPI app
app = FastAPI()

# Load CORS configuration from cors_config.yaml
try:
    with open("cors_config.yaml", "r") as file:
        cors_config = yaml.safe_load(file)
    allowed_origins = cors_config.get("allowed_origins", [])
    print("Loaded allowed_origins:", allowed_origins)  # Debug log
except FileNotFoundError:
    allowed_origins = []
    print("Warning: cors_config.yaml not found. No origins will be allowed for CORS.")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # List of allowed origins from YAML
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Updated endpoint to use custom subject
@app.post("/send-emails")
def send_emails(request: EmailRequest):
    try:
        # Establish SMTP connection
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(request.gmail, request.app_password)
            
            # Process each student
            for student in request.scores:
                # Build marks table from student's marks
                marks_table = "\n".join([f"{subj}: {val}" for subj, val in student.marks.items()])
                
                # Fill in the email template
                message_body = request.template.format(
                    student_name=student.student_name,
                    marks_table=marks_table,
                    **request.template_vars
                )
                
                # Construct email message
                msg = MIMEText(message_body, "plain", "utf-8")
                msg["Subject"] = request.subject  # Use custom subject from request
                sender_name = request.template_vars.get("sender_name", "")
                msg["From"] = formataddr((sender_name, request.gmail))
                msg["To"] = student.email
                msg["Reply-To"] = request.gmail
                
                # Send email
                smtp.send_message(msg)
        
        return {"status": "success", "message": "Emails sent successfully"}
    
    except smtplib.SMTPAuthenticationError:
        raise HTTPException(status_code=401, detail="Invalid Gmail credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send emails: {str(e)}")
    
@app.get("/")
def ping():
    return {"status": "success", "message": "Server is responding"}