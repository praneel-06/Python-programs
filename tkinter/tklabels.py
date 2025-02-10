from tkinter import *

window=Tk()
window.geometry("600x600")
window.config(background="black")
emoji = PhotoImage(file="/Users/praneelchetlapalli/Desktop/Python programs/tkinter/image.png")
# emoji = PhotoImage(file="image.png")
label=Label(window,               #declaring a label and its parameters
            text="Damn",
            font=("Arial",50,"italic"),
            background="white",
            fg="red",             #colour of text
            relief=GROOVE,        #border, only groove, flat and ridge works on mac
            bd=10,                #border size of 10 pixels
            padx=10,              #length between edge and border(x)
            pady=10,              #same but in (y) direction
            image = emoji,        #inserts above declared image but replaces text
            compound="left")      #inserts image wrt text      

# label.pack()
label.pack()
window.mainloop()
