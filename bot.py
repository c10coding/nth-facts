# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from fact.fact import Fact
from fact.wordcount import WordCount

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

COMMAND_PREFIX = '.'

client = commands.Bot(command_prefix=COMMAND_PREFIX)

FACTS = {
    'wordcount': Fact("wordcount")
}

VALID_FACT_ARGUMENTS = ['common', 'wordcount', 'lasttype']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(name='fact', help='Tells you whatever fact you wish to know about your discord server.')
async def fact(ctx, fact_name="none"):
    if fact_name == 'none':
        await ctx.send(f'No fact name was given! Use {COMMAND_PREFIX}fact list to see the list of facts!')
    elif fact_name.lower() not in FACTS.keys():
        await ctx.send(f'This is not a valid fact name! Use {COMMAND_PREFIX}fact list to see the list of facts!')
    else:
        current_fact = FACTS.get(fact_name.lower())
        await current_fact.display_fact(ctx)

client.run(TOKEN)