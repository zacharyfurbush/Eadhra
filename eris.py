import os
from dotenv import load_dotenv
import pymongo
from pymongo import mongo_client
import discord
from discord.ext import commands

# Private Stuff Retrieval
load_dotenv()
TOKEN = os.getenv('TOKEN')
TESTGUILD = os.getenv('TESTGUILD')
MONGOCONNECT = os.getenv('MONGOCONNECT')

# MongoDB Connection
cluster = mongo_client(MONGOCONNECT)
db = cluster['ErisDB']
levels_collection = db['Levels']

# Bot Startup
bot = discord.Client()

@bot.event 
async def on_ready():
    print('Eris is online!') # Startup Console Message

@bot.event
async def on_message(ctx):
    author_id = ctx.author.id
    guild_id = ctx.guild.id

    # Thot Bot
    if ctx.message('thot'):
        print('oh no')

bot.run(TOKEN)