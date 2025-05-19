from tkinter import *
import subprocess


def submit():
    name=entry.get()

    # Use correct classpath format (Mac/Linux uses ":")
    java_classpath = "/Users/praneelchetlapalli/Desktop/Java Programs:mysql-connector-j-9.2.0.jar"

    # Java command
    java_cmd = ["java", "-cp", java_classpath, "InsertAndFetchData", "test"]

    # Run Java program
    result = subprocess.run(java_cmd, capture_output=True, text=True)

    #result = subprocess.run(["java", "/Users/praneelchetlapalli/Desktop/Java Programs/InsertAndFetchData", name], capture_output=True, text=True)
    print(name)
    print(result)

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