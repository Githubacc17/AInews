import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
from dotenv import load_dotenv
import os

class EmailSender:
    def __init__(self):
        """Initialize email sender with configuration from environment variables"""
        load_dotenv()
        
        # Sender configuration
        self.sender_email = os.getenv('GMAIL_SENDER')
        self.sender_password = os.getenv('GMAIL_PASSWORD')
        
        # Get recipient list
        recipients = os.getenv('RECIPIENT_EMAILS', '')
        self.recipient_emails = [email.strip() for email in recipients.split(',') if email.strip()]
        
        if not self.sender_email or not self.sender_password:
            raise ValueError("Sender email configuration is missing in .env file")
        
        if not self.recipient_emails:
            raise ValueError("No recipient emails configured in .env file")

    def send_newsletter(self, pptx_file):
        """Send newsletter to all configured recipients"""
        try:
            # Create subject with date
            current_date = datetime.now().strftime("%B %d, %Y")
            subject = f"Daily Tech Newsletter - {current_date}"
            
            # Create email body
            body = f"""Hello,

Your daily tech newsletter for {current_date} is attached.

This newsletter includes:
- Latest tech news and updates
- AI-generated tech imagery
- Interactive tech quiz
- Tech humor of the day

The PowerPoint presentation is attached for your review.

Best regards,
Your Tech Newsletter Team"""

            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = ', '.join(self.recipient_emails)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach PowerPoint file
            with open(pptx_file, 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(pptx_file))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(pptx_file)}"'
                msg.attach(part)
            
            # Send email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            print(f"Newsletter sent successfully to {len(self.recipient_emails)} recipients")
            
        except Exception as e:
            print(f"Error sending newsletter: {str(e)}")
            raise 