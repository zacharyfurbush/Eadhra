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

@bot.event 
async def on_ready():
    print('Eris is online!') # Startup Console Message

@bot.event
async def on_message(ctx):
    author_id = ctx.author.id
    guild_id = ctx.guild.id

    if author_id != '924400948707745802':

        # Thot Bot v2
        if 'thot' in ctx.content:
            await ctx.reply(file=discord.file('Thot.jpg'))
        
        

bot.run(TOKEN)