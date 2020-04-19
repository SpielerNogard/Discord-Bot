import random
from random import *
import mysql.connector
import requests
import json
import discord

def Waffe(Eingabe):
    Eingabe = Eingabe.replace("0", "")
    Eingabe = Eingabe.replace("1", "")
    Eingabe = Eingabe.replace("2", "")
    Eingabe = Eingabe.replace("3", "")
    Eingabe = Eingabe.replace("4", "")
    Eingabe = Eingabe.replace("5", "")
    Eingabe = Eingabe.replace("6", "")
    Eingabe = Eingabe.replace("7", "")
    Eingabe = Eingabe.replace("8", "")
    Eingabe = Eingabe.replace("9", "")
    return(Eingabe)
def LVL(Eingabe):
    Eingabe = Eingabe.upper()
    Eingabe = Eingabe.replace("A", "")
    Eingabe = Eingabe.replace("B", "")
    Eingabe = Eingabe.replace("C", "")
    Eingabe = Eingabe.replace("D", "")
    Eingabe = Eingabe.replace("E", "")
    Eingabe = Eingabe.replace("F", "")
    Eingabe = Eingabe.replace("G", "")
    Eingabe = Eingabe.replace("H", "")
    Eingabe = Eingabe.replace("I", "")
    Eingabe = Eingabe.replace("J", "")
    Eingabe = Eingabe.replace("K", "")
    Eingabe = Eingabe.replace("L", "")
    Eingabe = Eingabe.replace("M", "")
    Eingabe = Eingabe.replace("N", "")
    Eingabe = Eingabe.replace("O", "")
    Eingabe = Eingabe.replace("P", "")
    Eingabe = Eingabe.replace("Q", "")
    Eingabe = Eingabe.replace("R", "")
    Eingabe = Eingabe.replace("S", "")
    Eingabe = Eingabe.replace("T", "")
    Eingabe = Eingabe.replace("U", "")
    Eingabe = Eingabe.replace("V", "")
    Eingabe = Eingabe.replace("W", "")
    Eingabe = Eingabe.replace("X", "")
    Eingabe = Eingabe.replace("Y", "")
    Eingabe = Eingabe.replace("Z", "")
    Eingabe = Eingabe.replace(" ", "")
    return(Eingabe)