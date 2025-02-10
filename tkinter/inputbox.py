from tkinter import *

def submit():
    name=entry.get()
    print(name)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window =Tk()
window.title("Input")
s=Button(text="submit",font=("Arial",30,"bold"),command=submit)
s.pack(side="right")

d=Button(text="delete",font=("Arial",30,"bold"),command=delete)
d.pack(side="right")

b=Button(text="backspace",font=("Arial",30,"bold"),command=backspace)
b.pack(side="right")

entry=Entry()#used for single line inputs by the user
entry=Entry(font=("Helvetica",50,"bold"),
            bg="Green",
            fg="Black",)
#entry.insert(0,"Name")#inserts text before input
#entry.config(show="*")#can be used for passwords, automatically changes input to *
#entry.config(width=40)#can hold 40 characters at a time

entry.pack()
window.mainloop()