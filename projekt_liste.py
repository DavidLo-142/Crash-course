# Trying to make a list with elements that can be added by input of the user.
# In the end, the system should be able to print out how many elements are in the list and
# what they are called.
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from pydantic import BaseModel

# Fenster
def create_window():

    def hinzuf():
        text = entry1.get()
        hinzuf_button.config(relief=SUNKEN)
        hinzuf_button.after(100, lambda: hinzuf_button.config(relief=RAISED))
        if text:
            liste.append(text)
            label3.config(
                text="Liste: " + ", ".join(liste),
            )
            entry1.delete(0, END)

    def beenden():

        checked = [BooleanVar(value=False) for _ in liste]
        
        def save():
            files = [('Text Document', '*.pdf')]
            file = asksaveasfilename(filetypes = files, defaultextension = ".pdf")
            with open(file, "w") as f:
                for element in liste:
                   f.write("%s\n" %element)
            f.close()

        def delete(index):
            del liste[index]
            refresh()

        def swapup(index):
            liste[index], liste[index-1] = liste[index-1], liste[index]
            checked[index], checked[index-1] = checked[index-1], checked[index]
            refresh()

        def swapdown(index):
            liste[index], liste[index+1] = liste[index+1], liste[index],
            checked[index], checked[index+1] = checked[index+1], checked[index]
            refresh()

        labelitems = entry1.get()
        zwischenfenster.destroy()
        endfenster = Tk()
        endfenster.title("Ihre Liste")
        endfenster.geometry("130x200+300+120")
        
        labelitems = Label(endfenster, text="Liste")
        labelitems.config(font=("Arial", 15))
        labelitems.grid(row=0, column=0)

        speichern = Button(endfenster, text="√", command=save)
        speichern.grid(row=0, column=1)

        list_frame = Frame(endfenster)
        list_frame.grid(row=1, column=0, columnspan=5)

        def refresh():
            # Clear all widgets in list_frame
            for widget in list_frame.winfo_children():
                widget.destroy()

            # Recreate the list display
            for i, element in enumerate(liste):
                label = Label(list_frame, text=element)
                label.grid(row=i, column=2)

                kasten = Checkbutton(list_frame, variable=checked[i])
                kasten.grid(row=i, column=3)

                upbutton = Button(list_frame, text="↑", command=lambda idx=i: swapup(idx))
                upbutton.grid(row=i, column=0)
                upbutton.config(height=1, width=1)

                downbutton = Button(list_frame, text="↓", command=lambda idx=i: swapdown(idx))
                downbutton.grid(row=i, column=1)
                downbutton.config(height=1, width=1)

                remove_button = Button(
                    list_frame, text="x", command=lambda idx=i: delete(idx))
                remove_button.grid(row=i, column=4)
                remove_button.config(height=1, width=1)

        refresh()

#----------------------------------- Elementfenster ---------------------------------------

    def return_funktion(event):
        hinzuf_button.invoke()

    start_fenster.destroy()
    zwischenfenster = Tk()
    zwischenfenster.title("Listen Tool")
    zwischenfenster.geometry("300x150+300+120")
    label1 = Label(zwischenfenster, text="Eine Liste wurde für sie erstellt.")
    label1.place(x=60, y=0)

    label2 = Label(
        zwischenfenster, text="Welches Element möchtest du der Liste hinzufügen: ")
    label2.place(x=10, y=20)
    

    entry1 = Entry(zwischenfenster)
    entry1.place(x=50, y=45)

    hinzuf_button = Button(zwischenfenster, text="Hinzufügen", command=hinzuf)
    hinzuf_button.place(x=180, y=40)

    label3 = Label(zwischenfenster, text="Liste: ")
    label3.place(x=50, y=70)

    button2 = Button(zwischenfenster, text="Fertig", command=beenden)
    button2.place(x=130, y=95)

    zwischenfenster.bind("<Return>", return_funktion)

#----------------------------------- Startfenster ---------------------------------------
def close_window():
    raise SystemExit()


if __name__ == "__main__":
    liste = []
    start_fenster = Tk()
    start_fenster.title("Listen Tool")
    start_fenster.geometry("300x150+300+120")

    w = Label(start_fenster, text="Bitte wählen sie eine Aktion.")
    w.place(x=70, y=0)

    button1 = Button(start_fenster, text="Liste erstellen", command=create_window)
    button1.place(x=50, y=30)

    button2 = Button(start_fenster, text="Programm beenden", command=close_window)
    button2.place(x=140, y=30)

    start_fenster.mainloop()