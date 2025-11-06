# Klasse definiert
class Auto:
    def __init__(self, inputmarke, inputfarbe, inputhp): 
        self.marke = None
        self.farbe = None
        self.hp = None

Start = (input("Welche Aktion soll ausgeführt werden? \nAuto erstellen oder Programm beenden?"))
if Start == "Auto erstellen":
    print("Ein neues Auto Objekt wurde erstellt.")
    # Objekt erstellt
    auto1 = Auto(inputmarke, inputfarbe, inputhp)
elif Start == "Programm beenden":
    print("Programm wurde beendet.")
    raise SystemExit()


# Fragen nach Eigenschaften
inputmarke = (input("Welche Marke hat das Auto?"))
inputfarbe = (input("Welche Farbe hat das Auto?"))
inputhp = (input("Wie viel HP hat das Auto?"))
# Eigenschaften zum Objekt hinzugefügt
auto1.marke = inputmarke
auto1.farbe = inputfarbe
auto1.hp = inputhp


# Funktion zum beenden des Programms
def closefunk():
    beenden = str(input("Soll das Programm beendet werden? "))
    if beenden == "ja":
        print("Programm wurde beendet.")
        raise SystemExit()
    elif beenden == "nein":
        autoinfofrage()

def infofrage():
    return str(input("Welche Info über das Auto möchtest du?"))

# Funktion für Antwort
def autoinfofrage(auto, inputinfo):
    if inputinfo == "marke":
        print(f"Das Auto ist von der Marke {auto.marke}")
        closefunk()
    elif inputinfo == "farbe":
        print(f"Das Auto ist {auto.farbe}")
        closefunk()
    elif inputinfo == "hp":
        print(f"Das Auto hat {auto.hp} HP.")
        closefunk()
    else:
        print("Es gab ein Problem mit der Eingabe, bitte versuche es nochmal.")
    return False # wird in allen Fällen außer inputinfo == "X" aufgerufen

# warum muss ich auch in diesen block "create auto" aufrufen?
if __name__ == "__main__":
    inputinfo = infofrage()
    autoinfofrage(auto1, inputinfo)

# Aufgabe
# 1. Die frage nach dem programm beenden, als eingene funktion.(Fertig)

# 2. Auto instanzieren in eingene Funktion, damit es nicht beim Import automatisch ausgeführt wird.
#    z.B. bei Eingabe von "objekt erzeugen".(Fertig) 

# 3. Frage nach dem attribut(z.22) aus der Funktion herausziehen und die Antwort als parameter angeben

# 4. Funktionen als Klassenmethoden machen

# Zeilen 8-25 in eine funktion packen