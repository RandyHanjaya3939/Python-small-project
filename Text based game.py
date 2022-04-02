import builtins
from tkinter import *

Question = 1
point = 0
Aans = ""
Bans =""
Nexts = ""

def PlayGame():
    global Question,Aans,Bans,Nexts
    YesButton.destroy()
    NoButton.destroy()
    Aans.destroy()
    Bans.destroy()
    Nexts.destroy()
    if(Question == 1):
        Title.config(text="Hasil dari 1 + 1 adalah?")
        Aans = Button(root,text = "2",width=10,command=Right)
        Aans.place(relx=0.35,rely=0.4,anchor=N)

        Bans = Button(root,text = "7",width=10,command=Falses)
        Bans.place(relx=0.65,rely=0.4,anchor=N)
        
    elif(Question == 2):
        Result.config(text="")
        Title.config(text="Kapan hari kemerdekaan Indonesia?")
        Aans = Button(root,text = "21 September 1945",width=15,command=Falses)
        Aans.place(relx=0.35,rely=0.4,anchor=N)

        Bans = Button(root,text = "17 Agustus 1945",width=15,command=Right)
        Bans.place(relx=0.65,rely=0.4,anchor=N)

    elif(Question == 3):
        Result.config(text="")
        Aans.destroy()
        Bans.destroy()
        Title.config(text="Tamat")
        Title.place(relx=0.5,rely=0.4,anchor=N)

    Question = Question + 1

def Right():
    global point,Nexts
    point = point + 1
    Aans['state'] = DISABLED
    Bans['state'] = DISABLED
    Result.config(text="Benar!",fg="green")
    Nexts = Button(root,text="Next",bg="white",fg="black",command=PlayGame)
    Nexts.place(relx=0.5,rely=0.5,anchor=N)
    Score.config(text="Score : " + str(point))


def Falses():
    global point,Nexts
    if(point == 0):
        point = 0
    else:
        point = point - 1

    Aans['state'] = DISABLED
    Bans['state'] = DISABLED
    Result.config(text="Salah!",fg="red")
    Nexts = Button(root,text="Next",bg="white",fg="black",command=PlayGame)
    Nexts.place(relx=0.5,rely=0.5,anchor=N)
    Score.config(text="Score : " + str(point))

def Quit():
    YesButton.destroy()
    NoButton.destroy()
    Title.config(text="Thankyou, See You Later")
    Title.place(relx=0.5,rely=0.4,anchor=N)

root = Tk()
root.title("Text Based Game")
root.geometry("500x400")

Title = Label(root, text="Welcome to the game, play the game?",font=("",15))
Title.place(relx=0.5,rely=0.3,anchor=N)

YesButton = Button(root,text = "Yes",bg="green",fg="white",width=10,command=PlayGame)
YesButton.place(relx=0.4,rely=0.4,anchor=N)

NoButton = Button(root,text = "No",bg="Red",fg="white",width=10,command=Quit)
NoButton.place(relx=0.6,rely=0.4,anchor=N)

Result = Label(root,text="",font=("",10))
Result.place(relx=0.5,rely=0.6,anchor=N)

Score = Label(root,text="Score : 0")
Score.place(relx=0.0,rely=0.0,anchor=NW)

Aans = Button()
Bans = Button()
Nexts = Button()

root.mainloop()