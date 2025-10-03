from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.contact import ContactForm
from app.config import EMAIL_USER, EMAIL_PASS, EMAIL_RECEIVER
import smtplib
from email.mime.text import MIMEText
import traceback

router = APIRouter()

def send_email(contact: ContactForm):
    try:

        msg = MIMEText(f"""
        First name: {contact.first_name}
        Last name: {contact.last_name}
        Email: {contact.email}
        Phone: {contact.phone}
        Address: {contact.address}
        Message: {contact.message}
        """)

        msg['Subject'] = f'New contact from {contact.first_name} {contact.last_name}'
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_RECEIVER


        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
            print("Email sent successfully")

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP auth error: {e.smtp_code} - {e.smtp_error}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="SMTP authentication failed")

    except Exception as e:
        print("Email error:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Failed to send email")

@router.post("/send")
async def send_contact(contact: ContactForm):
    send_email(contact)
    return JSONResponse(content={"message": "Message sent successfully"})