from os import system
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.font import BOLD
from pytube import YouTube
from pytube.request import post

FolderName = ""
FolderName2 = ""
FolderNameFinal = ""
QListSort = []
QList = []
Check = 0

def openLoc() : 
    global FolderName,FolderName2,FolderNameFinal
    FolderName = filedialog.askdirectory()
    FolderName2 = ytdEntry2.get()
    if(len(FolderName) > 1 and len(FolderName2) < 1):
        ytdEntry2.insert(0,FolderName)
        FolderNameFinal = FolderName
    elif(len(FolderName2) > 1 and len(FolderName) < 1):
        FolderNameFinal = FolderName2
    elif(len(FolderName2) > 1 and len(FolderName) > 1):
        FolderNameFinal = FolderName
    else:
        LocationError.config(text="Please Choose Folder!",fg="red")


def AvaQuality() :
    global QListSort,QList,Check
    url = ytdEntry.get()
    if(Check == 0):     
        if(len(url) > 1):
            yt = YouTube(url)
            #get all the available reso
            for i in yt.streams:
                QList.append(i.resolution)

            #Making duplicate reso in array into 1 (None appear so we can't do sorting)
            QList = list(set(QList))

            #remove None so we can sort the array
            for val in QList:
                if val != None:
                    QListSort.append(val)

            QListSort.append('Audio Only')
            #Final QList
            QListSort.sort()

        else:
            DownloadError.config(text="No URL inserted!",fg="red")

        Check = 1    
        ytdchoices.config(values=QListSort)


def DownloadVid():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url) > 1 and FolderName != ""):
        ytdError.config(text="")
        yt = YouTube(url)
        if(choice == '1080p'):
            select = yt.streams.filter(res="1080p").first()

        elif(choice == '720p'):
            select = yt.streams.filter(res="720p").first()

        elif(choice == '480p'):
            select = yt.streams.filter(res="480p").first()

        elif(choice == '360p'):
            select = yt.streams.filter(res="360p").first()
            
        elif(choice == '240p'):
            select = yt.streams.filter(res="240p").first()

        elif(choice == '144p'):
            select = yt.streams.filter(res="144p").first()

        elif(choice == '1440p'):
            select = yt.streams.filter(res="1440p").first()

        elif(choice == '2160p'):
            select = yt.streams.filter(res="2160p").first()

        elif(choice == 'Audio Only'):
            select = yt.streams.filter(only_audio=True).first()
    else:
        DownloadError.config(text="Download can't be started",font=("",15,BOLD))

    select.download(FolderNameFinal)
    DownloadError.config(text="Download Completed!")


root = Tk()
root.title("Youtube Downloader")
root.geometry("500x200")

ProgTitle = Label(root,text="YT Vid Downloader",font=("",15))
ProgTitle.grid(row=0,column=1)

ytdLabel = Label(root, text="URL                  : ")
ytdLabel.grid(row=1,column=0,pady=10)

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid(row=1,column=1)

ytdError = Label(root,text="",fg="red")
ytdError.grid(row=2,column=1)

SaveLoc = Label(root,text="Save location : ")
SaveLoc.grid(row=3,column=0)

ytdEntryVar2 = StringVar()
ytdEntry2 = Entry(root,width=50,textvariable=ytdEntryVar2)
ytdEntry2.grid(row=3,column=1)

SaveLocButoon = Button(root,width=10,bg="white",fg="black",text="Browse",command=openLoc)
SaveLocButoon.grid(row=3,column=2,padx=5)

LocationError = Label(root,text="",fg="red")
LocationError.grid(row=4,column=1)

QualityChoose = Label(root,text="Select Quality : ")
QualityChoose.grid(row=5,column=0)

ytdchoices = ttk.Combobox(root,postcommand=AvaQuality)
ytdchoices.grid(row=5,column=1,sticky=W)

DownloadButton = Button(root,text="Download",width=10, bg="red",fg="white",command=DownloadVid)
DownloadButton.grid(row=6,column=1,pady=10)

DownloadError = Label(root,text="",fg="red")
DownloadError.grid(row=7,column=1)

root.mainloop()