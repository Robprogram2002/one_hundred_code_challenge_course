import random
import datetime as dt
import smtplib as smt
import pandas as pd

data = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
month, day = now.month, now.day

my_email = ""
password = ""

for (index, row) in data.iterrows():
    if row.month == month and row.day == day:
        x = random.randint(1, 3)
        with open(f"./letter_templates/letter_{x}.txt") as letter:
            text = letter.read().replace("[NAME]", row["name"])

        with smt.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row.email,
                                msg=f"Subject: Happy Birthday !! \n\n{text}")
