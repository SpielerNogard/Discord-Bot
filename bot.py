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
import Levelsystem
import Komandoverwaltung
import FunktionenBot
import aiohttp
import datetime
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print("Changing Status......")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Warframe'))
    print("Status changed")
    print("Start Eidolon Timer......")
    change_status.start()
    print('Eidolon Timer started')
    print("Start Arbitration Tracker......")
    Arbitration_status.start()
    print('Arbitration Tracker started')
    print("Bot is ready.")
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(686438624857948262)
    await channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
@bot.event
async def on_message(Message):
    try:
        Befehl = Message.content
        User = Message.author
        now = datetime.datetime.now()
        Time = now.strftime('%H:%M:%S')
        Ausdruck = str(Time)+": "+str(User)+": "+str(Befehl)
        print(Ausdruck)
        User = Message.author
        channel = Message.channel
        
        #print(User)
        Table = "lvl"
        Anzahl_User = FunktionenBot.counterUser(Table,User)
        #print( str(Anzahl_User))
        WillUserNachrichten = FunktionenBot.UserMessages(Message)
        if Anzahl_User == 0:
            Levelsystem.new_User(User)
        if Anzahl_User >= 1: 
            Levelsystem.new_Message(User)
            embed = Levelsystem.lvl_Up(User)
        if embed !="":
            #print('User schon Vorhanden')
            if WillUserNachrichten<1:
                await User.send(embed=embed)
        Antwort = Komandoverwaltung.get_command(Message)
        if Antwort != "":
            
            await User.send(embed=Antwort)

    except:
        print("Fehler in on message")
@tasks.loop(seconds=30)
async def change_status():
    try:
        url='https://api.warframestat.us/pc/cetusCycle/'
        with requests.get(url) as response:
            python_json_obj = response.text
            python_json_obj = json.loads(python_json_obj)
            Out = python_json_obj["shortString"]
            if Out == '5m to Night' or Out=='4m to Night' or Out== '3m to Night' or Out== '2m to Night' or Out== '1m to Night' or Out=='5m to Day' or Out=='4m to Day' or Out=='3m to Day' or Out=='2m to Day' or Out=='1m to Day':
                print(Out)
                Message  = Out
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="bSIxubcT1RprBlNi",
                database="warframe"
                )
                
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM eidolon")
                myresult = mycursor.fetchall()
                for x in myresult:
                    id = x[0]
                    sendung = x[1]
                    embed=discord.Embed(title="Eidolon Clock", description="Time of Cetus", color=0x00ffff)
                    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/7/73/Teralyst.png/revision/latest?cb=20171016171720")
                    embed.add_field(name="Time", value=Out, inline=False)
                    channel = bot.get_channel(int(sendung))
                    await channel.send(embed=embed)
            print(Out)
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(Out))
    except:
        print('Fehler im Eidolon Timer')
@tasks.loop(minutes = 1)
async def Arbitration_status():
    try:
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
            
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="bSIxubcT1RprBlNi",
                database="warframe"
                )
                
            mycursor = mydb.cursor()
            sql = "SELECT * FROM arbitration WHERE id = 1"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                id = x[0]
                Plattform = x[1]
                Ort = x[2]
                print('Enthalten ist gerade: '+Ort)
                if(Ort == Arbitration):
                    print('I dont need to change Arbitration')
                if(Ort != Arbitration):
                    print(Arbitration)
                    sql = "UPDATE arbitration SET Arbitration = '"+Arbitration+"' WHERE id=1"
                    mycursor.execute(sql)
                    mydb.commit()
                    print('Arbitration updated')
                    mycursor.execute("SELECT * FROM arbitrationtracker")
                    channelausgabe = mycursor.fetchall()
                    for a in channelausgabe:
                        id = a[0]
                        sendung = a[1]
                        channel = bot.get_channel(int(sendung))
                        embed=discord.Embed(title="Arbitration", description="a new arbitration is available", color=0x0080ff)
                        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/b/b9/VitusEssence.png/revision/latest?cb=20190923095056")
                        embed.add_field(name="Ort", value=Arbitration, inline=False)
                        await channel.send(embed=embed)
                       
    except:
        print('Fehler beim checken des Arbitration_Status')
        
        
bot.run(token)