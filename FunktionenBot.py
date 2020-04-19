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

def randomizer(Start,Ende):
    Zahl=randint(Start, Ende)
    return Zahl

def counter(Table):
    sql = "SELECT MAX(id) AS maximum FROM "+Table
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
    return id
def counterUser(Table,User):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="warframe"
    )
    mycursor = mydb.cursor()
    id = "" 
    sql = "SELECT COUNT(*) FROM "+Table+" WHERE User = '"+str(User)+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]

    return id     
def selectWarframe(id):
    sql = "SELECT * FROM warframes WHERE id = "+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        Warframe =x[1]
        Link = x[2]
        Out = Warframe
    return Out
def selectprimary(id):
    sql = "SELECT * FROM primär WHERE id = "+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        Warframe =x[1]
        Link = x[2]
        Out = Warframe
    return Out
def selectsecondary(id):
    sql = "SELECT * FROM sekundär WHERE id = "+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        Warframe =x[1]
        Link = x[2]
        Out = Warframe
    return Out
def WeaponStats(Weapon):
    try:
        url='https://api.warframestat.us/weapons/'+Weapon
        with requests.get(url) as response:
            Out34 = 0
            python_json_obj = response.text
            python_json_obj = json.loads(python_json_obj)
            Out = python_json_obj["name"]
            Out1 = python_json_obj["damagePerShot"]
            Out2 = python_json_obj["magazineSize"]
            Out3 = python_json_obj["reloadTime"]
            Out4 = python_json_obj["totalDamage"]
            Out5 = python_json_obj["damagePerSecond"]
            Out6 = python_json_obj["trigger"]
            Out7 = python_json_obj["description"]
            Out8 = python_json_obj["accuracy"]
            Out9 = python_json_obj["criticalChance"]
            Out10 = python_json_obj["criticalMultiplier"]
            Out11 = python_json_obj["procChance"]
            Out12 = python_json_obj["fireRate"]
            Out13 = python_json_obj["chargeAttack"]
            Out14 = python_json_obj["spinAttack"]
            Out15 = python_json_obj["leapAttack"]
            Out16 = python_json_obj["wallAttack"]
            Out17 = python_json_obj["slot"]
            Out18 = python_json_obj["noise"]
            Out19 = python_json_obj["sentinel"]
            Out20 = python_json_obj["masteryReq"]
            Out21 = python_json_obj["productCategory"]
            Out22 = python_json_obj["channelingDamageMultiplier"]
            Out23 = python_json_obj["buildPrice"]
            Out24 = python_json_obj["buildTime"]
            Out25 = python_json_obj["skipBuildTimePrice"]
            Out26 = python_json_obj["buildQuantity"]
            Out27 = python_json_obj["consumeOnBuild"]
            Out28 = python_json_obj["components"]
            Out29 = python_json_obj["tradable"]
            Out30 = python_json_obj["category"]
            Out31 = python_json_obj["ammo"]
            Out32 = python_json_obj["damage"]
            Out33 = python_json_obj["damageTypes"]
            #Out34 = python_json_obj["marketCost"]
            #Out35 = python_json_obj["polarities"]
            Out36 = python_json_obj["wikiaThumbnail"]
            Out37 = python_json_obj["wikiaUrl"]
            Out38 = python_json_obj["disposition"]
            
            embed=discord.Embed(title=str(Out), description="Deine Ergebnisse: ", color=0xff0000)
            embed.set_thumbnail(url=Out36)
            embed.add_field(name="Beschreibung", value=str(Out7), inline=False)
            embed.add_field(name="MagazinGröße", value=str(Out2), inline=True)
            embed.add_field(name="Nachladezeit", value=str(Out3), inline=True)
            embed.add_field(name="Crit Chance", value=str(Out9), inline=True)
            embed.add_field(name="Crit Multiplier", value=str(Out10), inline=True)
            embed.add_field(name="Damage", value=str(Out32), inline=True)
            embed.add_field(name="Damage Verteilung", value=str(Out33), inline=True)
            embed.add_field(name="Firerate", value=str(Out12), inline=True)
            embed.add_field(name="Benötigter Mastery Rank", value=str(Out20), inline=True)
            embed.add_field(name="Riven Dispo", value=str(Out38), inline=True)
            embed.add_field(name="Lautstärke", value=str(Out18), inline=True)
            embed.add_field(name="Category", value=str(Out30), inline=True)
            embed.add_field(name="mehr Informationen", value=str(Out37), inline=True)
    except:
        Out = "Error while searching for WorldStatus Cetus"
    print(str(Out))
    print(str(Out1))
    print(str(Out2))
    print(str(Out3))
    print(str(Out4))
    print(str(Out5))
    print(str(Out6))
    print(str(Out7))
    print(str(Out8))
    print(str(Out9))
    print(str(Out10))
    print(str(Out11))
    print(str(Out12))
    print(str(Out13))
    print(str(Out14))
    print(str(Out15))
    print(str(Out16))
    print(str(Out17))
    print(str(Out18))
    print(str(Out19))
    print(str(Out20))
    print(str(Out21))
    print(str(Out22))
    print(str(Out23))
    print(str(Out24))
    print(str(Out25))
    print(str(Out26))
    print(str(Out27))
    #print(str(Out28))
    print(str(Out29))
    print(str(Out30))
    print(str(Out31))
    print(str(Out32))
    print(str(Out33))
    #print(str(Out34))
    #print(str(Out35))
    print(str(Out36))
    print(str(Out37))
    print(str(Out38))
    return(embed)
    
    
    
    
def selectWarframelink(id):
    sql = "SELECT * FROM warframes WHERE id = "+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        Warframe =x[1]
        Link = x[2]
        Out = Link
    return Out
def selectprimarylink(id):
    sql = "SELECT * FROM primär WHERE id = "+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        Warframe =x[1]
        Link = x[2]
        Out = Link
    return Out
def selectsecondarylink(id):
    sql = "SELECT * FROM sekundär WHERE id = "+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        id = x[0]
        Warframe =x[1]
        Link = x[2]
        Out = Link
    return Out
def getWorldstateCetus():
    try:
        url='https://api.warframestat.us/pc/cetusCycle/'
        with requests.get(url) as response:
            python_json_obj = response.text
            python_json_obj = json.loads(python_json_obj)
            Out = python_json_obj["shortString"]
    except:
        Out = "Error while searching for WorldStatus Cetus"
    return Out
def getArbitartionData():
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
    except:
        Arbitration = "Error while checking Arbitration Status"
    return Arbitration 
def getData(Item):
    url='https://api.warframestat.us/drops/search/'+Item
    response = requests.get(url, stream=True)
    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["place"]
            Out2 = python_json_obj["item"]
            Out3 = python_json_obj["rarity"]
            Out4 = python_json_obj["chance"]
            print("Ort: "+Out1)
            print("Item: "+Out2)
            print("Seltenheit: "+Out3)
            print("Chance: "+str(Out4))
            if not Item in Out1:
              
                print('Done')
                print("Ort: "+Out1)
                print("Item: "+Out2)
                print("Seltenheit: "+Out3)
                print("Chance: "+str(Out4))
        except:
            info="Fehler"
            print(info)
def cleanspot():
    sql = "Insert into arbeiter(chance) values ('1')"
    mycursor.execute(sql)
    mydb.commit()
    print("bestspotcleaned")
def insertbestspot(dropchance, Ort, Item, Seltenheit, zahl):
    try:
        
       
        sql = "SELECT * FROM bestspot WHERE id ="+str(zahl)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for x in result:
            id = x[0]
            Place =x[1]
            item = x[2]
            rarity= x[3]
            chance=x[4]
            if float(dropchance)>float(chance):
                print(Place)
                print(item)
                print(rarity)
                print(chance)
                sql1 = "UPDATE bestspot SET Place = '"+Ort+"' WHERE id="+str(zahl)
                sql2 = "UPDATE bestspot SET item = '"+Item+"' WHERE id="+str(zahl)
                sql3 = "UPDATE bestspot SET rarity = '"+Seltenheit+"' WHERE id="+str(zahl)
                sql4 = "UPDATE bestspot SET chance = '"+str(dropchance)+"' WHERE id="+str(zahl)
                mycursor.execute(sql1)
                mydb.commit()
                print('Ort updated')
                mycursor.execute(sql2)
                mydb.commit()
                print('Item updated')
                mycursor.execute(sql3)
                mydb.commit()
                print('Seltenheit updated')
                mycursor.execute(sql4)
                mydb.commit()
                print('Chance updated')
                print(Ort)
                print(Item)
                print(Seltenheit)
                print(str(dropchance))
            if float(dropchance)<float(chance):
                print("Schlechtere Chance")
            if float(dropchance)==float(chance):
                sql = "Insert into bestspot(Place, item, rarity, chance) values ('"+Ort+"','"+Item+"','"+Seltenheit+"','"+str(dropchance)+"')"
                mycursor.execute(sql)
                mydb.commit()
                print("insertedd")
               
    except:
        print("Fehler beim select")
                    
def foundbestSpot(Item):
    Ausgabe = ""
    url='https://api.warframestat.us/drops/search/'+Item
    cleanspot()
    zahl = counter('bestspot')
    print(str(zahl))
    response = requests.get(url, stream=True)
    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["place"]
            Out2 = python_json_obj["item"]
            Out3 = python_json_obj["rarity"]
            Out4 = python_json_obj["chance"]
            if not Item in Out1:
                #print("Ort: "+Out1)
                #print("Item: "+Out2)
                #print("Seltenheit: "+Out3)
                #print("Chance: "+str(Out4))
                insertbestspot(Out4, Out1, Out2, Out3, zahl)
        except:
            info="Fehler"
            print(info)
    mycursor.execute("SELECT * FROM bestspot where id ="+str(zahl))
    myresult = mycursor.fetchall()
    embed=discord.Embed(title="Itemsuche", description="Deine Ergebnisse: ", color=0xff0000)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/7/7f/ResourceButtonHover.png/revision/latest?cb=20140830065141")

    for x in myresult:
       chanceintable=x[4] 
    mycursor.execute("SELECT * FROM bestspot")
    myresult = mycursor.fetchall()
    for x in myresult:
         id = x[0]
         Place =x[1]
         item = x[2]
         rarity= x[3]
         chance=x[4]
         if float(chance) == float(chanceintable):
            embed.add_field(name="Ort", value=Place, inline=False)
            embed.add_field(name="Item", value=item, inline=False)
            embed.add_field(name="Rarity", value=rarity, inline=True)
            embed.add_field(name="Chance", value=chance, inline=True)
            embed.add_field(name="Ergebnis", value="Nächstes Ergebnis:", inline=False)          
    return(embed)       
            
def getTrader():
    Ausgabe = ""
    url='https://api.warframestat.us/PC/voidTrader'
    response = requests.get(url, stream=True)
    embed=discord.Embed(title="Baroo Ki'Teer", description="Der aktuelle Void Trader ")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/919694298295046144/zMEbYUWP_400x400.jpg")

    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["item"]
            Out2 = python_json_obj["ducats"]
            Out3 = python_json_obj["credits"]
            Out5 = python_json_obj["startString"]
            print(Out5)
            Ausgabe = Out1
            embed.add_field(name="Item", value=Out1, inline=False)
            embed.add_field(name="Ducats", value=str(Out2), inline=True)
            embed.add_field(name="Credits", value=str(Out3), inline=True)     
        except:
            info="Fehler"
            print(info)
    if Ausgabe == "":
        embed.add_field(name="Not Active", value="Der Trader ist gerade nicht aktiv", inline=False)
    if Ausgabe != "":
        embed.add_field(name="Time left:", value=Out5, inline=True)
    return(embed)
def getArcanes(Search):
    Ausgabe=""
    url='https://api.warframestat.us/arcanes/search/'+Search
    embed=discord.Embed(title="Arcane ", description="Ihre Suche ergab folgende Ergebnisse ", color=0x0080ff)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/4/46/VirtuosStrike.png/revision/latest/scale-to-width-down/350?cb=20171129163040")
    response = requests.get(url, stream=True)
    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["name"]
            Out2 = python_json_obj["effect"]
            Out3 = python_json_obj["rarity"]
            Out4 = python_json_obj["location"]
            Out5 = python_json_obj["thumbnail"]
            Out6 = python_json_obj["info"]
            print("Item: "+Out1)
            print("Effect: "+str(Out2))
            print("Rarity: "+str(Out3))
            print("Location: "+str(Out4))
            print("Picture: "+str(Out5))
            print("More Informations: "+str(Out6))
            embed.add_field(name="Item", value=Out1, inline=False)
            embed.add_field(name="Effect", value=str(Out2), inline=False)
            embed.add_field(name="Rarity", value=str(Out3), inline=True)
            embed.add_field(name="Location", value=str(Out4), inline=True)
            embed.add_field(name="More Information", value=str(Out6), inline=False)
            a= "Item: "+Out1+" Effect: "+str(Out2)+" ,Rarity: "+str(Out3)+" ,Location: "+str(Out4)+" ,Picture: "+str(Out5)+" ,More Informations: "+str(Out6)+"\n"+"\n"
            Ausgabe= Ausgabe+a 
        except:
            info="Fehler"
            print(info)
    return(embed)
def getDailyDeals():
    Ausgabe=""
    url='https://api.warframestat.us/PC/dailyDeals'
    response = requests.get(url, stream=True)
    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["item"]
            Out2 = python_json_obj["originalPrice"]
            Out3 = python_json_obj["salePrice"]
            Out4 = python_json_obj["total"]
            Out5 = python_json_obj["sold"]
            Out6 = python_json_obj["eta"]
            print("Item: "+Out1)
            print("OriginalPrice: "+str(Out2))
            print("SalePrice: "+str(Out3))
            print("Total Number of Items: "+str(Out4))
            print("Sold: "+str(Out5))
            print("Time left: "+str(Out6))
            a= "Item: "+Out1+" OriginalPrice: "+str(Out2)+" ,SalePrice: "+str(Out3)+" ,Total Number of Items: "+str(Out4)+" ,Sold: "+str(Out5)+" ,Time left: "+str(Out6)+"\n"+"\n"
            Ausgabe= Ausgabe+a  
            embed=discord.Embed(title="Darvos Deal", description="Darvos actual Deal")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/7/7d/DarvoCodex.png/revision/latest?cb=20150518154630")
            embed.add_field(name="Item", value=Out1, inline=False)
            embed.add_field(name="Original Price", value=str(Out2), inline=True)
            embed.add_field(name="Actual Price", value=str(Out3), inline=True)
            embed.add_field(name="Total Number of Items", value=str(Out4), inline=True)
            embed.add_field(name="Sold Items", value=str(Out5), inline=True)
            embed.add_field(name="Time left", value=str(Out6), inline=False)            
        except:
            info="Fehler"
            print(info)
    return(embed)
def getfissures():
    url='https://api.warframestat.us/PC/fissures'
    response = requests.get(url, stream=True)
    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["node"]
            Out2 = python_json_obj["missionType"]
            Out3 = python_json_obj["enemy"]
            Out5 = python_json_obj["tier"]
            Out4 = python_json_obj["eta"]
            Out = Out5+": "+Out2+" ("+Out3+") "+Out1+" Time left: "+Out4
            print(Out)          
        except:
            info="Fehler"
            print(info)
def getNews():
    url='https://api.warframestat.us/PC/news'
    response = requests.get(url, stream=True)
    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["message"]
            Out2 = python_json_obj["link"]
            Out3 = python_json_obj["eta"]
            Out5 = python_json_obj["asString"]
            
            print(Out5)          
        except:
            info="Fehler"
            print(info)  
def getRivens(Search):
    url='https://api.warframestat.us/PC/rivens/search/'+Search
    response = requests.get(url, stream=True)
    for line in response.iter_lines(decode_unicode=True, delimiter="}"):
        try:
            info=line.split("{")[1]
            info2="{"+info+"}"
            python_json_obj = json.loads(info2)
            Out1 = python_json_obj["itemType"]
            Out2 = python_json_obj["compatibility"]
            Out3 = python_json_obj["rerolled"]
            Out5 = python_json_obj["avg"]
            Out4 = python_json_obj["stddev"]
            Out6 = python_json_obj["min"]
            Out7 = python_json_obj["max"]
            Out8 = python_json_obj["pop"]
            Out9 = python_json_obj["median"]
            Out = "Dein gesuchter Riven: "+"\n"+"Riven Art: "+Out1+"\n"+"Waffe: "+Out2+"\n"+"gerollt?: "+str(Out3)+"\n"+"Lowest Price: "+str(Out6)+"\n"+"Highest Price: "+str(Out7)
            print(Out)          
        except:
            info="Fehler"
            print(info) 
def getOutpost():
    url='https://api.warframestat.us/PC/sentientOutposts'
    try:
        with requests.get(url) as response:
            python_json_obj = response.text
            python_json_obj = json.loads(python_json_obj)
            Out = python_json_obj["mission"]
            Out1 = python_json_obj["active"]
            Ausgabe = "Sentient Outpost Active : "+str(Out1)+"\n"+"Mission: "+str(Out)
            
            print(Ausgabe)          
    except:
        info="Fehler"
        print(info)

def nomessages(Message):
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="warframe"
        )
        mycursor = mydb.cursor()
        User = Message.author
        sql = "Insert into nomessages(User) values ('"+str(User)+"')"
        mycursor.execute(sql)
        mydb.commit()   
    except:
        print("Fehler in nomessages")
def UserMessages(Message):
    try:
        User = Message.author
        Table = "nomessages"
        Uservorhanden = counterUser(Table,User)
        print(str(Uservorhanden))
    except:
        print("Fehler in UserMessages")
dropchance= 2.2
Ort = "b"
Item= "C" 
Seltenheit = "3"       
#id = counter('warframes')
#Zahl = randomizer(1,id)
#Out = selectWarframe(Zahl)
#Status = getWorldstateCetus()
#Arbitration = getArbitartionData()
#getData('Lith C4')
#foundbestSpot('Lith C4')
#cleanspot()
#insertbestspot(dropchance, Ort, Item, Seltenheit)
#getTrader()
#getArcanes('Strike')
#getDailyDeals()
#getfissures()
#getNews()
#getOutpost()
#getRivens('Amprex')
#print (Zahl)
#print (Out)
#print (Status)
#print (Arbitration)