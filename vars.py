# Don't Remove Credit Tg - @Tushar0125
# Ask Doubt on telegram @Tushar0125

from os import environ

API_ID = int(environ.get("API_ID", "22946135")) #Replace with your api id
API_HASH = environ.get("API_HASH", "93e1b0c387cabe34a3ccfa1724ae8527") #Replace with your api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "8330388328:AAF3IVnhiVJ66JmdvI7ZiRXdlWTVt-2KCY4") #Replace with your bot token

# Database Configuration for MongoDB
# Example: "mongodb://user:password@host:port/dbname"
# For MongoDB Atlas: "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<dbname>?retryWrites=true&w=majority"
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://vikrammishra9210_db_user:UWMwNO0M5sFslW4o@cluster0.ollhem3.mongodb.net/?appName=Cluster0")
# Replace "your_bot_db" with your desired database name.
# For local testing, you might use "mongodb://localhost:27017/your_bot_db"
