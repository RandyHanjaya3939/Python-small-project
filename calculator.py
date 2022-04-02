from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("360x380")

def insertval(number):
    global operators
    operators = operators + str(number)
    value.set(operators)

def clr():
    global operators
    operators = ""
    value.set(operators)

def result():
    global operators
    hasil = eval(str(operators))
    value.set(hasil)
    operators = ""

operators = ""
value = StringVar()
Input = Entry(root,font=("",20,'bold'), textvariable=value,insertwidth=4, bd=30,justify='right').grid(columnspan=4)

Btn1 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=1,command=lambda:insertval(1)).grid(row=3,column=0)

Btn2 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=2,command=lambda:insertval(2)).grid(row=3,column=1)

Btn3 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=3,command=lambda:insertval(3)).grid(row=3,column=2)

Btn4 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=4,command=lambda:insertval(4)).grid(row=2,column=0)

Btn5 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=5,command=lambda:insertval(5)).grid(row=2,column=1)

Btn6 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=6,command=lambda:insertval(6)).grid(row=2,column=2)

Btn7 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=7,command=lambda:insertval(7)).grid(row=1,column=0)

Btn8 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=8,command=lambda:insertval(8)).grid(row=1,column=1)

Btn9 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=9,command=lambda:insertval(9)).grid(row=1,column=2)

Btn0 = Button(root,padx=16,font=("",20,'bold'),bd=8,text=0,command=lambda:insertval(0)).grid(row=4,column=0)

Btnclr = Button(root,padx=16,font=("",20,'bold'),bd=8,text='C',command=lambda:clr()).grid(row=4,column=1)

Btnequ = Button(root,padx=16,font=("",20,'bold'),bd=8,text='=',command=lambda:result()).grid(row=4,column=2)



Plus = Button(root,padx=16,font=("",20,'bold'),bd=8,text='+',command=lambda:insertval('+')).grid(row=1,column=3)
Minus = Button(root,padx=16,font=("",20,'bold'),bd=8,text='-',command=lambda:insertval('-')).grid(row=2,column=3)
Times = Button(root,padx=16,font=("",20,'bold'),bd=8,text='*',command=lambda:insertval('*')).grid(row=3,column=3)
Subs = Button(root,padx=16,font=("",20,'bold'),bd=8,text='/',command=lambda:insertval('/')).grid(row=4,column=3)


root.mainloop()