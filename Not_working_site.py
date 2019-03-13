# import statements
# smtplib allows sending of an email
# requests ping's website
import smtplib
import requests
# global variables that for the email address and password
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
website = ""
# creates an instance of requests with the get method searching for a
# response from the given website
# (Current website is blank)
r = requests.get(website, timeout=5)

if r.status_code != 200:
    with smtplib.SMTP('#input email server',   "#input port number as a number") as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'The site is currently down'
        body = 'The ' + website + " is currently down and needing attention."
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, "# input a receiver email", msg)
