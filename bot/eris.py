import os
import requests
from dotenv import load_dotenv
import mysql.connector
import discord

# SSL Certificate Verification Fix
requests.get('https://discord.com', verify=True)

# Private Stuff Retrieval
load_dotenv()
BOTTOKEN = os.getenv('BOTTOKEN')
TESTGUILD = os.getenv('TESTGUILD')
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DBPORT = os.getenv('DBPORT')
DBNAME = os.getenv('DBNAME')

# ErisDB Connection
db = mysql.connector.connect(
    host = DBHOST, 
    user = DBUSER,
    password = DBPASS,
    port = DBPORT,
    database = DBNAME
    )

# Bot Startup
bot = discord.Client()

# Startup Console Message
@bot.event 
async def on_ready():
    print('Eadhra is online!') 

# Registers and Processes Messages Sent
@bot.event
async def on_message(ctx):
    if ctx.author.bot: # Author Bot Check
        return

    # Thot Bot: Revival
    if 'thot' in ctx.content.lower():
        await ctx.reply('https://i.imgur.com/RoJ9IYz.jpg')

    # Bueno Bot: Origins
    if 'bueno' or 'good' or 'nice' in ctx.content.lower():
        await ctx.reply('https://imgur.com/a/FuuYEUV.png')

    author_id = ctx.author.id
    guild_id = ctx.guild.id



bot.run(BOTTOKEN)