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
import datetime
import WaffenDaten
import Hilfe
import Arbitration
import FunktionenBot
import DamageSimulator

def get_command(Message):
    channel = Message.channel
    if Message.content.startswith("!help"):
        try:
            embed=Hilfe.Hilfe()
           
            return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Es ist ein Fehler im Hilfebefehl aufgetreten", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Weapon"):
        try:
           Suche = Message.content
           Weapon = Suche.replace("!Weapon ", "")
           embed = WaffenDaten.Weapon(Weapon)
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Trader"):
        try:
           embed = FunktionenBot.getTrader()
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Darvo"):
        try:
           embed = FunktionenBot.getDailyDeals()
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Frame"):
        try:
           id = FunktionenBot.counter('warframes')
           Zahl = FunktionenBot.randomizer(1,id)
           Out = FunktionenBot.selectWarframe(Zahl)
           Link = FunktionenBot.selectWarframelink(Zahl)
           embed=discord.Embed(title="Warframe", description="Dein gewählter Frame:", color=0x0080ff)
           embed.set_thumbnail(url=Link)
           embed.add_field(name="Frame", value=Out, inline=False)
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Primary"):
        try:
           id = FunktionenBot.counter('primär')
           Zahl = FunktionenBot.randomizer(1,id)
           Out = FunktionenBot.selectprimary(Zahl)
           Link = FunktionenBot.selectprimarylink(Zahl)
           embed=discord.Embed(title="Primary", description="Deine gewählte Primary:", color=0x0080ff)
           embed.set_thumbnail(url=Link)
           embed.add_field(name="Weapon", value=Out, inline=False)
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Secondary"):
        try:
           id = FunktionenBot.counter('sekundär')
           Zahl = FunktionenBot.randomizer(1,id)
           Out = FunktionenBot.selectsecondary(Zahl)
           Link = FunktionenBot.selectsecondarylink(Zahl)
           embed=discord.Embed(title="Secondary", description="Deine gewählte Secondary:", color=0x0080ff)
           embed.set_thumbnail(url=Link)
           embed.add_field(name="Weapon", value=Out, inline=False)
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Arcane"):
        try:
           Suche = Message.content
           arg1 = Suche.replace("!Arcane ", "")
           embed = FunktionenBot.getArcanes(arg1)
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
            
    if Message.content.startswith("!Search"):
        try:
           Suche = Message.content
           Eingabe = Suche.replace("!Search ", "")
           embed = FunktionenBot.foundbestSpot(Eingabe)
           return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Sorry i can't find your Weapon", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Arbitration"):
        try:
            embed = Arbitration.Arbitration()
            return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Es ist ein Fehler im Arbitrationtracker aufgetreten", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!Damage"):
        try:
            Suche = Message.content
            Eingabe = Suche.replace("!Damage ", "")
            Eingabe = DamageSimulator.Damage_Simulator(Eingabe)
            embed = Arbitration.Arbitration()
            return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Es ist ein Fehler im Arbitrationtracker aufgetreten", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!noMessages"):
        try:
            FunktionenBot.nomessages(Message)
            embed = Arbitration.Arbitration()
            return(embed)
        except:
            embed=discord.Embed(title="Fehler", description="Es ist ein Fehler im Arbitrationtracker aufgetreten", color=0x0080ff)
            embed.set_thumbnail(url="https://www.deutsche-startups.de/app/uploads/2014/08/ds-fehler-wolken.jpg")
            return(embed)
    if Message.content.startswith("!patch"):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="warframe"
        )
        mycursor = mydb.cursor()
        idpatches = FunktionenBot.counter('patches')
        sql = "SELECT * FROM patches WHERE id ="+str(idpatches)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            id = x[0]
            Version = x[1]
            Text = x[2]
            mycursor.execute("SELECT * FROM patchnotes")
            channelausgabe = mycursor.fetchall()
            for a in channelausgabe:
                id = a[0]
                sendung = a[1]
                channel = bot.get_channel(int(sendung))
                Ausgabe= "```"+Text+"```"
                Title = "Patch "+str(Version)
                embed=discord.Embed(title=Title, description=Ausgabe, color=0x0080ff)
                embed.set_thumbnail(url="https://heise.cloudimg.io/width/1019/q50.png-lossy-50.webp-lossy-50.foil1/_www-heise-de_/imgs/18/2/6/6/3/3/8/4/geralt9-fc3553703abd451a.png")
        return(embed)        