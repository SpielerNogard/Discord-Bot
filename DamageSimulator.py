import random
from random import *
import mysql.connector
import requests
import json
import discord
import Eingabezerlegung
import WaffenDaten

def Damage_Simulator(Eingabe):
    EingabeWaffe = Eingabezerlegung.Waffe(Eingabe)
    URL = "https://api.warframestat.us/weapons/"
    EingabeWaffe = URL+EingabeWaffe
    EingabeWaffe = EingabeWaffe.replace("/ ", "/")
    EingabeWaffe = EingabeWaffe.replace("https://api.warframestat.us/weapons/", "")
    print (EingabeWaffe)
    EingabeLVL = Eingabezerlegung.LVL(Eingabe)
    print (str(EingabeLVL))
    Damage = WaffenDaten.getDamage(EingabeWaffe)
    print(str(Damage))