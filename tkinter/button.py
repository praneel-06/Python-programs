from tkinter import *


def click():
    count=count+1
    print(count)



window = Tk()
window.geometry("600x600")
window.title("damn")
# window.config(bg="white")

button = Button(window,
                text="click meee!!",
                font=("Ink Free", 50, "bold"),
                bg="#ff6200",  # Background color
                fg="red",  # Text color
                activebackground="#ff8533",  # Background when pressed
                activeforeground="black",  # Text color when pressed
                relief="flat",  # Remove native styling
                command=click) # Attach the function to the button
                #state=DISABLED) #disables button usage
button.pack()

window.mainloop()
