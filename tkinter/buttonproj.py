from tkinter import *

count=0
def click():
    global count
    count+=1
    lab(text=count)
window = Tk()
window.geometry("1200x1200")
window.title("ButtonProj")

b=Button(window,
         text="click",
         font=("Ink Free",80,"bold"),
         bg="#ff6200",
         fg="red",
         activebackground="#ff8533",
         activeforeground="black",
         command=click
         )
lab=Label(window,
          text=count,
          font=("Arial",30,"bold"),
          fg="green",
          )
b.pack()
lab.pack()
window.mainloop()