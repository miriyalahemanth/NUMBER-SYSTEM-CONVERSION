from tkinter import *
from tkinter import messagebox
root=Tk()
root.title(" Number  System Conversion ")
root.geometry("1000x700")
def binary():
    messagebox.showinfo("result",bin(num.get()))
        
def decimal():
    messagebox.showinfo("result",num.get())
def octal():
    messagebox.showinfo("result",oct(num.get()))
def hexadecimal():
    messagebox.showinfo("result",hex(num.get()))
    
num =IntVar() 

Label(root,text="NUMBER SYSTEM COVERTOR",font="arial20",bg="black",fg="white").pack(pady=10)
n=Label(root,text="Enter Number",font="arial 15",bg="black",fg="white").place(x=150,y=150)
e1=Entry(root,font="arial 20",textvariable=num).place(x=600,y=150)
button1=Button(root,text="Binary",font="arial 20",bg="green",command=binary)
button1.place(x=200,y=400)
button2=Button(root,text="Decimal",font="arial 20",bg="green",command=decimal).place(x=350,y=400)
button3=Button(root,text="Octal",font="arial 20",bg="green",command=octal).place(x=500,y=400)
button4=Button(root,text="Hexadecimal",font="arial 20",bg="green",command=hexadecimal).place(x=650,y=400)
root.mainloop()
