# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.')

VALID_FACT_ARGUMENTS = ['common', 'wordcount', 'lasttype']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(name='fact', help='Tells you whatever fact you wish to know about your discord server.')
async def fact(ctx):
    await ctx.send('')

client.run(TOKEN)