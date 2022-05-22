import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()

bot = discord.Client()

@bot.event
async def on_ready():
    print('Eris is online!')

bot.run(os.getenv('TOKEN'))