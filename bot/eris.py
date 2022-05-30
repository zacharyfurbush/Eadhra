import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
import discord

# Private Stuff Retrieval
load_dotenv()
TOKEN = os.getenv('TOKEN')
TESTGUILD = os.getenv('TESTGUILD')
MONGOCONNECT = os.getenv('MONGOCONNECT')

# MongoDB Connection
cluster = MongoClient(MONGOCONNECT)
db = cluster['ErisDB']
levels_collection = db['Levels']

# Bot Startup
bot = discord.Client()

# Startup Console Message
@bot.event 
async def on_ready():
    print('Eris is online!') 

# Registers and Processes Messages Sent
@bot.event
async def on_message(ctx):
    if ctx.author.bot: # Author Bot Check
        return

    # Thot Bot: Revival
    if 'thot' in ctx.content.lower():
        await ctx.reply('https://i.imgur.com/RoJ9IYz.jpg')

    author_id = ctx.author.id
    guild_id = ctx.guild.id



bot.run(TOKEN)