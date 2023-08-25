import smtplib
from email.mime.text import MIMEText
from random import randint

def send_otp_email(email):
    # Generate a 6-digit random number as OTP
    otp = str(randint(100000, 999999))

    # Create a message with the OTP as the body
    msg = MIMEText(f"Your OTP is: {otp}")
    msg['Subject'] = '983465'
    msg['From'] = 'lakshmiviji2003@gmail.com'
    msg['To'] = email

    # Send the message using SMTP
    server = smtplib.SMTP('smtp.gmail.com', your_smtp_port)
    server.starttls()
    server.login('lakshmiviji2003@gmail.com', '9843788261')
    server.send_message(msg)
    server.quit()

# Example usage
send_otp_email('lakshmiviji2003@gmail.com')
