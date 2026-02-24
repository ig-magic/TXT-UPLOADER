from flask import Flask
from main import bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Start bot once when app loads
bot.start()
