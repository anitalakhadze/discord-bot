import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.environ['TOKEN']
intents = discord.Intents.all()

bot = commands.Bot(intents=intents, command_prefix='!')

@bot.event
async def on_ready():
    print('bot ready')

@bot.command()
async def ping(ctx):
    print('inside ping')
    await bot.say('Pong')

@bot.event
async def on_message(message: discord.message.Message):
    if message.author == bot.user:
        return

    await message.channel.send(message.content[::-1])

bot.run(TOKEN)