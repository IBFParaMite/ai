import sys
import time
import tkinter as tk


lastemotion = 0
name = "User"
feeling = 0

def endsubprogram(emotion):
    # changes the face at the beggining of the message based on the emotion variable set in the initial command
    # if emotion == "sad":
        # print(cn, "(T_T)")
        # reac = tk.Label()

    # elif emotion == "happy":
        # print(cn, "( ^w^)")
    # elif emotion == "neutral":
        # print(cn, "(o-o)")

    # gives the user the choice to return to the main menu or to terminate the program
    # print(cn, "Would you like to return to the main menu", name, "? (Y/N)")
    # print(cn, "Y | Main menu")
    # print(cn, "N | Terminate program")
    returnoption = str(input("User: "))

    if returnoption == "Y" or returnoption == "y":
        getname()
    elif returnoption == "N" or returnoption == "n":
        # print("Goodbye",name,"!")
        time.sleep(3)
        sys.exit()

def navbar(windowname):
    mmb = tk.Button(windowname, text="Main menu", command=greet)
    mmb.pack()

def getname():
    global name
    mm = tk.Tk()

    mm.title('Main menu')
    mm.geometry('200x270')
    mm.configure(bg="black")

    def mainmenu():
        greetb = tk.Button(mm, text="Greet", command=greet, bg="black", foreground="white")
        greetb.pack(fill="x") 

        chatb = tk.Button(mm, text="Chat", command=chat, bg="black", foreground="white")
        chatb.pack(fill="x")

        triviab = tk.Button(mm, text="Trivia", command=trivia, bg="black", foreground="white")
        triviab.pack(fill="x")

        storyb = tk.Button(mm, text="Story", command=story, bg="black", foreground="white")
        storyb.pack(fill="x")

        chuserb = tk.Button(mm, text="Change User", command=changeUser, bg="black", foreground="white")
        chuserb.pack(fill="x")

        exitb = tk.Button(mm, text="Exit", command=exit, bg="black", foreground="white")
        exitb.pack(fill="x")

    gnl = tk.Label(mm, text="What is your name?", font=("Helvetica", 10), bg="black", foreground="white")
    gnl.pack()

    def returnEntry(arg=None):
        result = "Hello there, " + myEntry.get()
        resultLabel.config(text=result)
    
    # Create the Entry widget
    myEntry = tk.Entry(mm, width=20)
    myEntry.focus()
    myEntry.bind("<Return>",returnEntry)
    myEntry.pack()
    
    # Create the Enter button
    enterEntry = tk.Button(mm, text= "Enter", command=returnEntry, bg="black", foreground="white")
    enterEntry.pack(fill="x")

    # Create and emplty Label to put the result in
    resultLabel = tk.Label(mm, text = "", font=("Helvetica", 10), bg="black", foreground="white")
    resultLabel.pack(fill="x")

    blksp = tk.Label(mm, bg="black", foreground="white")
    blksp.pack()

    mainmenu()
    mm.mainloop()

def greet():
    global feeling
    global lastemotion

    gr = tk.Tk()

    gr.title('Greet')
    gr.geometry('600x600')

    # feelings import
    # opens the goodfeelings.txt file in read mode
    gfi = open("Feelings/goodfeelings.txt","r+")
    # stores the values from the file in a variable
    goodfeelings = gfi.read()
    # closes the file
    gfi.close()

    # opens the badfeelings.txt file in read mode
    bfi = open("Feelings/badfeelings.txt","r+")
    # stores the values from the file in a variable
    badfeelings = bfi.read()
    # closes the file
    bfi.close()

    # opens the neutralfeelings.txt file in read mode
    nfi = open("Feelings/neutralfeelings.txt","r+")
    # stores the values from the file in a variable
    neutralfeelings = nfi.read()
    # closes the file
    nfi.close()

    feeling = tk.Label(gr)
    feeling.pack()

    if feeling in goodfeelings:
            # print(cn, "(＾▽ ＾) Good news!")
            # print(cn, "I'm glad that you are feeling", feeling, "!")
            lastemotion = "g"

            endsubprogram("happy")
        
    # if the string in the feeling variable is in the badfeelings variable, run this dialogue
    elif feeling in badfeelings:
        # print(cn, "I'm sorry you feel like this")
        # print(cn, "Do you want to talk about it?")
        # bfresponse = str(input("User: "))
        print()
        
    # if the string in the feeling variable is in the neutralfeelings variable, run this dialogue
    elif feeling in neutralfeelings:
        # print(cn, "Just", feeling, "?")
        neutralquestion = str(input("User: "))

        if neutralquestion == "yes" or neutralquestion == "Yes" or neutralquestion == "yeah" or neutralquestion == "Yeah":
            # print(cn, "Well if you are sure that you are ok, just remember that you can come to me if you need to talk,")
            # print(cn, "and you have wonderful friends and family to help you out as well")
            lastemotion = "n"
            
            endsubprogram("neutral")

    # if the string isn't in any of the variables, then runs the function savefeeling().
    else:
        savefeeling()

    gr.mainloop()

# function to save a new feeling to the text files
def savefeeling():
    global name
    global feeling
    
    global lastemotion

    # print(cn, "I don't know that feeling, is it good, bad or neutral?")
    # saves the user input as a string in the variable newfeeling
    newfeeling = str(input("User: "))

    # based on the value of newfeeling, writes the value to the corresponding list
    if newfeeling == "good" or newfeeling == "Good":
        print("Ok, I will remember", feeling, " is a good feeling")
        lastemotion = "g"
        gfi = open("Feelings/goodfeelings.txt","a")
        # writes the feeling to the list with a new line in front of it so the text isn't clustered together
        gfi.write("\n" + feeling)
        gfi.close()

    elif newfeeling == "bad" or newfeeling == "Bad":
        print("Ok, I will remember", feeling, " is a bad feeling")
        lastemotion = "b"
        bfi = open("Feelings/badfeelings.txt","a")
        bfi.write("\n" + feeling)
        bfi.close()

    elif newfeeling == "neutral" or newfeeling == "Neutral":
        print("Ok, I will remember", feeling, " is a neutral feeling")
        lastemotion = "n"
        nfi = open("Feelings/neutralfeelings.txt","a")
        nfi.write("\n" + feeling)
        nfi.close()

    endsubprogram("neutral")

def chat():
    ch = tk.Tk()

    ch.title('Chat')
    ch.geometry('600x600')

    ch.mainloop()

def trivia():
    tr = tk.Tk()

    tr.title('Trivia')
    tr.geometry('600x600')

    tr.mainloop()

def story():
    st = tk.Tk()

    st.title('Story')
    st.geometry('200x100')
    st.configure(bg="black")

    wt = tk.Label(st, text="Please choose a story option!", font=("Helvetica", 10), bg="black", foreground="white")
    wt.pack()
    
    def returnEntry(arg=None):
        result = myEntry.get()

        if result == "a":
            s = open("Stories/story1.txt","r")
            result = s.read()
            s.close()
            st.geometry('1150x270')
        elif result == "b":
            s = open("Stories/story2.txt","r")
            result = s.read()
            s.close()
            st.geometry('1550x320')
        elif result == "c":
            s = open("Stories/story3.txt","r")
            result = s.read()
            s.close()
            st.geometry('1300x550')

        resultLabel.config(text=result)
    
    # Create the Entry widget
    myEntry = tk.Entry(st, width=20)
    myEntry.focus()
    myEntry.bind("<Return>",returnEntry)
    myEntry.pack()
    
    # Create the Enter button
    enterEntry = tk.Button(st, text= " Enter ", command=returnEntry, bg="black", foreground="white")
    enterEntry.pack()

    # Create and emplty Label to put the result in
    resultLabel = tk.Label(st, text = "", font=("Helvetica", 10), bg="black", foreground="white", justify="left")
    resultLabel.pack(fill="x")

    st.mainloop()

def changeUser():
    chu = tk.Tk()

    chu.title('Change User')
    chu.geometry('600x600')

    chu.mainloop()

def exit():
    ex = tk.Tk()

    ex.title('Exit')
    ex.geometry('600x600')

    ex.mainloop()

getname()
