import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    from_email = "addhyannigam@gmail.com"  
    app_password = "wbtl hroo mazj dtqa"  

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Example: Notify the assigned admin
send_email(
    to_email="addhyannigam@gmail.com",
    subject="📢 New Complaint Registered",
    body="A new complaint has been assigned to your department.\nPlease check your dashboard."
)
