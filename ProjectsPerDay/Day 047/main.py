''' Amazon Proce Tracker '''
import os
import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

# Step 1 - Use BeautifulSoup to Scrape the Product Price
URL = "https://www.amazon.com/-/es/dp/B071HHXB27/ref=twister_B07HMKDM6N"

headers = {
    "Accept-Language": "es,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

response = requests.get(URL, headers=headers, timeout=10)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_number = float(price.split("$")[1])


# Step 2 - Email Alert When Price Below Preset Value
def send_email(subject, message):
    ''' Send the email '''
    email = "laurasofi0507@gmail.com"
    password = os.environ.get("APP_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="laurasofi0507@hotmail.com",
            msg=f"Subject:{subject}\n\n{message}".encode("utf-8")
        )

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 70

if price_number < BUY_PRICE:
    send_email("Amazon Price Alert!", f"{title} is now in {price}\n{URL}")
