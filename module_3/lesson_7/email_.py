import smtplib
import time
from email.message import EmailMessage


email_address = "absaitovdev@gmail.com"
email_password = "ldxzpmbnjstihsng"


email_list = """saidakbaruraimov7@gmail.com
mohirmirahmadov@gmail.com
zoirbekergashev4567@gmail.com
khayrullo.devs@gmail.com
imonqulovf1234@gmail.com
samidilloravshanov13@gmail.com
shahrizodaxakimova12@gmail.com
9140380@gmail.com
shohjahonobruyev3@gmail.com
diyorbekdilmurodov1@gmail.com
suratovdoniyor@gmail.com
dilshodbekakhmatov@gmail.com
nurillayevezozbek@gmail.com
saidakbaruraimov7@gmail.com
mohirmirahmadov@gmail.com
zoirbekergashev4567@gmail.com
 azamovshahboz06082001@gmail.com""".split()
# create email


start = time.time()
for i in email_list:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        msg = EmailMessage()
        msg['Subject'] = "Email subject"
        msg['From'] = email_address
        msg['To'] = i
        msg.set_content("This is eamil message")
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("send mail !")
print(time.time() - start)

