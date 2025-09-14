import requests
from bs4 import BeautifulSoup
import time
import telebot

# 🔹 Replace with your own Telegram Bot token
BOT_TOKEN = "8440996677:AAFk6y5wQI3VEoh8kb6CSfemMWs1UGFWtW0"
CHAT_ID = "8372126524"
bot = telebot.TeleBot(BOT_TOKEN)

URL = "https://www.stwdo.de/en/living-houses-application/current-housing-offers"
last_seen = ""

def check_dorms():
    global last_seen
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract offers (table rows or divs containing dorms)
    offers = soup.find_all("div", class_="ce-table")  # adjust if structure changes
    text = soup.get_text().lower()

    if "no current housing offers" not in text:  # means something is listed
        if text != last_seen:  # prevent duplicate alerts
            last_seen = text
            bot.send_message(CHAT_ID, "🏠 Dorm available! Check here: " + URL)

while True:
    check_dorms()
    time.sleep(600)  # check every 10 minutes
