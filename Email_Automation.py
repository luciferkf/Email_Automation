import os 
import smtplib
import csv
import pandas

def automatic_email():
    sender_email = 'enter your email'
    app_password = "enter your google app password"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, app_password)

    with open("Rahul.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row['name']
            email = row['email']

            with open("Text.txt") as msg_file:
                message_content = msg_file.read()

            message = f"""Subject: Important Message

Dear {name},

{message_content}

Regards,
Rahul
"""

            s.sendmail(sender_email, email, message)
            print("Email sent to", email)

    s.quit()
    print("All emails sent successfully!")

automatic_email()