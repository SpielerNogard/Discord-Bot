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
import csv
Waffen = ["Acrid","Afuris","Akarius","Akbolto","Akbolto PRime","Akbronco","Akbronco Prime","Akjagara","Akjagara Prime","Aklato","Aklex","Aklex Prime","Akmagnus","Aksomati","Aksomati Prime","Akstiletto","Akstiletto Prime","Akvasto","Akvasto Prime","Akzani","Angstrum","Arca Scisco","Atomos","Azima","Ballistica","Ballistica Prime","Bolto","Brakk","Bronco","Bronco Prime","Castanas","Cestra","Cyanex","Cycron","Despair","Detron","Dex Furis","Dual Cestra","Dual Toxocyst","Embolist","Euphona Prime","Furis","Fusilai","Gammacor","Hikou","Hikou Prime","Hystrix","Knell","Kohmak","Kraken","Kulstar","Kunai","Kuva Brakk","Kuva Kraken","Kuva Nukor","Kuva Seer","Kuva Twin Stubbas","Lato","Lato Prime","Lato Vandal","Lex","Lex Prime","Magnus","Mara Detron","Marelok","MK1-Furis","MK1-Kunai","Nukor","Ocucor","Pandero","Plinx","Pox","Prisma Angstrum","Prisma Twin Gremlins","Pyrana","Pyrana Prime","Quatz","Rakta Ballistica","Sancti Castanas","Secura Dual Cestra","Seer","Sicarus","Sicarus Prime","Sonicor","Spectra","Spectra Vandal","Spira","Spira Prime","Staticor","Stubba","Stug","Synoid Gammacor","Talons","Telos Akbolto","Twin Grakatas","Twin Gremlins","Twin Kohmak","Twin Rogga","Twin Vipers","Twin Vipers Wraith","Tysis","Vasto","Vasto Prime","Vaykor Marelok","Viper","Viper Wraith","Zakti","Zylok"]
def WeaponStats(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
            Out34 = 0
            Out36 = "nicht gefunden"
            python_json_obj = response.text
            python_json_obj = json.loads(python_json_obj)
            Out = python_json_obj["name"]
            Out36 = python_json_obj["wikiaThumbnail"]
            Zeile = "Insert into Sekundär(Waffe,Bild) values('"+str(Out)+"','"+str(Out36)+"');"
            print (Zeile)
            #print (Out36) 
            return(Zeile)
            
    except: 
        print("Fehler")
        
def Waffenauslesen():
    file = open("SQL.txt","w")
    for x in Waffen:
      Zeile = WeaponStats(x)
      file.write(Zeile)
      file.write("\n")
    file.close()

Waffenauslesen() 
#WeaponStats("Shedu")     