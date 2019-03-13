# import statements
# smtplib allows sending of an email
# requests ping's website
import smtplib
import requests
import logging
# global variables that for the email address and password
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
website = ""
# creates an instance of requests with the get method searching for a
# response from the given website
# (Current website is blank)
r = requests.get(website, timeout=5)

logging.basicConfig(filename='./logging.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def notify_user():
    with smtplib.SMTP('#input email server',   "#input port number as a number") as smtp:

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        logging.info("Sending Email....")
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'The site is currently down'
        body = 'The ' + website + " is currently down and needing attention."
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, "# input a receiver email", msg)


try:
    if r.status_code != 200:
        logging.info("Website is down")
        notify_user()

    else:
        logging.info("website is running")

        notify_user()

except Exception as e:
    logging.info("website is down")
    notify_user()
