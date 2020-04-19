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

def Arbitration():
    url='https://api.warframestat.us/pc/arbitration'
    with requests.get(url) as response:
        python_json_obj = response.text
        python_json_obj = json.loads(python_json_obj)
        Out = python_json_obj["node"]
        Out1 = python_json_obj["enemy"]
        Out2 = python_json_obj["type"]
        Out3 = python_json_obj["activation"] 
        Out4 = python_json_obj["expiry"]
        Arbitration = 'Ort: '+Out+' ('+Out1+') '+Out2
        embed=discord.Embed(title="Arbitration", description="The actual Arbitration", color=0x0080ff)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/b/b9/VitusEssence.png/revision/latest?cb=20190923095056")
        embed.add_field(name="Ort", value=Arbitration, inline=False)
    return(embed)