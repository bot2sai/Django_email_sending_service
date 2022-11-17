
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

APIKEY = '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'


message = Mail(
    from_email='aepzhdflq@yomail.info',
    to_emails='bot2sai@mail.ru',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

try:
    sg = SendGridAPIClient(APIKEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)