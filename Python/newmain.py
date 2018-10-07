import os
import random
import time

import tkinter as tk

##arrays
vip = ["Cameron", "Ancient", "Aleyna", "Jonas", "161616"]

##read text files
#bot names
bnimport = open("./Text Files/botnames.txt")
botnames = bnimport.read().split(',')
bnimport.close()

#good feelings
gfimport = open("./Text Files/Feelings/goodfeelings.txt", "r")
goodfeelings = gfimport.read()
gfimport.close()

#bad feelings
bfimport = open("./Text Files/Feelings/goodfeelings.txt", "r")
badfeelings = bfimport.read()
bfimport.close()

#neutral feelings
nfimport = open("./Text Files/Feelings/goodfeelings.txt", "r")
neutralfeelings = nfimport.read()
nfimport.close()

#roberto relationship status
rrs = open("./Text Files/Bot Relationships/robertorelationships.txt","r")
robertorelationship = rrs.read().split(',')
rrs.close()

#currentbot relationship status
crs = open("./Text Files/Bot Relationships/currentbotrelationships.txt")
currentbotrelationship = crs.read().split(',')
crs.close()

##global variables
name = "User"
vipstatus = False
cnp = random.choice(botnames)
cn = cnp + ":"
def clear(): 
    return os.system('cls')

def checkVIP(name):
    global vipstatus

    if name in vip:
        vipstatus = True

    return

def giveVIPBot(name):
    global cn
    global cnp

    if name == "Ancient":
        cnp = "Roberto"
        cn = cnp + ":"       
    elif name == "Cameron":
        cnp = "Hank"
        cn = cnp + ":"
    elif name == "Jonas":
        cnp = "Terrence"
        cn = cnp + ":"

    return

##get the name of the user
def getName():
    global name
    global cnp
    global cn

    while name == "User":
        print("Computer: Hello there", name,"! What is your name?")

        name = str(input("User: "))
        checkVIP(name)
        giveVIPBot(name)
        print("\nComputer: The bot you are talking to is",cnp)

        if vipstatus == True:
            print(cn,"Welcome back, VIP user", name, "\n")
            
        elif vipstatus == False:
            print(cn,"Hello,", name, "\n")

    mainMenu()

##main menu
def mainMenu():
    print("Option A | Greet \nOption B | Change user \nOption C | Chat \nOption D | Trivia \nOption E | Story \nOption F | Relationship status")

    valid = 0
    while (valid == 0):
        option = str(input("\nComputer: Please select an option: ").lower())

        if option == "a":
            valid = 1
            #greet()
        elif option == "b":
            valid = 1
            #changeUser()
        elif option == "c":
            valid = 1
            chat()
        elif option == "d":
            valid = 1
            #trivia()
        elif option == "e":
            valid = 1
            #story()
        elif option == "f": #and bestfriends == 1:
            valid = 1
            relationshipStatus()
        elif option == "g": #and bestfriends == 1:
            valid = 1
            #jokes()
        elif option == "h": #and bestfriends == 1 and name == "Ancient":
            valid = 1
            #flirting()
        elif option == "i":
            valid = 1
            #clearmemory()
        elif option == "x":
            clear()
            os._exit(1)
        else:
            # if the input is not correct, display an error then go back to the beginning
            print("System: Error, please try again \n")
            valid = 0

##end the current sub program
def endSubProgram(emotion):
    if emotion == "sad":
        print(cn, "(T_T)")
    elif emotion == "happy":
        print(cn, "( ^w^)")
    elif emotion == "neutral":
        print(cn, "(o-o)")
    
    print(cn, "Would you like to return to the main menu",name,"?")
    
    returnoption = str(input("User: ").lower())

    if returnoption == "y":
        clear()
        mainMenu()

    elif returnoption == "n":
        print(cn, "Goodbye",name,"!")
        time.sleep(1)
        clear()
        os._exit(1)

##show the relationship status between the user and the bot
def relationshipStatus():
    print("\nComputer: Which bot would you like to see relationship status with? \nOption A | Current bot \nOption B | Roberto")
    rsoption = str(input("User: ").lower())

    if rsoption == "a":
        matching = [s for s in currentbotrelationship if name in s]

        botoption = cnp
    elif rsoption == "b":
        matching = [s for s in robertorelationship if name in s]

        if cnp == "Roberto":
            botoption = cnp
        else:
            botoption = "Roberto"
        
    splitmatching = [i.split('-', 1)[1] for i in matching]
  
    if splitmatching == []:
        print("\nComputer: You have no relationship with", botoption,",", name,". \n")
        
        endSubProgram("neutral")
    elif splitmatching != "":
        print("\nComputer: The relationship between",name,"and",botoption,"is", "".join(splitmatching), ". \n")

        endSubProgram("neutral")

def chat():
    print(cn, "Hey", name, "! Tell me what is on your mind!")
    chatstart = str(input("User: ").lower())

##main menu call
getName()