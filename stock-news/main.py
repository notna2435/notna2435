import requests
from twilio.rest import Client
import time

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "****************"
NEWS_API_KEY = "********************************"
TWILIO_SID = "********************************"
TWILIO_AUTH_TOKEN = "***************************"

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]

#Find the positive difference between 1 and 2.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price))

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    #Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body="This is a test message",
            from_="+18776186739",
            to="+19788094083",
        )
        time.sleep(5)
        print(message.sid)
