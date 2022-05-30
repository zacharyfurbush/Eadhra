import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
import discord
from discord import app_commands # refer https://github.com/Digiwind/Digiwind-Videos/blob/main/DPY%20Slash%20Commands.py

# Private Stuff Retrieval
load_dotenv()
TOKEN = os.getenv('TOKEN')
TESTGUILD = os.getenv('TESTGUILD')
MONGOCONNECT = os.getenv('MONGOCONNECT')

# MongoDB Connection
cluster = MongoClient(MONGOCONNECT)
db = cluster['ErisDB']
levels_collection = db['Levels']


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=TESTGUILD))
            self.synced = True
        print('Eris is online!') 

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'Ping', description = 'Pings Eris', id = TESTGUILD)
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message('Pong! 🏓', ephemeral = True)

client.run(TOKEN)

# # Bot Startup
# bot = discord.Client()

# # Startup Console Message
# @bot.event 
# async def on_ready():
#     print('Eris is online!') 

# # Registers and Processes Messages Sent
# @bot.event
# async def on_message(ctx):
#     if ctx.author.bot: # Author Bot Check
#         return

#     # Thot Bot: Revival
#     if 'thot' in ctx.content.lower():
#         await ctx.reply('https://i.imgur.com/RoJ9IYz.jpg')

#     author_id = ctx.author.id
#     guild_id = ctx.guild.id

# @bot.slash_command
        


# bot.run(TOKEN)