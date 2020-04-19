import os
import random
import mysql.connector
import asyncio
import requests
import io
import json
import aiohttp
import datetime
import Eingabezerlegung

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
def get_Damage_per_second(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                damagePerSecond = python_json_obj["damagePerSecond"]
        return(damagePerSecond)
    except:
        print("Fehler in get_Damage_per_second")
def effectiveHealth(LVL):
    try:
        Health = 800
        BaseArmor = 500
        BaseHealth = 300
        BaseLevel = 8
        Currentlevel = int(LVL)
        CurrentArmor = BaseArmor*(1+(((Currentlevel-BaseLevel)**1.75)*0.005))
        CurrentHealth = BaseHealth *(1+(((Currentlevel-BaseLevel)**2)*0.015))
        CurrentEffectiveHitpoints = CurrentHealth* ( 1 + CurrentArmor / 300 )
        Health = CurrentEffectiveHitpoints
        return(Health)
    except:
        print("Fehler in effectiveHealth")
def get_Status_Chance(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                damagePerSecond = python_json_obj["procChance"]
                damagePerSecond = damagePerSecond*100
        return(damagePerSecond)
    except:
        print("Fehler in get_Status_Chance")
def get_crit_chance(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                damagePerSecond = python_json_obj["criticalChance"]
                damagePerSecond = damagePerSecond*100
        return(damagePerSecond)
    except:
        print("Fehler in get_crit_chance")
def get_crit_multi(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
                #Json Object erhalten
                python_json_obj = response.text
                python_json_obj = json.loads(python_json_obj)
                #Json Object auslesen
                damagePerSecond = python_json_obj["criticalMultiplier"]
        return(damagePerSecond)
    except:
        print("Fehler in get_crit_chance")
def get_FullDamage(Damagejson):
    FullDamage = 0
    Damage = Damagejson
    python_json_obj = json.loads(Damagejson)
    if "impact" in Damage:
        Impact = python_json_obj["impact"]
        FullDamage = FullDamage+Impact
    if "slash" in Damage:
        Slash = python_json_obj["slash"]
        FullDamage = FullDamage+Slash
    if "puncture" in Damage:
        Puncture = python_json_obj["puncture"]
        FullDamage = FullDamage+Puncture
    if "electricity" in Damage:
        electricity = python_json_obj["electricity"]
        FullDamage = FullDamage+electricity
    if "toxin" in Damage:
        toxin = python_json_obj["toxin"]
        FullDamage = FullDamage+toxin
    if "magnetic" in Damage:
        magnetic = python_json_obj["magnetic"]
        FullDamage = FullDamage+magnetic
    if "radiation" in Damage:
        radiation = python_json_obj["radiation"]
        FullDamage = FullDamage+radiation
    
    return(FullDamage)
def Statustypefinden(Impactchance,Slashchance,Puncturechance,Electricitychance,Toxinchance,Magneticchance,Radiationchance):
    Statustype="nothing"
    randomzahl = random.randint(0,100)
    print(str(randomzahl))
    if randomzahl < Impactchance:
        print("Impact")
        Statustype = "Impact"
    if randomzahl < Slashchance:
        print("Slash")
        Statustype = "Slash"
    if randomzahl < Puncturechance:
        print("Puncture")
        Statustype = "Puncture"
    if randomzahl < Electricitychance:
        print("Electricity")
        Statustype = "Electricity"
    if randomzahl < Toxinchance:
        print("Toxin")
        Statustype = "Toxin"
    if randomzahl < Magneticchance:
        print("Magnetic")
        Statustype = "Magnetic"
    if randomzahl < Radiationchance:
        print("Radiation")
        Statustype = "Radiation"
    return(Statustype)
def Status_taken(FullDamage, Damagejson):
    try:
        Statustype = "nothing"
        Damage = Damagejson
        python_json_obj = json.loads(Damagejson)
        Impactchance = 0
        Slashchance = 0
        Puncturechance = 0
        Electricitychance = 0
        Magneticchance = 0
        Radiationchance = 0
        Toxinchance = 0
        if "impact" in Damage:
            Impact = python_json_obj["impact"]
            Impactchance = (Impact/FullDamage)*100
            print("ImpactChance: "+str(Impactchance))
        if "slash" in Damage:
            Slash = python_json_obj["slash"]
            Slashchance = (Slash/FullDamage)*100
            print("Slashchance: "+str(Slashchance))
        if "puncture" in Damage:
            Puncture = python_json_obj["puncture"]
            Puncturechance = (Impact/FullDamage)*100
            print("Puncturechance: "+str(Puncturechance))
        if "electricity" in Damage:
            electricity = python_json_obj["electricity"]
            Electricitychance = (electricity/FullDamage)*100
            print("Electricitychance: "+str(Electricitychance))
        if "toxin" in Damage:
            toxin = python_json_obj["toxin"]
            Toxinchance = (toxin/FullDamage)*100
            print("Toxinchance: "+str(Toxinchance))
        if "magnetic" in Damage:
            magnetic = python_json_obj["magnetic"]
            Magneticchance = (magnetic/FullDamage)*100
            print("Magneticchance: "+str(Magneticchance))
        if "radiation" in Damage:
            radiation = python_json_obj["radiation"]
            Radiationchance = (radiation/FullDamage)*100
            print("Radiationchance: "+str(Radiationchance))
        Statustype = Statustypefinden(Impactchance,Slashchance,Puncturechance,Electricitychance,Toxinchance,Magneticchance,Radiationchance)
        while Statustype == "nothing":
            Statustype = Statustypefinden(Impactchance,Slashchance,Puncturechance,Electricitychance,Toxinchance,Magneticchance,Radiationchance)
        print(Statustype)
        return(Statustype)
    except:
        print("Fehler in Status_taken")
def Statusanwenden(TypedesStatus,Damagepersecond,Damage):
    Statusdamage = 0
    print("Derzeitiger Statustype: "+TypedesStatus)
    if TypedesStatus == "Electricity":
       Statusdamage = Damagepersecond
    if TypedesStatus == "Slash":
       Statusdamage = Damagepersecond *2
    return(Statusdamage)
def Statustype(Damagejson,Weapon,Damage):
    Damagepersecond =Damage
    Damage = Damagejson
    FullDamage = get_FullDamage(Damage)
    TypedesStatus=Status_taken(FullDamage, Damage)
    print("Damage vor Status: "+str(Damagepersecond))
    Damagepersecond = Statusanwenden(TypedesStatus,Damagepersecond,Damage)
    print("Damage nach Status: "+str(Damagepersecond))
    print("Statustyp: "+str(TypedesStatus))
    print("FullDamage: "+str(FullDamage))
    return(Damagepersecond) 

    
def Status(Weapon,Damage,Statuschance, Damagejson):
    if random.randint(0,100) < Statuschance:
        print("Statuseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        Damage =Statustype(Damagejson,Weapon,Damage)
    return(Damage)
    
def Crit(CritChance,damagePerSecond,criticalMultiplier):
    if random.randint(0,100) < CritChance:
        print("Sie haben einen kritischen Treffer gelandet")
        damagePerSecond = damagePerSecond* criticalMultiplier
    return(damagePerSecond)


def Attack(Waffe,LVL,Damage):
    Sekunden = 0
    damagePerSecond = get_Damage_per_second(Waffe)
    Health = effectiveHealth(LVL)
    FullHealth = Health
    Statuschance = get_Status_Chance(Waffe)
    CritChance = get_crit_chance(Waffe)
    criticalMultiplier = get_crit_multi(Waffe)
    while Health > 0:
        Damagedone = damagePerSecond
        Damagedone = Crit(CritChance,damagePerSecond,criticalMultiplier)
        Damagedone = Status(Waffe, Damagedone, Statuschance, Damage)
        Health = Health- Damagedone
        print("Sie haben "+str(Damagedone)+" Schaden angerichtet")
        Sekunden = Sekunden + 1
        
        
        print(str(Health))
    print("Ihre Waffe hat eine Statuschance von "+str(Statuschance)+" Prozent")
    print("Ihre Waffe hat eine Critchance von "+str(CritChance)+" Prozent")
    print("Ihre Waffe hat einen Crit Multiplier von "+str(criticalMultiplier))
    print("Ihr Gegner hatte "+str(FullHealth)+" Leben ") 
    print("Sie haben "+str(Sekunden)+" Sekunden gebraucht")
    
    
def Damage_Simulator(Eingabe):
    Gegner = "Corrupted Heavy Gunner"
    EingabeWaffe = Eingabezerlegung.Waffe(Eingabe)
    URL = "https://api.warframestat.us/weapons/"
    EingabeWaffe = URL+EingabeWaffe
    EingabeWaffe = EingabeWaffe.replace("/ ", "/")
    EingabeWaffe = EingabeWaffe.replace("https://api.warframestat.us/weapons/", "")
    EingabeWaffe = EingabeWaffe.replace(" ", "")
    print (EingabeWaffe)
    EingabeLVL = Eingabezerlegung.LVL(Eingabe)
    print (str(EingabeLVL))
    Damage = getDamage(EingabeWaffe)
    print("Ihre gewählte Waffe: "+EingabeWaffe)
    print("Ihr gewähltes LVL: "+str(EingabeLVL))
    print("Der ausgewählte Gegner: "+Gegner)
    Attack(EingabeWaffe,EingabeLVL,Damage)
    
    
def Damage(Suche): 
    Eingabe = Suche.replace("!Damage ", "")
    Eingabe = Damage_Simulator(Eingabe)
            

Damage("Galatine 50")