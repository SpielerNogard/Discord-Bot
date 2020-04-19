import os
import random
import mysql.connector
import asyncio
import requests
import io
import discord
import requests
import json
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle
import aiohttp

def Hilfe():
    embed=discord.Embed(title="Help", description="my help page", color=0x0080ff)
    embed.set_thumbnail(url="")
    embed.add_field(name="!Arbitration", value="Shows you the running Arbitration", inline=False)
    embed.add_field(name="!Weapon {arg}", value="Find your Weapon ", inline=False)
    embed.add_field(name="!Search {arg}", value="Find the Spot with the highest Drop Chance for every Item", inline=False)
    embed.add_field(name="!Trader", value="Shows you all Items from actual Baro Ki`Teer ", inline=False)
    embed.add_field(name="!Darvo", value="Shows you the current Deal", inline=False)
    embed.add_field(name="!Arcane {arg}", value="Shows you a lot of onformations abaut a Arcane", inline=False)
    embed.add_field(name="!Frame", value="Randomize a Warframe for you ", inline=False)
    embed.add_field(name="!Primary", value="Randomize a primary Weapon for you ", inline=False)
    embed.add_field(name="!Secondary", value="Randomize a secondary Weapon for you ", inline=False)
    embed.add_field(name="!noMessages", value="The Bot dont send you DM for LVL UP ", inline=False)
    return(embed)