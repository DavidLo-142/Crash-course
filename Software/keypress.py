from tkinter import *

root = Tk()
root.title("WASD")

# WASD Code
def wpressed():
    print("w")
    wbutton.config(relief=SUNKEN)
    wbutton.after(100, lambda: wbutton.config(relief=RAISED))

def apressed():
    print("a")
    abutton.config(relief=SUNKEN)
    abutton.after(100, lambda: abutton.config(relief=RAISED))

def spressed():
    print("s")
    sbutton.config(relief=SUNKEN)
    sbutton.after(100, lambda: sbutton.config(relief=RAISED))

def dpressed():
    print("d")
    dbutton.config(relief=SUNKEN)
    dbutton.after(100, lambda: dbutton.config(relief=RAISED))


wbutton = Button(root, text="W", command=wpressed)
wbutton.grid(row=0, column=1)
wbutton.config(height=4, width=10)

abutton = Button(root, text="A", command=apressed)
abutton.grid(row=1, column=0)
abutton.config(height=4, width=10)

sbutton = Button(root, text="S", command=spressed)
sbutton.grid(row=1, column=1)
sbutton.config(height=4, width=10)

dbutton = Button(root, text="D", command=dpressed)
dbutton.grid(row=1, column=2)
dbutton.config(height=4, width=10)

def on_keypressw(event):
    if event.keysym== "w":
        wbutton.invoke()

def on_keypressa(event):
    if event.keysym== "a":
        abutton.invoke()

def on_keypresss(event):
    if event.keysym== "s":
        sbutton.invoke()

def on_keypressd(event):
    if event.keysym== "d":
        dbutton.invoke()

root.bind("<KeyPress-w>", on_keypressw)
root.bind("<KeyPress-W>", on_keypressw)

root.bind("<KeyPress-a>", on_keypressa)
root.bind("<KeyPress-A>", on_keypressa)

root.bind("<KeyPress-s>", on_keypresss)
root.bind("<KeyPress-S>", on_keypresss)

root.bind("<KeyPress-d>", on_keypressd)
root.bind("<KeyPress-D>", on_keypressd)

# MAUS Code
def lpressed():
    print("left")
    lclickbutton.config(relief=SUNKEN)
    lclickbutton.after(100, lambda: lclickbutton.config(relief=RAISED))   

def rpressed():
    print("right")
    rclickbutton.config(relief=SUNKEN)
    rclickbutton.after(100, lambda: rclickbutton.config(relief=RAISED))

lclickbutton = Button(root, text="L", command=lpressed)
lclickbutton.grid(row=0, column=4)
lclickbutton.config(height=4, width=10)

rclickbutton = Button(root, text="R", command=rpressed)
rclickbutton.grid(row=0, column=5)
rclickbutton.config(height=4, width=10)

def on_keypressmouse(event):
    if event.num == 1:
        lclickbutton.invoke()
    elif event.num == 3:
        rclickbutton.invoke()

root.bind("<Button>", on_keypressmouse)

root.mainloop()