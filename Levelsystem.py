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

def new_User(User):
    #Creates a new User for leveling
    sql = "Insert into lvl(User,LVL,Messages,Xp) values ('"+str(User)+"','1','0','0')"
    mycursor.execute(sql)
    mydb.commit()
    print("New User Created")
def new_Message(User):
#User has sent a Message, now he can get XP
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="warframe"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM lvl WHERE User ='"+str(User)+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        User =x[1]
        LVL = x[2]
        Messages= x[3]
        Xp=x[4]
        #print (id)
        #print ( User) 
        #print(LVL)
        #print (Messages)
        #print ( Xp)
        new_XP = int(Xp) + 1
        new_Messages = int(Messages) + 1
        #print(str(new_XP))
        #print(str(new_Messages))
        sql = "UPDATE lvl SET Messages = '"+str(new_Messages)+"' WHERE id='"+str(id)+"'"
        mycursor.execute(sql)
        mydb.commit()
        #print('Messages updated')
        sql = "UPDATE lvl SET Xp = '"+str(new_XP)+"' WHERE id='"+str(id)+"'"
        mycursor.execute(sql)
        mydb.commit()
        #print('XP updated')
    #print("User hat Xp erhalten")
def lvl_Up(User):
#User has enough XP now ist Time for LVL UP
    embed = ""
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="warframe"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM lvl WHERE User ='"+str(User)+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        User =x[1]
        LVL = x[2]
        Messages= x[3]
        Xp=x[4]
        new_LVL = int(LVL) + 1
        Nachricht= "@"+User+" you have reached LVL: "+str(new_LVL)
    if int(Xp) >= (int(LVL)*int(LVL)):
        sql = "UPDATE lvl SET LVL = '"+str(new_LVL)+"' WHERE id='"+str(id)+"'"
        mycursor.execute(sql)
        mydb.commit()
        sql = "UPDATE lvl SET Xp = '0' WHERE id='"+str(id)+"'"
        mycursor.execute(sql)
        mydb.commit()
        #print('LVL UP')
        embed=discord.Embed(title="LVL UP !!", description="You have reached a new Level", color=0xf82c07)
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSQlczAUQ8uhObAaQsuz2KKP3iEGRnoGzi6f9fZQkI2F1Apu45Y")
        embed.add_field(name=User, value=Nachricht, inline=False)
    return(embed) 
    #print("User wurde gelevelt")