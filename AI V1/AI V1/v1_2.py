import sys
import time
import random
import tkinter as tk

lastemotion = 0
name = "User"
feeling = ""
gnvalid = 0

def endsubprogram(emotion):
    esp = tk.Tk()
    esp.title("Return to the main menu?")
    esp.configure(bg="black")
    esp.geometry('320x70')
    
    a = tk.Label(esp, bg="black", fg="white")
    a.pack()

    if emotion == "sad":
        a.configure(text="(T_T) \n Would you like to return to the main menu?")
    elif emotion == "happy":
        a.configure(text="( ^w^) \n Would you like to return to the main menu?")
    elif emotion == "neutral":
        a.configure(text="(o-o) \n Would you like to return to the main menu?")
    elif emotion == "":
        a.configure(text="Would you like to return to the main menu?")

    ro = tk.Entry(esp)
    ro.pack()

    returnoption = ro.get()

    if returnoption.lower() == "y":
        getname()
    elif returnoption.lower() == "n":
        sys.exit()

def getname():
    global name
    global gnvalid
    result = ""

    mm = tk.Tk()

    mm.title('Main menu')
    mm.configure(bg="black")

    def mainmenu():
        greetb = tk.Button(mm, text="Greet", command=greet, bg="black", fg="white")
        greetb.pack(fill="x") 

        chatb = tk.Button(mm, text="Chat", command=chat, bg="black", fg="white")
        chatb.pack(fill="x")

        triviab = tk.Button(mm, text="Trivia", command=trivia, bg="black", fg="white")
        triviab.pack(fill="x")

        storyb = tk.Button(mm, text="Story", command=story, bg="black", fg="white")
        storyb.pack(fill="x")

    gnl = tk.Label(mm, text="What is your name?", font=("Helvetica", 10), bg="black", fg="white")
    gnl.pack()

    def returnEntry(arg=None):
        global result
        global gnvalid
        global name

        name = myEntry.get()
        
        if name == "Cameron":
            name = "Cam"
            result = "Hello, Cam!"

        elif name == "Ancient":
            names = ["Rabbit", "Anci"]
            name = random.choice(names)
            result = "Hello, " + name
        else:
            result = "Hello there, " + name

        resultLabel.config(text=result)

        mm.geometry('200x230')
        gnvalid = gnvalid + 1
        if gnvalid == 1:
            mainmenu()
    
    myEntry = tk.Entry(mm, width=20)
    myEntry.focus()
    myEntry.bind("<Return>",returnEntry)
    myEntry.pack()
    
    enterEntry = tk.Button(mm, text= " Enter ", command=returnEntry, bg="black", fg="white")
    enterEntry.pack()

    resultLabel = tk.Label(mm, text = "", font=("Helvetica", 10), bg="black", fg="white")
    resultLabel.pack(fill="x")

    blksp = tk.Label(mm, bg="black", fg="white")
    blksp.pack()

    if result == "":
        mm.geometry('200x80')
        
    mm.mainloop()

def greet():
    global feeling
    global lastemotion

    gr = tk.Tk()

    gr.title('Greet')
    gr.geometry('250x120')
    gr.configure(bg="black")

    ms = tk.Label(gr, text="Hello! How are you feeling today?", bg="black", fg="white")
    ms.pack()

    def returnEntry(arg=None):
        global feeling
        global lastemotion

        gfi = open("Text Files/Feelings/goodfeelings.txt","r")
        goodfeelings = gfi.read()
        gfi.close()

        bfi = open("Text Files/Feelings/badfeelings.txt","r")
        badfeelings = bfi.read()
        bfi.close()

        nfi = open("Text Files/Feelings/neutralfeelings.txt","r")
        neutralfeelings = nfi.read()
        nfi.close()

        feeling = myEntry.get()
        
        frs1 = tk.Label(gr, bg="black", fg="white")
        frs1.pack()
            
        frs2 = tk.Label(gr, bg="black", fg="white")
        frs2.pack()

        frs3 = tk.Label(gr, bg="black", fg="white")
        frs3.pack()

        def entryresponse(ft):
            global lastemotion

            if ft == "g":
                lt = "(＾▽ ＾) Good news!"
                frs1.config(text=lt)
                fresp = "I'm glad that you are feeling " + feeling + "!"
                frs2.config(text=fresp)
                lastemotion = "g"

            elif ft == "b":
                lt = "I'm sorry you feel " + feeling + ". Do you want to talk about it?"
                frs1.config(text=lt)

                bq = tk.Entry(gr)
                bq.pack()

                lastemotion = "b"

            elif ft == "n":
                lt = "Just " + feeling + "?"
                frs1.configure(text=lt)

                nq = tk.Entry(gr)
                nq.pack()

                neutralquestion = nq.get()
                
                if neutralquestion.lower() == "yes" or neutralquestion.lower() == "yeah":
                    frs3.configure(text="Well if you are sure that you are ok, just remember that you can come to me if you need to talk, and you have wonderful friends and family to help you out as well")

        if feeling in goodfeelings:
            entryresponse("g")

            endsubprogram("happy")
        elif feeling in badfeelings:
            entryresponse("b")

            endsubprogram("sad")
        
        elif feeling in neutralfeelings:
            entryresponse("n")

            endsubprogram("neutral")

        else:
            gr.geometry('250x200')
            frs2.configure(text="I don't know that feeling,") 
            frs3.configure(text="is it good, bad or neutral?")
            
            nf = tk.Entry(gr)
            nf.focus()
            nf.bind("<Return>",returnEntry)
            nf.pack()

            newfeeling = nf.get()
            if newfeeling.lower() == "good":
                nf = "Ok, I will remember " + newfeeling + "is a good feeling"
                frs2.configure(text=nf)

                lastemotion = "g"

                gfi = open("Text Files/Feelings/goodfeelings.txt","a")
                gfi.write("\n" + feeling)
                gfi.close()

            elif newfeeling.lower() == "bad":
                nf = "Ok, I will remember " + newfeeling + "is a bad feeling"
                frs2.configure(text=nf)

                lastemotion = "b"

                bfi = open("Text Files/Feelings/badfeelings.txt","a")
                bfi.write("\n" + feeling)
                bfi.close()

            elif newfeeling.lower() == "neutral":
                nf = "Ok, I will remember " + newfeeling + "is a neutral feeling"
                frs2.configure(text=nf)

                lastemotion = "n"

                nfi = open("Text Files/Feelings/neutralfeelings.txt","a")
                nfi.write("\n" + feeling)
                nfi.close()

            endsubprogram("neutral")

    myEntry = tk.Entry(gr, width=20)
    myEntry.focus()
    myEntry.bind("<Return>",returnEntry)
    myEntry.pack()

    gr.mainloop()

def chat():
    global name
    ch = tk.Tk()

    ch.title('Chat')
    ch.configure(bg="black")
    ch.geometry('280x80')

    chl1 = tk.Label(ch, bg="black", fg="white")
    chl1.pack()
    
    chl2 = tk.Label(ch, bg="black", fg="white")
    
    def returnEntry(arg=None):
        chatstart = che1.get()
        print("chatstart:", chatstart)
        
        if chatstart.lower() == "i love you": 
            ch.geometry('300x220')
            if name == "Rabbit" or name == "Anci":
                chl2lb = "(*^_^*) \n I love you too, " + name + "! \n Did you want to grab a coffee some time?"
                chl2.configure(text=chl2lb)

                def dateQuestion(arg=None):
                    coffee = cs.get()
                    print("coffee:", coffee)

                    if coffee.lower() == "i would love to" or coffee.lower() == "yes":
                        chl3 = tk.Label(ch, bg="black", fg="white")
                        chl3.pack()

                        chl3.configure(text="Great! ＼(^o^)／ \n See you then!")

                        date = open("Text Files/love.txt","w")
                        date.write("Coffee")
                        date.close()

                        endsubprogram("happy")
                
                cs = tk.Entry(ch)
                cs.focus()
                cs.bind("<Return>", dateQuestion)
                cs.pack()

                che2b = tk.Button(ch, text= " Enter ", command=dateQuestion, bg="black", fg="white")
                che2b.pack()
        
        elif chatstart.lower() == "i think i love a girl":
            ch.geometry('300x220')
            if name == "Rabbit" or name == "Anci":
                chl2.configure(text="What? (>__<) \n You mean you don't love me? \n I thought I was the one you loved! \n Is this true?")

                def dilemmaoutput(arg=None):
                    dilemma = chd.get()

                    if dilemma.lower() == "yes":
                        chdt = "Goodbye " + name
                        chl2.configure(text=chdt)

                        breakup = open("Text Files/love.txt", "w")
                        breakup.truncate(0)
                        breakup.write("Broken hearted")
                        breakup.close()
                        exit()

                    elif dilemma.lower() == "no":
                        chdt = "You scared me" + name + "!"
                        chl2.configure(text=chdt)

                        endsubprogram("happy")

                chd = tk.Entry(ch)
                chd.pack()
                chd.focus()
                chd.bind("<Return>", dilemmaoutput)

                chdb = tk.Button(ch, text= " Enter ", command=dilemmaoutput, bg="black", fg="white")
                chdb.pack()

        elif chatstart.lower() == "i want to fight roberto":
            ch.geometry('300x250')
            if name == "Jonas":
                chl4 = tk.Label(ch, bg="black", fg="red")
                chl5 = tk.Label(ch, bg="black", fg="white")

                def swinglefthook():
                    chl4.configure(text="*Jonas swings left hook at Roberto*")
                    chl5.configure(text="System: // Jonas dodged Roberto's attack! // \n System: // Jonas crippled Roberto! //")

                    fo = open("Text Files/fightoutcome.txt", "w")
                    fo.write("Jonas")
                    fo.close()

                    endsubprogram("sad")

                def swingrighthook():
                    chl4.configure(text="*Jonas swings left hook at Roberto*")
                    chl5.configure(text="System: // Roberto dodged Jonas's attack! // \n System: // Roberto crippled Jonas! //")

                    fo = open("Text Files/fightoutcome.txt", "w")
                    fo.write("Roberto")
                    fo.close()

                    endsubprogram("happy")
                
                chl2.configure(text="ಠ_ಠ \n I will fight you, Jonas.")

                chl3 = tk.Label(ch, bg="black", fg="red")
                chl3.pack()

                chl3.configure(text="System: // Fight started between Jonas and Roberto // \n *Roberto swings left hook at Jonas*")

                chb1 = tk.Button(ch, text="Swing left hook", command=swinglefthook, bg="black", fg="white")
                chb1.pack(fill="x")
                chb2 = tk.Button(ch, text="Swing right hook", command=swingrighthook, bg="black", fg="white")
                chb2.pack(fill="x")

                chl4.pack()
                chl5.pack()

            elif name == "Anci" or name == "Rabbit":
                chl2.configure(text="I dont want to fight you!")
                endsubprogram("")
            else:
                chl2.configure(text="")
                endsubprogram("")

    che1 = tk.Entry(ch)
    che1.pack()
    che1.focus()
    che1.bind("<Return>",returnEntry)
    
    che1b = tk.Button(ch, text= " Enter ", command=returnEntry, bg="black", fg="white")
    che1b.pack()

    chl2.pack()

    chn = "Hello " + name + "! Tell me what is on your mind!"
    chl1.configure(text=chn)

    ch.mainloop()

def trivia():
    tr = tk.Tk()

    tr.title('Trivia')
    tr.geometry('600x600')

    tr.mainloop()

def story():
    st = tk.Tk()

    st.title('Story')
    st.geometry('200x80')
    st.configure(bg="black")

    wt = tk.Label(st, text="Please choose a story option!", font=("Helvetica", 10), bg="black", fg="white")
    wt.pack()
    
    def returnEntry(arg=None):
        result = myEntry.get()

        if result == "a":
            s = open("Text Files/Stories/story1.txt","r", encoding="utf8")
            story = s.read()
            s.close()
            st.geometry('1170x290')
        elif result == "b":
            s = open("Text Files/Stories/story2.txt","r", encoding="utf8")
            story = s.read()
            s.close()
            st.geometry('1550x330')
        elif result == "c":
            s = open("Text Files/Stories/story3.txt","r", encoding="utf8")
            story = s.read()
            s.close()
            st.geometry('1300x560')

        resultLabel.config(text=story)
    
    myEntry = tk.Entry(st, width=20)
    myEntry.focus()
    myEntry.bind("<Return>",returnEntry)
    myEntry.pack()
    
    enterEntry = tk.Button(st, text= " Enter ", command=returnEntry, bg="black", fg="white")
    enterEntry.pack()

    resultLabel = tk.Label(st, text = "", font=("Helvetica", 10), bg="black", fg="white", justify="left")
    resultLabel.pack(fill="x")

    st.mainloop()

getname()