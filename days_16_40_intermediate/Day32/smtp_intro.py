import smtplib

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="robert.laksee20@gmail.com",
                        msg="Subject:Greetings\n\nHello bro this is working!!")
