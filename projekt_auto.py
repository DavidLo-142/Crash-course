class Auto:

    total_cars = 0

    def __init__(self, marke, farbe, hp):
        self.marke = marke
        self.farbe = farbe
        self.hp = hp
        Auto.total_cars += 1


def build_decision():
    command = input("Auto erstellen oder Programm beenden?")
    if command == "Auto erstellen":
        build_car_command()
    if command == "Programm beenden":
        print("Programm beendet.")
        raise SystemExit()
    
def close_command(auto, marke, farbe, hp):
    close = input("Gibt es weitere Fragen?")
    if close == "Ja":
        question_command(auto, marke, farbe, hp)
    elif close == "nein":
        print("Programm beendet.")
        raise SystemExit()

def question_command(auto, marke, farbe, hp):
    while True:
        auto = Auto(marke, farbe, hp)
        command = input("Welche Info über das Auto?")
        if command == "marke":
            print(f"Das Auto ist von der marke: {auto.marke}")
            close_command(auto, marke, farbe, hp)
        elif command == "farbe":
            print(f"Das Auto ist {auto.farbe}")
            close_command(auto, marke, farbe, hp)
        elif command == "hp":
            print(f"Das Auto hat {auto.hp} hp.")
            close_command(auto, marke, farbe, hp)
        elif command == "X":
            print("Programm beendet.")
            raise SystemExit()

def build_car_command():
    marke = input("Welche Marke hat das Auto?")
    farbe = input("Welche Farbe hat das Auto?")
    hp = input("Wie viel Hp hat das Auto?")
    auto = Auto(marke, farbe, hp)
    question_command(auto, marke, farbe, hp)

print("Welche Aktion soll ausgeführt werden?")
build_decision()