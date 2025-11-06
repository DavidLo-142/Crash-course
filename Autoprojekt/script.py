# bei einem Import werden alle nicht eingerückten Zeilen ausgeführt
from klasseauto import autoinfofrage
from klasseauto import infofrage # nur der if __name__ == main block nicht.
# = ist eine wertzuweisung, == ist ein vergleich
quit = False 
while not quit: # not nigiert, while prüft automatisch auf True, not quit ist das gleich wie quit == False
    inputinfo = infofrage()
    quit = autoinfofrage() # wir weisen "quit" die returnvalue von autoinfofrage 