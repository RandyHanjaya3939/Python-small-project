from tkinter import *
import random


randomnumber = ""
TandaTanya = []
Nmember = []
reverse = ""
check = 0
score = 0

def GenerateNumber():
    global randomnumber,TandaTanya,indexnew,indexold,Nmember,reverse,check
    indexnew = 0
    indexold = 0
    Nmember = []
    reverse = ""
    check = 0
    Number.config(text="")
    TandaTanya = []
    Answer['state'] = NORMAL
    temp = random.randint(0,2000)
    randomnumber = temp
    jumlahangka = 0
    while(temp >= 1):
        temp = temp/10
        jumlahangka = jumlahangka + 1   

    while(jumlahangka != 0):
        TandaTanya.append('?')
        jumlahangka = jumlahangka - 1

    n = len(TandaTanya)
    soal = ""
    for i in range(n):
        soal = soal  + TandaTanya[i]

    Number.config(text=soal)

def GetHint():
    global reverse,check,indexnew,indexold,TandaTanya
    temp2 = randomnumber
    if(check == 0):
        while(temp2 > 1):
            Nmember.append(int(temp2%10))
            temp2 = temp2/10
        reverse = Nmember[::-1]
        check = 1

    TandaTanya[indexold] = reverse[indexnew]
    indexold = indexold + 1
    indexnew = indexnew + 1
    n = len(TandaTanya)
    soalWhint = ""
    for i in range(n):
        soalWhint = soalWhint  + str(TandaTanya[i])

    Number.config(text=soalWhint)
    
def CheckAnswer():
    global randomnumber,score
    answer = UAnswer.get()
    if(int(answer) == randomnumber):
        Hasil.config(text = "Benar!!", fg="green")
        Number.config(text=randomnumber)
        score = score + 1
        scores.config(text="Score : " + str(score))
        Answer['state'] = DISABLED
    else:
        Hasil.config(text = "Belum Tepat!!", fg="red")


root = Tk()
root.title("Number Guessing Game")
root.geometry("450x400")

Ptitle = Label(root,text="Guess The Number!",font=("",15))
Ptitle.place(relx=0.5,rely=0,anchor=N)

Number = Label(root, text="",font=("",25),fg="red")
Number.place(relx=0.5,rely=0.1,anchor=N)

GenerateButton = Button(root,text="Generate Number",command=GenerateNumber,bg="red",fg="white")
GenerateButton.place(relx=0.5,rely=0.23,anchor=N)

GenerateHint = Button(root,text="Get Hint",command=GetHint, bg="green", fg="white")
GenerateHint.place(relx=0.5,rely=0.33,anchor=N)

UAnswer = Entry(root)
UAnswer.place(relx=0.5,rely=0.43,anchor=N)

Answer = Button(root,text="Check Answer",command=CheckAnswer)
Answer.place(relx=0.5,rely=0.5,anchor=N)

Hasil = Label(root, text="",font=("",25),fg="red")
Hasil.place(relx=0.5,rely=0.6,anchor=N)

scores = Label(root,text="Score : 0")
scores.grid()

root.mainloop()