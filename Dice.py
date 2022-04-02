import tkinter
from tkinter import *
from PIL import Image,ImageTk
import os, random

label1 = ""
label2 = "" 

def Generate():
    global label1,label2
    label1.destroy()
    label2.destroy()
    path = "Dice Image/"
    files = os.listdir(path)
    d = random.choice(files)
    Dice1 = Image.open(path + str(d))
    images1 = ImageTk.PhotoImage(Dice1)

    label1 = Label(image=images1)
    label1.image = images1

    # Position image
    label1.place(x=100, y=100)

    files2 = os.listdir(path)
    d2 = random.choice(files2)
    Dice2= Image.open(path + str(d2))
    Images2 = ImageTk.PhotoImage(Dice2)

    label2 = Label(image=Images2)
    label2.image = Images2

    label2.place(x=500,y=100)

root = Tk()
root.title("Dice")
root.geometry('900x600')

Generate = Button(root,text="Generate Dice",bg="green",fg='white',command=Generate)
Generate.place(relx=0.5,rely=0.02,anchor=N)

label1 = Label()
label2 = Label()

root.mainloop()