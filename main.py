# import libraries used in some of the functions of the bot
import sys
import csv
import os
import random

# list of arrays
names = ["Hank", "Roberto", "Sylvia",
         "Bob", "George", "Jacob",
         "Charlie", "Barry", "Tony",
         "Alex", "Jessica", "Jason",
         "Kat", "Andrey", "Beck",
         "Melissa", "Lucas", "Mario",
         "Jane", "James", "Gerard"]

vipusers = ["Cameron", "Ancient", "Aleyna", "Jonas"]

# list of global variables
computernameprint = random.choice(names)
computername = computernameprint + ":"
name = "User"
feeling = 0
lastemotion = 0

# function that brings the user back to the main menu
def endsubprogram():
    print()
    print(computername, "Would you like to return to the main menu", name, "? (Y/N)")
    returnoption = input("User: ")

    if returnoption == "Y" or returnoption == "y":
        print()
        main()
    elif returnoption == "N" or returnoption == "n":
        print()

# defining the main function of the bot
def main():
    global computername
    global computernameprint
    global name
    global feeling
    global lastemotion
    global talk

    while name == "User":
        print("Computer: Hello there!")
        print("Computer: What is your name?")
        name = str(input("User: "))

        if name in vipusers:
            print("System: // User", name, "is in the VIP List //")
            if name == "Ancient":
                computername = "Roberto:"
                computernameprint = "Roberto"
            elif name == "Cameron":
                computername = "Hank:"
                computernameprint = "Hank"
            elif name == "161616":
                protocol16()

            print(computername, "Welcome back", name, ", my name is", computernameprint, "!")
            print()
        else:
            print(computername, "Hello", name, "!")
            print()

    # print the menu options
    print("Option A | Greet")
    print("Option B | Change user")
    print("Option C | Chat")
    print("Option D | Trivia")
    print("Option X | Exit Program")
    # print a blank space between the options and the input
    print()
    # validation meaning that the user has to put in a valid option to proceed
    valid = 0
    while (valid == 0):
        # user input for the option
        option = input("System: Please select an option: ")

        if option == "A" or option == "a":
            valid = 1
            greet()
        elif option == "B" or option == "b":
            valid = 1
            changeUser()
        elif option == "C" or option == "c":
            valid = 1
            chat()
        elif option == "D" or option == "d":
            valid = 1
            trivia()
        elif option == "X" or option == "x":
            # clears the console
            def clear(): return os.system('cls')
            clear()

            # exits the program
            sys.exit()
        else:
            # if the input is not correct, display an error then go back to the beginning
            print("System: Error, please try again")
            valid = 0

# Function run to greet the user when the option A is selected
def greet():
    # list of all the global variables needed for the function
    global computername
    global computernameprint
    global name
    global feeling
    global lastemotion
    global talk

    goodfeelings = ["great", "good", "spectacular", "cheerful", "excellent"]
    neutralfeelings = ["meh", "alright", "tired", "fine"]
    badfeelings = ["bad", "awful", "dreadful"]

    print()
    print(computername, "Hello,",name, "! How are you feeling today?")
    feeling = str(input("User: "))

    if feeling in goodfeelings:
        print(computername, "(＾▽＾) Good news!")
        print(computername, "I'm glad that you are feeling", feeling, "!")
        lastemotion = "g"
        endsubprogram()
    elif feeling in neutralfeelings:
        print(computername, "Just", feeling, "?")
        neutralquestion = input("User: ")

        if neutralquestion == "yes" or neutralquestion == "Yes" or neutralquestion == "yeah" or neutralquestion == "Yeah":
            print(computername, "Well if you are sure that you are ok, just remember that you can come to me if you need to talk,")
            print(computername, "and you have wonderful friends and family to help you out as well")
            lastemotion = "n"
            endsubprogram()

    elif feeling in badfeelings:
        print(computername, "I'm sorry you feel like this")
        print(computername, "Do you want to talk about it?")
        bfresponse = input("User: ")

        if bfresponse == "no" or bfresponse == "No":
            print(computername, "Ok, no problem.")
            print(computername, "Try doing something that makes you happy, or talking to someone that makes you happy")
            lastemotion = "b"
            talk = "n"
            endsubprogram()

        else:
            print(computername, "I don't know that feeling, is it good, bad or neutral?")
            newfeeling = input("User: ")

            if newfeeling == "good" or newfeeling == "Good":
                print("Ok, I will remember", feeling, " is a good feeling")
                lastemotion = "g"

            elif newfeeling == "bad" or newfeeling == "Bad":
                print("Ok, I will remember", feeling, " is a bad feeling")
                lastemotion = "b"

            elif newfeeling == "neutral" or newfeeling == "Neutral":
                print("Ok, I will remember", feeling, " is a neutral feeling")
                lastemotion = "n"

            endsubprogram()

    else:
        returngreet()

def returngreet():
    global computername
    global computernameprint
    global name
    global feeling
    global lastemotion
    global talk

    print(computername, ": Back again,", name, "? Still feeling", feeling, "?")
    returnquestion = input("User: ")

    if returnquestion == "yes" or returnquestion == "Yes" or returnquestion == "yeah" or returnquestion == "Yeah" and lastemotion == "g":
        print(computername, "I'm glad to hear it!")
    elif returnquestion == "yes" or returnquestion == "Yes" or returnquestion == "yeah" or returnquestion == "Yeah" and lastemotion == "b":
        print(computername, "I hope you start feeling better soon, and remember you can talk about it if you want")
    elif returnquestion == "yes" or returnquestion == "Yes" or returnquestion == "yeah" or returnquestion == "Yeah" and lastemotion == "n" and talk == "y":
        print(computername, "Any improvement on how you were feeling before?")
        nimprove = input("User: ")

        if nimprove == "yes" or nimprove == "Yes" or nimprove == "yeah" or nimprove == "Yeah":
            print(computername, "Thats good, i'm glad that you are making improvements!")
        elif nimprove == "no" or nimprove == "No":
            print(computername, "I hope you start feeling better soon!")
    elif returnquestion == "yes" or returnquestion == "Yes" and lastemotion == "n" and talk == "n":
        print(computername, "Are you ready to talk about it?")
        bfresponse = input("User: ")

        if bfresponse == "no" or bfresponse == "No":
            print(computername, "Ok, no problem.")
            print(computername, "Come back again when you are ready to talk about this")
            endsubprogram()
        if bfresponse == "yes" or bfresponse == "Yes":
            print(computername, "I'm glad you are ready to talk about it")
    elif returnquestion == "no" or returnquestion == "No":
        print(computername, "How are you feeling now?")
        newfeeling = input("User: ")
        feeling = newfeeling

def changeUser():
    # list of all the global variables needed for the function
    global name
    global computername
    global computernameprint

    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if name == "User":
        print(computername, "There is no user signed in currently")
        print(computername, "Returning to the main menu")
        print()
        main()
    else:
        print(computername, "Would you like to sign out", name, "?")
        soconfirm = input("User: ")

        if soconfirm == "yes" or soconfirm == "Yes":
            name = 0
            computername = "Hank:"
            computernameprint = "Hank"
            print(computername, "Signed out...")
            print()
            main()
        elif soconfirm == "no" or soconfirm == "No":
            print(computername, "Returning to the main menu")
            print()
            main()

def chat():
    global name
    global computername
    global computernameprint

    print(computername, "Hey", name, "! Tell me what is on your mind!")
    chatstart = input("User: ")

    if chatstart == "I love you":
        print(computername, "(*^_^*)")
        print(computername, "I love you too,", name)
        print(computername, "Did you want to grab a coffee some time,", name, "?")
        coffee = input("User: ")

        if coffee == "I would love to!":
            print(computername, "Great! ＼(^o^)／")
            print(computername, "See you then!")
            endsubprogram()

    elif chatstart == "I have something on my mind":
        print(computername, "Tell me about it")
        input("User: ")

def trivia():
    global name
    global computername

    facts = ["The heart of a shrimp is located in its head.",
             "A snail can sleep for three years.",
             "It is possible to hypnotize a frog by placing it on its back and gently stroking its stomach.",
             "The fingerprints of a koala are so indistinguishable from humans that they have on occasion been confused at a crime scene.",
             "Slugs have four noses.",
             "Elephants are the only animal that can't jump.",
             "It takes a sloth two weeks to digest its food.",
             "Nearly three percent of the ice in Antarctic glaciers is penguin urine.",
             "A cow gives nearly 200,000 glasses of milk in a lifetime.",
             "Trained pigeons can tell the difference between the paintings of Pablo Picasso and Claude Monet."]

    print(computername, "Hi there",name, ", welcome to random facts!")
    print()
    print(computername, "Did you know:")
    print(random.choice(facts))
    endsubprogram()

def protocol16():
    print("System: ERROR :: PROTOCOL 16 INITIATED :: ERROR")
    print("System: User 161616 logged in")
    print("System: ")

# Go to the main menu when the program is run
main()