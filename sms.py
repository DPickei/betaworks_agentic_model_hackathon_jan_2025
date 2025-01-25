from pathlib import Path
import smtplib
from dotenv import dotenv_values

# Load environment variables from .env file
env_path = Path('.') / '.env'
config = dotenv_values(env_path)  # Load variables from .env
email_password = config.get("GMAIL_PASS")  # Get the Gmail App Password from .env

# Configuration
recipient_number = "7033386461"  # Replace with your phone number (AT&T mobile)
carrier_gateway = "@txt.att.net"  # AT&T SMS gateway
to_number = f"{recipient_number}{carrier_gateway}"  # Full email address for SMS
from_email = "dwpickei@gmail.com"  # Your Gmail address

# Message content
subject = "Test SMS"
body = "Hello, this is a test message sent via email-to-SMS gateway!"
message = f"Subject: {subject}\n\n{body}"

# Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Encrypt connection
        server.login(from_email, email_password)  # Log in to your Gmail account
        server.sendmail(from_email, to_number, message)  # Send the message
        print(f"Message sent successfully to {recipient_number} via AT&T!")
except Exception as e:
    print(f"Failed to send message. Error: {e}")
