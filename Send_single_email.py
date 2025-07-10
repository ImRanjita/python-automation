import yagmail
import os

sender = "lakshmibanu703@gmail.com"
receiver = "059jagesw4@mailpwr.com"

subject = "Test Email"

contents = "This is a test email sent using yagmail."

my_email = os.getenv('email')

my_password = os.getenv('password')

yag = yagmail.SMTP(user=my_email, password=my_password)
yag.send(to=receiver, subject=subject, contents=contents)

print("email sent successfully!")