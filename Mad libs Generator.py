from os import system
from tkinter import *

root = Tk()
root.title("Mad Libs Generator")
root.geometry("420x400")
root.resizable(width=False, height=False)

def GenerateWord():

    Uname =  Nameinput.get()
    Ucompanion = Companioninput.get()
    UPlace = PlaceInput.get()
    Result.config(text="Hello my name is " + Uname + ". And this is my friend " + Ucompanion +". Today we are at the " + UPlace)

Ptitle = Label(root, text="Mad Libs Generator",font=("Arial",15),fg="red")
Ptitle.grid(row=0,column=1)

Name = Label(root,text="Name            : ")
Name.grid(row=1,column=0,sticky=W)

Nameinput = Entry(root, width=50)
Nameinput.grid(row=1,column=1)

Companion = Label(root,text="Companion : ")
Companion.grid(row=2,column=0,sticky=W,pady=10)

Companioninput = Entry(root, width=50)
Companioninput.grid(row=2,column=1)

Placee = Label(root,text="Place             :")
Placee.grid(row=3,column=0,sticky=W,pady=5)

PlaceInput = Entry(root, width=50)
PlaceInput.grid(row=3,column=1)

GenerateButton = Button(root,text="Generate !",bg="white",fg="black",command=GenerateWord)
GenerateButton.grid(row=4,column=1,pady=10)

Result = Label(root,text="",wraplengt=300)
Result.place(relx=0.15,rely=0.5)

root.mainloop()