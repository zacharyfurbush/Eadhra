import os
import hikari
import lightbulb
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD_ID = os.getenv('GUILD_ID')
bot = lightbulb.BotApp(token = TOKEN, default_enabled_guilds=(GUILD_ID))

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

bot.run()