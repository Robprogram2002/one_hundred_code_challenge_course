import smtplib
import random
import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))

year = now.year
print(year)
print(type(year))

month = now.month
day = now.day
week_day = now.weekday()
print(year, month, day, week_day)

date_of_birth = dt.datetime(year=2002, day=20, month=2, hour=19)
print(date_of_birth)

# Ej 1: send a motivational quote on mondays
my_email = ""
password = ""

if dt.datetime.now().weekday() == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        x = random.randint(0, len(quotes) - 1)
        author = quotes[x].split("-")[-1].strip()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="robert.laksee20@gmail.com",
                                msg=f"Subject:Monday motivation, {author} \n\n{quotes[x]} ")
