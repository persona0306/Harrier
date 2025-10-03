import os
import discord
from discord.ext import commands

TOKEN = os.environ.get('HARRIER_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

if __name__ == '__main__':
    if not TOKEN:
        raise ValueError("HARRIER_TOKEN environment variable not set.")
    bot.run(TOKEN)
