''' Extra Hard Starting Project '''
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
#    person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

from datetime import datetime
from random import randint
import smtplib
import pandas as pd



def send_email(email_to_send, subject, message):
    ''' Send the email '''
    email = "laurasofi0507@gmail.com"
    password = "szgbhjjvkczlysfw"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email_to_send,
            msg=f"Subject:{subject}\n\n{message}"
        )

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index,
                                                                      data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"

    with open(file_path, encoding="utf-8") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    send_email(birthday_person["email"], "Happy Birthday!", contents)
