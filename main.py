import datetime as dt
import smtplib
import random

MY_EMAIL = "lukasztest246@gmail.com"
PW = "100daysofcode"
SUNDAY = 6  # day of the test

today = dt.datetime.now().weekday()

with open("quotes.txt") as file:
    lines = file.readlines()
    random_quote = random.choice(lines)


if today == SUNDAY:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=PW
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="zielzor@gmail.com",
            msg=f"Subject:Quote of the day\n\n{random_quote}"
        )

