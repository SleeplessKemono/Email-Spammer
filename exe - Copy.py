import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
_cache_config_build_v2 = "script"
print("WARNING! This is for troll use only! DO NOT use this to actually send an email.")
print("Enter your key:")
key = input()
if key == _cache_config_build_v2:
    time.sleep(1)
    print("Access granted!")
    time.sleep(1)
    print("loading...")
    time.sleep(3)
    print("Welcome to Email Spammer!")
    email = input("Type in email you want to send to (Make sure NO TYPOS):  ")
    subjec = input("Enter email subject:   ")
    c = input("Enter email contents:   ")

    SENDER_EMAIL = "getspammedlooser@gmail.com"       
    SENDER_PASSWORD = "cjxr vesb qhlv zuge"  
    RECIPIENT_EMAIL = email

    subject = subjec
    body = f"""
{c}

Your cooked. GGs
"""

    def send_email(sender, password, recipient, subject, body):
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.sendmail(sender, recipient, msg.as_string())
            print(f"Email sent successfully to {recipient}!")
            return True
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Make sure you're using an App Password, not your regular Gmail password.")
            return False
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def spam_emails():
        try:
            num_times = int(input("How many times do you want to send the email? "))
            if num_times <= 0:
                print("Please enter a positive number.")
                return
            
            print(f"Sending {num_times} emails...  DO NOT CLOSE CMD WHILE SENDING!")
            success_count = 0
            
            for i in range(num_times):
                print(f"Sending email {i+1}/{num_times}")
                if send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body):
                    success_count += 1
                
                # Add a small delay to avoid triggering rate limits
                time.sleep(1)
                
            print(f"Successfully sent {success_count}/{num_times} emails. Please keep the CMD open until all emails are sent.")
        except ValueError:
            print("Please enter a valid number.")

    spam_emails()
else:
    print("Invalid key. Access denied.")
    time.sleep(3)
    print("app will now close")