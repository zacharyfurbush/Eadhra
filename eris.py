import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
import discord
from discord.ext import commands

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
    author_id = ctx.author.id
    guild_id = ctx.guild.id

    if author_id != '924400948707745802': # If the message author is Eris, it wont reply

        # Thot Bot v2
        if 'thot' in ctx.content.lower():
            await ctx.reply('https://i.imgur.com/RoJ9IYz.jpg')
        


bot.run(TOKEN)