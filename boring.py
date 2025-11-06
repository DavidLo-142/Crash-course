from tkinter import *
import random

def move_label():
    random_x = random.randint(0, 250)
    random_y = random.randint(0, 250)
    label.place(x=100, y=100)
    label.place(x=random_x, y=random_y)



root = Tk(screenName="Boring Project")
root.geometry("250x250+500+250")

label = Label(root, text="Ä")

button = Button(root, text="Move", command=move_label)
button.pack()

root.mainloop()