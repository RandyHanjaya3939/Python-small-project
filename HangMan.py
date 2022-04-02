import tkinter
from tkinter import *
from PIL import Image,ImageTk
import random

pic = 1
Hewan = ['Sapi','Singa','Nyamuk','Rusa','Buaya']
Buah = ['Apel','Pisang','Jeruk','Nanas','Strawberry']
Jawaban = ""
Garisbawah = []
Soal = ""
StoreWord = ""
TempWord = ""
point = 0

def GenerateWord():
    global Hewan,Buah,Jawaban,Garisbawah,Soal, StoreWord, Ans, AnsBtn,TempWord,pic
    Soal = ""
    StoreWord = ""
    TempWord = ""

    pic = 1
    path = "HangMan/" + str(pic) +".png"
    HangMans = ImageTk.PhotoImage(Image.open(path))
    Tkinterpic.config(image=HangMans)
    Tkinterpic.image = HangMans

    randomnumber = random.randint(1,2)
    Ans.destroy()
    AnsBtn.destroy()
    if(randomnumber == 1):
        Jawaban = random.choice(Hewan)
        WordLen = len(Jawaban)
        while(WordLen >= 1):
            Soal = Soal + "_ "
            WordLen = WordLen - 1
        Hint.config(text="Hint: Nama Hewan")

    elif(randomnumber == 2):
        Jawaban = random.choice(Buah)
        WordLen = len(Jawaban)
        while(WordLen >= 1):
            Soal = Soal + "_ "
            WordLen = WordLen - 1
        Hint.config(text="Hint: Nama Buah")

    Soals.config(text = Soal)
    Ans = Entry(root)
    Ans.place(relx=0.5,rely=0.62,anchor=N)
    AnsBtn = Button(root,text="Guess",command=CekAns)
    AnsBtn.place(relx=0.5,rely=0.65,anchor=N)

def CekAns():
    global Soal,TempWord,pic,Tkinterpic,AnsBtn,Jawaban,point
    TempSoal = "" ##untuk mengganti soal _ _ _ menjadi berisi jika user memasukan huruf yg tepat(barus 59 & 62)
    Tempsoal2 = Soal ##Soal akan diubah mengikuti temp soal, dan nanti soal akan dibandingkan dengan tempsoal 2. jika sama, maka user melakukan kesalahan (baris 65 & 67).
    
    ##untuk mengecek apakah input user lebih dari 1 huruf
    Word = Ans.get()

    ##menampung seluruh input user
    TempWord = TempWord + Ans.get()

    if(len(Word) > 1):
        Warns.config(text="Masukan 1 huruf!")
    else:
        Warns.config(text="")
        for i in Jawaban:
            if i.lower() in TempWord.lower():
                TempSoal = TempSoal + i
                Soal = TempSoal ##Var soal yg dibuat pada generateWord akan diupdate secara berkala
            else:
                TempSoal = TempSoal + "_ "
                Soal = TempSoal ##Var soal yg dibuat pada generateWord akan diupdate secara berkala

        ##mengganti soal dengan soal baru yg sudah berisikan input user (jika benar)
        Soals.config(text = TempSoal)

    if(Soal == Tempsoal2):
        pic = pic + 1
    elif(Soal == Tempsoal2):
        pic = pic

    if(Jawaban == TempSoal):
        path = "HangMan/" + str(pic) +"s.png"
        HangMans = ImageTk.PhotoImage(Image.open(path))
        Tkinterpic.config(image=HangMans)
        Tkinterpic.image = HangMans
        AnsBtn['state'] = DISABLED
        Ans['state'] = DISABLED
        point = point + 1
        Playerpoint.config(text="Point: " + str(point))
    elif(pic <= 7):
        path = "HangMan/" + str(pic) +".png"
        HangMans = ImageTk.PhotoImage(Image.open(path))
        Tkinterpic.config(image=HangMans)
        Tkinterpic.image = HangMans
    elif(pic == 8):
        path = "HangMan/" + str(pic) +".png"
        HangMans = ImageTk.PhotoImage(Image.open(path))
        Tkinterpic.config(image=HangMans)
        Tkinterpic.image = HangMans
        AnsBtn['state'] = DISABLED
        Ans['state'] = DISABLED





root = Tk()
root.title("HangMan")
root.geometry("500x800")

ptitle = Label(root,text="Welcome to HangMan game",font=("",15))
ptitle.place(relx=0.5,rely=0.01,anchor=N)

path = "HangMan/" + str(pic) +".png"

Playerpoint = Label(root,text = "Point: " + str(point))
Playerpoint.place(anchor=NW)

HangMans = ImageTk.PhotoImage(Image.open(path))
Tkinterpic = Label(image=HangMans)
Tkinterpic.image = HangMans

Tkinterpic.place(relx=0.5,rely=0.1,anchor=N)

GenerateButton = Button(root,text="Generate Word",command=GenerateWord)
GenerateButton.place(relx=0.5,rely=0.45,anchor=N)

Hint = Label(root, text="",fg="green")
Hint.place(relx=0.5,rely=0.51,anchor=N)

Soals = Label(root,text="",font=("",15))
Soals.place(relx=0.5,rely=0.55,anchor=N)

Ans = Entry()
AnsBtn = Button()

Warns = Label(root,text="",fg="red")
Warns.place(relx=0.5,rely=0.68,anchor=N)

root.mainloop()