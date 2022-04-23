import os
import hikari
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = hikari.GatewayBot(token = TOKEN)
bot.run()