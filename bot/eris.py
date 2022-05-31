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
        return

    # Bueno Bot: Origins
    if 'bueno' or 'good' or 'nice' or 'cool' or 'excellent' or 'great' in ctx.content.lower():
        await ctx.reply('https://i.imgur.com/a4pQcxn.jpg')
        return

    # Virgin Bot: Vengence
    if 'no maidens' or 'virgin' or 'no bitches' or 'no hoes' in ctx.content.lower():
        await ctx.repl('https://i.imgur.com/bTfmaZA.jpg')
        return

    author_id = ctx.author.id
    guild_id = ctx.guild.id



bot.run(BOTTOKEN)