import smtplib
import datetime as dt
import random

MY_EMAIL = ""
PASSWORD = ""
SENDER_EMAIL = ""

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=SENDER_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{random.choice(quotes)}"
        )






