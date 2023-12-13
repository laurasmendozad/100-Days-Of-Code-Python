''' Stock Trading News '''
import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "QLH4MF2OSZ5OKWMX"
NEWS_API_KEY = "c95110b974f44bad932896364b129c42"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # When stock price increase/decreases by 5% between yesterday and the day before yesterday then
    # print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python
# dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_resp = requests.get(STOCK_ENDPOINT, params=stock_params, timeout=10)
data_list = [value for (key,value) in stock_resp.json()["Time Series (Daily)"].items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#TODO 2. - Get the day before yesterday's closing stock price

beforeyesterday_data = data_list[1]
beforeyesterday_closing_price = beforeyesterday_data["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive
# difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(beforeyesterday_closing_price)
if difference < 0:
    EMOJI = "🔻"
else:
    EMOJI = "🔺"
positive_diference = abs(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing
# price the day before yesterday.

diff_percent = (positive_diference / float(yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if diff_percent > 5:
    # print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the
# COMPANY_NAME.

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title"
    }

    news_resp = requests.get(NEWS_ENDPOINT, params=news_params, timeout=10)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    articles = news_resp.json()["articles"][:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list
# comprehension.

    formatted_articles = [STOCK_NAME+": "+EMOJI+" "+str(round(diff_percent,2))+"%\n"
                          "Headline: "+
                          article["title"]+". \n Brief: "+
                          article["description"] for article in articles]

#TODO 9. - Send each article as a separate message via Twilio.

    for m in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=m,
                            from_='+13858326743',
                            to='+573178923835'
                        )

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors
are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions
as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors
are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions
as of March 31st, near the height of the coronavirus market crash.
"""
