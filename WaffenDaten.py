import random
from random import *
import mysql.connector
import requests
import json
import discord

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="warframe"
)
mycursor = mydb.cursor()
def WeaponCategory(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
            python_json_obj = response.text
            python_json_obj = json.loads(python_json_obj)
            Category = python_json_obj["category"]
    except:
        print("Konnte Kategorie nicht feststellen")  
        Category = "Konnte Kategorie nicht feststellen"
    return(Category)
def Weapon(Weapon):
    try:
        Category = WeaponCategory(Weapon)
        if Category == "Secondary":
            url='https://api.warframestat.us/weapons/'+Weapon
            with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                Name = python_json_obj["name"]
                Beschreibung = python_json_obj["description"]
                Bild = python_json_obj["wikiaThumbnail"]
                MagazinGröße = python_json_obj["magazineSize"]
                Nachladezeit = python_json_obj["reloadTime"]
                CritChance = python_json_obj["criticalChance"]
                CritMultiplier = python_json_obj["criticalMultiplier"]
                Damage = python_json_obj["damage"]
                Damageverteilung = python_json_obj["damageTypes"]
                Firerate = python_json_obj["fireRate"]
                Statuschance = python_json_obj["procChance"]
                Mastery = python_json_obj["masteryReq"]
                Riven = python_json_obj["disposition"]
                Noise = python_json_obj["noise"]
                Link = python_json_obj["wikiaUrl"]
                #Ausgabe
                embed=discord.Embed(title=str(Name), description="Deine Ergebnisse: ", color=0xff0000)
                embed.set_thumbnail(url=Bild)
                embed.add_field(name="Beschreibung", value=str(Beschreibung), inline=False)
                embed.add_field(name="MagazinGröße", value=str(MagazinGröße), inline=True)
                embed.add_field(name="Nachladezeit", value=str(Nachladezeit), inline=True)
                embed.add_field(name="Crit Chance", value=str(CritChance), inline=True)
                embed.add_field(name="Crit Multiplier", value=str(CritMultiplier), inline=True)
                embed.add_field(name="Statuschance", value=str(Statuschance), inline=True)
                embed.add_field(name="Damage", value=str(Damage), inline=True)
                embed.add_field(name="Damage Verteilung", value=str(Damageverteilung), inline=True)
                embed.add_field(name="Firerate", value=str(Firerate), inline=True)
                embed.add_field(name="Benötigter Mastery Rank", value=str(Mastery), inline=True)
                embed.add_field(name="Riven Dispo", value=str(Riven), inline=True)
                embed.add_field(name="Lautstärke", value=str(Noise), inline=True)
                embed.add_field(name="Category", value="Primary", inline=True)
                embed.add_field(name="mehr Informationen", value=str(Link), inline=True)
                
        if Category == "Melee":
            url='https://api.warframestat.us/weapons/'+Weapon
            with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                Name = python_json_obj["name"]
                Beschreibung = python_json_obj["description"]
                Bild = python_json_obj["wikiaThumbnail"]
                Attackspeed = python_json_obj["secondsPerShot"]
                CritChance = python_json_obj["criticalChance"]
                CritMultiplier = python_json_obj["criticalMultiplier"]
                Damage = python_json_obj["damage"]
                Damageverteilung = python_json_obj["damageTypes"]
                Firerate = python_json_obj["fireRate"]
                Statuschance = python_json_obj["procChance"]
                Mastery = python_json_obj["masteryReq"]
                Riven = python_json_obj["disposition"]
                Spin = python_json_obj["spinAttack"]
                Leap = python_json_obj["leapAttack"]
                Wall = python_json_obj["wallAttack"]
                Link = python_json_obj["wikiaUrl"]
                Typ = python_json_obj["type"]
                #Ausgabe
                embed=discord.Embed(title=str(Name), description="Deine Ergebnisse: ", color=0xff0000)
                embed.set_thumbnail(url=Bild)
                embed.add_field(name="Beschreibung", value=str(Beschreibung), inline=False)
                embed.add_field(name="Typ", value=str(Typ), inline=True)
                embed.add_field(name="Attackspeed", value=str(Attackspeed), inline=True)
                embed.add_field(name="Crit Chance", value=str(CritChance), inline=True)
                embed.add_field(name="Crit Multiplier", value=str(CritMultiplier), inline=True)
                embed.add_field(name="Statuschance", value=str(Statuschance), inline=True)
                embed.add_field(name="Damage", value=str(Damage), inline=True)
                embed.add_field(name="Damage Verteilung", value=str(Damageverteilung), inline=True)
                embed.add_field(name="Benötigter Mastery Rank", value=str(Mastery), inline=True)
                embed.add_field(name="Riven Dispo", value=str(Riven), inline=True)
                embed.add_field(name="Spin Attack", value=str(Spin), inline=True)
                embed.add_field(name="Leap Attack", value=str(Leap), inline=True)
                embed.add_field(name="Wall Attack", value=str(Wall), inline=True)
                embed.add_field(name="Category", value="Melee", inline=True)
                embed.add_field(name="mehr Informationen", value=str(Link), inline=True)
                
        if Category == "Primary":
            url='https://api.warframestat.us/weapons/'+Weapon
            with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                Name = python_json_obj["name"]
                Beschreibung = python_json_obj["description"]
                Bild = python_json_obj["wikiaThumbnail"]
                MagazinGröße = python_json_obj["magazineSize"]
                Nachladezeit = python_json_obj["reloadTime"]
                CritChance = python_json_obj["criticalChance"]
                CritMultiplier = python_json_obj["criticalMultiplier"]
                Damage = python_json_obj["damage"]
                Damageverteilung = python_json_obj["damageTypes"]
                Firerate = python_json_obj["fireRate"]
                Statuschance = python_json_obj["procChance"]
                Mastery = python_json_obj["masteryReq"]
                Riven = python_json_obj["disposition"]
                Noise = python_json_obj["noise"]
                Link = python_json_obj["wikiaUrl"]
                #Ausgabe
                embed=discord.Embed(title=str(Name), description="Deine Ergebnisse: ", color=0xff0000)
                embed.set_thumbnail(url=Bild)
                embed.add_field(name="Beschreibung", value=str(Beschreibung), inline=False)
                embed.add_field(name="MagazinGröße", value=str(MagazinGröße), inline=True)
                embed.add_field(name="Nachladezeit", value=str(Nachladezeit), inline=True)
                embed.add_field(name="Crit Chance", value=str(CritChance), inline=True)
                embed.add_field(name="Crit Multiplier", value=str(CritMultiplier), inline=True)
                embed.add_field(name="Statuschance", value=str(Statuschance), inline=True)
                embed.add_field(name="Damage", value=str(Damage), inline=True)
                embed.add_field(name="Damage Verteilung", value=str(Damageverteilung), inline=True)
                embed.add_field(name="Firerate", value=str(Firerate), inline=True)
                embed.add_field(name="Benötigter Mastery Rank", value=str(Mastery), inline=True)
                embed.add_field(name="Riven Dispo", value=str(Riven), inline=True)
                embed.add_field(name="Lautstärke", value=str(Noise), inline=True)
                embed.add_field(name="Category", value="Primary", inline=True)
                embed.add_field(name="mehr Informationen", value=str(Link), inline=True)
    except:
        print("Fehler in Weapon")  
        
        embed=discord.Embed(title="Fehler", description="Deine Ergebnisse: ", color=0xff0000)
        embed.set_thumbnail('https://imnamenderliebe.com/wp-content/uploads/2015/01/Fehler.jpg')
        embed.add_field(name="Beschreibung", value="Es ist Leider ein Fehler aufgetreten", inline=False)
    return(embed)
def getDamage(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                CritChance = python_json_obj["criticalChance"]
                CritMultiplier = python_json_obj["criticalMultiplier"]
                Damage = python_json_obj["damageTypes"]
                Damage = json.dumps(Damage)
                print(Damage)
                python_json_obj = json.loads(Damage)
                if "impact" in Damage:
                    Impact = python_json_obj["impact"]
                    print("Impact: "+str(Impact))
                if "slash" in Damage:
                    Slash = python_json_obj["slash"]
                    print("Slash: "+str(Slash))
                if "puncture" in Damage:
                    Puncture = python_json_obj["puncture"]
                    print("Puncture: "+str(Puncture))
                if "electricity" in Damage:
                    electricity = python_json_obj["electricity"]
                    print("electricity: "+str(electricity))
                if "toxin" in Damage:
                    toxin = python_json_obj["toxin"]
                    print("toxin: "+str(toxin))
                if "magnetic" in Damage:
                    magnetic = python_json_obj["magnetic"]
                    print("magnetic: "+str(magnetic))
                if "radiation" in Damage:
                    radiation = python_json_obj["radiation"]
                    print("radiation: "+str(radiation))
                return(Damage)
    except:
        print("Fehler in getDamage")
    
  