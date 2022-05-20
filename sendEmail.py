import smtplib
import os

EMAIL_ADDRESS = 'chsdmaguire@gmail.com'
EMAIL_PASSWORD = 'chris32c'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'grab dinner'
    body = 'hello word'

    msg = f'subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'chsdmaguire@gmail.com', msg)
    
