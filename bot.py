import telebot
import requests
from flask import Flask
from threading import Thread
import os

# --- FLASK SERVER TO KEEP ALIVE ---
app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------------

API_TOKEN = os.getenv('BOT_TOKEN') # Using Env Variable for security
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Truecaller Lookup is active! Send a number.")

@bot.message_handler(func=lambda message: True)
def lookup(message):
    # (Insert the lookup logic from my previous response here)
    pass

if __name__ == "__main__":
    keep_alive()  # Starts the web server
    print("Bot is running...")
    bot.infinity_polling()
  
