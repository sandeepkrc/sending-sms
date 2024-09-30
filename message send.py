import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_emails_from_excel(file_path, subject, body, sender_email, sender_password, smtp_server, smtp_port):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Check if 'Email' column exists
    if 'Email' not in df.columns:
        print("The file does not contain an 'Email' column.")
        return

    # Extract the email column
    email_list = df['Email'].dropna().tolist()

    # Setup SMTP server connection
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the email account

            # Loop through each email and send the message
            for email in email_list:
                try:
                    # Create the email content
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = email
                    msg['Subject'] = subject

                    # Attach the email body
                    msg.attach(MIMEText(body, 'plain'))

                    # Send the email
                    server.sendmail(sender_email, email, msg.as_string())
                    print(f"Email sent to {email}")

                except Exception as e:
                    print(f"Failed to send email to {email}. Error: {e}")

    except Exception as e:
        print(f"Failed to connect to the SMTP server. Error: {e}")

# Example usage
file_path = 'emails.xlsx'
subject = 'Your Subject Here'
body = 'This is the email body content.'
sender_email = 'your-email@example.com'
sender_password = 'your-password'
smtp_server = 'smtp.example.com'  # For Gmail use: smtp.gmail.com
smtp_port = 587  # For Gmail use: 587

send_emails_from_excel(file_path, subject, body, sender_email, sender_password, smtp_server, smtp_port)
