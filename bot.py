import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands

import aiohttp
import asyncio
import json
import re
import tracemalloc
import os
import requests
tracemalloc.start()

with open('config/config.json') as f:
    config = json.load(f)
    token = config['token']
    prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print("Logged in!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(token)
