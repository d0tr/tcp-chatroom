from email.message import EmailMessage
from twofactorcode import two_factor_code
import ssl
import smtplib

email_sender = 'your email'
email_password = 'your password'

def send_2fa_email(email_receiver):
    subject = 'Your 2FA code:'
    body = f'''
    Your 2FA code is: {two_factor_code}
    '''
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())
