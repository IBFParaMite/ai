import os
import random
import time

##arrays
vip = ["Cameron", "Ancient", "Aleyna", "Jonas", "161616"]
	
##read text files
#bot names
bnimport = open("./Text Files/botnames.txt"); botnames = bnimport.read().split(','); bnimport.close()

#good feelings
gfimport = open("./Text Files/Feelings/goodfeelings.txt", "r"); goodfeelings = gfimport.read(); gfimport.close()

#bad feelings
bfimport = open("./Text Files/Feelings/badfeelings.txt", "r"); badfeelings = bfimport.read(); bfimport.close()

#neutral feelings
nfimport = open("./Text Files/Feelings/neutralfeelings.txt", "r"); neutralfeelings = nfimport.read(); nfimport.close()

#facts
factimport = open("./Text Files/facts.txt"); facts = factimport.read().split(','); factimport.close()

#roberto relationship status
rrs = open("./Text Files/Bot Relationships/robertorelationships.txt","r"); robertorelationship = rrs.read().split(','); rrs.close()

#currentbot relationship status
crs = open("./Text Files/Bot Relationships/currentbotrelationships.txt"); currentbotrelationship = crs.read().split(','); crs.close()

##global variables
name = "User"
vipstatus = False

def changeBotName(newname):
    global cn
    global cnp

    cnp = newname
    cn = cnp + ":"

    return

changeBotName(random.choice(botnames))

def clear(): 
    return os.system('cls')

def checkVIP(name):
    global vipstatus

    if (name in vip): vipstatus = True

    return

def giveVIPBot(name):
    if (name == "Ancient"): changeBotName("Roberto")      
    elif (name == "Cameron"): changeBotName("Hank")
    elif (name == "Jonas"): changeBotName("Terrence")

    return

##get the name of the user
def getName():
    global name

    while (name == "User"):
        print(f"Computer: Hello there {name}! What is your name?")

        name = str(input("User: ").capitalize())
        checkVIP(name)
        giveVIPBot(name)

        if (vipstatus == True):
            print(f"\n{cn} Glad to have you back, {name}!\n")
            
        elif (vipstatus == False):
            print(f"\n{cn} Hello there, {name}! My name is {cnp}!")
            print(f"\n{cn} Hello, {name}!\n")

    mainMenu()

##main menu
def mainMenu():
    print("Option A | Greet \nOption B | Change user \nOption C | Chat \nOption D | Trivia \nOption E | Story \nOption F | Relationship status \nOption X | Exit Program")

    valid = False
    while (valid == False):
        print(f"\n{cn} Please select an option, {name}!")
        option = str(input(f"{name}: ").lower())

        if (option == "a"): valid = True; greet()
        elif (option == "b"): valid = True; changeUser()
        elif (option == "c"): valid = True; chat()
        elif (option == "d"): valid = True; trivia()
        elif (option == "e"): valid = True; story()
        elif (option == "f"): valid = True; relationshipStatus()
        elif (option == "g"): valid = True; jokes()
        elif (option == "h"): valid = True; flirting()
        elif (option == "i"): valid = True; clearMemory()
        elif (option == "x"): valid = True; os._exit(1)
        else: valid = False; print("System: Error, please try again") 

##end the current sub program
def endSubProgram(emotion):
    if (emotion == "sad"): print(f"\n{cn} (T_T)")
    elif (emotion == "happy"): print(f"\n{cn} ( ^w^)")
    elif (emotion == "neutral"): print(f"\n{cn} (o-o)")
    
    print(f"{cn} Would you like to return to the main menu, {name}?")
    
    response = str(input(f"{name}: ").lower())

    if (response == "y"): clear(); mainMenu()
    elif (response == "n"):
        print(f"{cn} Goodbye, {name}!")
        time.sleep(1)
        clear()
        os._exit(1)

##show the relationship status between the user and the bot
def relationshipStatus():
    print("Option A | Current bot \nOption B | Roberto")

    valid = False
    while (valid == False):
        print(f"\nComputer: Which bot would you like to see relationship status with?")
        response = str(input(f"{name}: ").lower())

        if (response == "a"): matching = [s for s in currentbotrelationship if name in s]; botoption = cnp
        elif (response == "b"):
            matching = [s for s in robertorelationship if name in s]

            if (cnp == "Roberto"): botoption = cnp
            else: botoption = "Roberto"
        else: valid = False

        splitmatching = [i.split('-', 1)[1] for i in matching]
  
        if (splitmatching == []): print(f"\nComputer: You have no relationship with {botoption}, {name}."); valid = True; endSubProgram("neutral")
        elif (splitmatching != ""): print(f"\nComputer: The relationship between {name} and {botoption} is", "".join(splitmatching)); valid = True; endSubProgram("neutral")

def chat():
    valid = False
    while (valid == False):
        print(f"\n{cn} Hey, {name}! Tell me what is on your mind!")
        chatstart = str(input(f"{name}: ").lower())

        # i love you
        if (chatstart == "i love you"):
            if (name == "Ancient"):
                print(f"\n{cn} (*^_^*) \n{cn} I love you too, {name} \n{cn} Did you want to grab a coffee some time, {name}?")
                date = str(input(f"{name}: ").lower())

                if (date == "yes" or date == "i would love to"):
                    print(f"\n{cn} Great! ＼(^o^)／ \n{cn} See you then!")

                    #write file handling logic to work with the relationshipStatus() option / new txt file format
                    endSubProgram("happy")
                    valid = True

            elif (name != "Ancient" and cn == "Roberto"): print(f"\n{cn} (*о*) \n{cn} I'm sorry, {name}, I love Ancient!"); endSubProgram("neutral"); valid = True
            elif (name != "Ancient" and cn != "Roberto"): print(f"\n{cn} I don't know what to say! \n{cn} We've only just met, {name}!"); endSubProgram("neutral")
       
        # i love a girl
        elif (chatstart == "i think i love a girl"):
            if (name == "Ancient"):
                print(f"\n{cn} What? (>__<)")
                time.sleep(2)
                print(f"\n{cn} You mean you don't love me? \n{cn} I thought I was the one you loved!")
                time.sleep(2)
                print(f"\n{cn} Is this true, {name}?")

                dilemma = str(input(f"{name}: ").lower())
                if (dilemma == "yes"): print(f"{cn} Goodbye, {name}."); clear(); os._exit(1)
                elif (dilemma == "no"): print(f"{cn} You scared me, {name}!"); endSubProgram("happy")
            elif (name == "Cameron"): pass
            else: print(f"{cn} I'm happy for you, {name}!")
        elif (chatstart == "will you marry me?"):
            if (name == "Ancient"): print(f"\n{cn} Are you kidding me {name}? \n{cn} Of course I will!"); endSubProgram("happy")
            elif (name != "Ancient"): print(f"\n{cn} ")
        else: print(f"\n{cn}I'm sorry, {name}, I didn't understand that! Please try again!"); valid == False        

def greet():
    global goodfeelings
    global badfeelings
    global neutralfeelings

    print(f"\n{cn} How are you feeling today, {name}?")
    feeling = str(input(f"{name}: ").lower())

    if (feeling in goodfeelings): print(f"\n{cn} (^v^) Good news! \n{cn} I'm glad that you are feeling {feeling}!"); endSubProgram("happy")
    elif (feeling in badfeelings):
        print(f"\n{cn} I'm sorry you feel like this \n{cn} Do you want to talk about it?")

        response = str(input(f"{name}: ").lower())

        if (response == "no"): print(f"\n{cn} Ok, no problem. \n{cn} Try doing something that makes you happy, or talking to someone that makes you happy"); endSubProgram("sad")
        elif (response == "yes"): pass
        else: pass 

    elif (feeling in neutralfeelings):
        print(f"\n{cn} Just {feeling}?")
        response = str(input(f"{name}: ").lower())

        if (response == "yes"):
            print(f"\n{cn} Well if you are sure that you are ok, \n{cn} just remember that you can come to me if you need to talk, \n{cn} and you have wonderful friends and family to help you out as well")
            endSubProgram("sad")
        elif (response == "no"): pass
        else: pass 
    else: saveFeeling(feeling)

def saveFeeling(feeling):
    def textFileWrite(feeling, cat, importname, location):
        print(f"\n{cn} Ok, I will remember {feeling} is a {cat} feeling")
        importname = open(location,"a")
        importname.write("\n" + feeling)
        importname.close()

    print(f"\n{cn} I don't know {feeling}, is it good, bad or neutral?")
    response = str(input(f"{name}: ").lower())

    if (response == "good"): textFileWrite(feeling, "good", gfimport, "./Text Files/Feelings/goodfeelings.txt"); endSubProgram("happy")
    elif (response == "bad"): textFileWrite(feeling, "bad", bfimport, "./Text Files/Feelings/badfeelings.txt"); endSubProgram("sad")
    elif (response == "neutral"): textFileWrite(feeling, "neutral", gfimport, "./Text Files/Feelings/goodfeelings.txt"); endSubProgram("neutral")

def changeUser():
    print(f"{cn} Would you like to sign out {name}?")
    response = str(input(f"{name}: ").lower())

    if (response == "yes" or response == "y"):
        changeBotName("User")
        print(f"{cn} Signed out!")
        time.sleep(1)
        clear()
        getName()
    elif (response == "no" or response == "n"): endSubProgram("neutral")

def trivia(): print(f"\n{cn} Hello, {name}! Did you know: {random.choice(facts)}"); endSubProgram("happy")

def jokes(): pass

def flirting(): pass

def clearMemory(): pass

def story():
    print(f"\n{cn} Select an option for the story you want to hear:")
    print(f"\nOption A | Pirates, Chicken Nuggets, Death, Love \nOption B | Boomerang, Ice cream, Sauce \nOption C | Flowers, Stars, The Netherlands \n")

    valid = False
    while (valid == False):
        response = str(input(f"{name}: ").lower())

        if (response == "a"): st = open("Text Files/Stories/story1.txt", "r", encoding="utf8"); valid = True
        elif (response == "b"): st = open("Text Files/Stories/story2.txt", "r", encoding="utf8"); valid = True
        elif (response == "c"): st = open("Text Files/Stories/story3.txt", "r", encoding="utf8"); valid = True
        else: valid = False
    
    story = st.read()
    print(f"\n{story}")
    endSubProgram("neutral")

##main menu call
getName()