from accesses import *
from gui import *

# # # # # Todo # # # # #
# - mainmenu           #
# - statistik          #
# # # # # #  # # # # # #

### initialisieren
gui = GUI("discamus", 600, 400, "black", "orange", True)
acc = funktion()

lern_oder_test = "lern"

### alle Menus erstellen ?

### Hauptmenu anzeigen
gui.show_mainmenu()
"""
def start_lernen(deck):
    # Deck eingelesen, das Lernen kann beginnen
    gui.show_lernmenu()
    acc.deck_load(deck)
    while(acc.deck_info[1] != 0):
        # Funktion sollte eine Liste [frage, loesgun] zurueckgeben
        frage_lsg = acc.frage(deck)
        richtung = 1 # irgendwie noch die Richtung per GUI abfragen lassen
        if(richtung == 1):
            frage = frage_lsg[0]
            loesung = frage_lsg[1]
        else:
            frage = frage_lsg[1]
            loesung = frage_lsg[0]
        # Funktion soll User-Antwort returnen
        antwort = gui.frage(frage) # sozusagen warten bis Antwort kommt
        # Funktion soll fuer sich exakten Wert (z.B. "3/7") abspeichern (fuer Statistik),
        # aber True oder False returnen (kompelett richtig o. nicht)
        x = richtig_falsch(loesung,antwort)
        gui.gib_loesung(loesung,x)
        if(x == True):
            # delete card
    # Lernen fertig
"""        
def lernen_a(deck, x):
    if(acc.deck_info[1] == 0):
        if(x):
            frage_lsg = acc.random_card()
        else:
            frage_lsg = acc.last_card()
        richtung = 1 # vielleicht durch GUI abfragen lassen
        if(richtung == 1):
            frage = frage_lsg[0]
            loesung = frage_lsg[1]
        else:
            frage = frage_lsg[1]
            loesung = frage_lsg[0]
        gui.show_lernmenu_a(frage)
    else:
        # Deck "leer"
        gui.hide_lernmenu_a()
        gui.show_auswertung(acc.erfolg())

def lernen_b(antwort):
    # Funktion soll fuer sich exakten Wert (z.B. "3/7") abspeichern (fuer Statistik),
    # aber True oder False returnen (kompelett richtig o. nicht)
    x = acc.richtig_falsch(loesung,antwort)
    gui.gib_loesung(loesung,x)
    #gui.show_lernmenu_b()



def start_testen(deck, antwort):
    if(antwort != "erste Runde"):
        # Funktion soll fuer sich exakten Wert (z.B. "3/7") abspeichern (fuer Statistik),
        # aber True oder False returnen (kompelett richtig o. nicht)
        acc.richtig_falsch(loesung,antwort)
        # delete card
    if(acc.deck_info[1] != 0):
        # Funktion sollte eine Liste [frage, loesung] zurueckgeben
        frage_lsg = acc.random_card(deck)
        richtung = 1 # irgendwie noch die Richtung per GUI abfragen lassen
        if(richtung == 1):
            frage = frage_lsg[0]
            loesung = frage_lsg[1]
        else:
            frage = frage_lsg[1]
            loesung = frage_lsg[0]
        gui.show_testmenu(frage)
        # Funktion soll User-Antwort returnen
    else:
        # Deck "leer"
        gui.hide_testmenu()
        gui.show_auswertung(acc.erfolg())

def decks_ansicht_test():
    gui.hide_mainmenu()
    # Funktion gibt alle Decks an die GUI, wenn "Testen" angeklickt wurde
    gui.show_deckmenu(acc.deck_list())
    lern_oder_test = "test"

def decks_ansicht_lern():
    gui.hide_mainmenu()
    # Funktion gibt alle Decks an die GUI, wenn "Lernen" angeklickt wurde
    gui.show_deckmenu(acc.deck_list())
    lern_oder_test = "lern"

def deck_ausgewaehlt(deck):
    # Deck ausgewählt, Lernen bzw. Testen kann beginnen
    if(lern_oder_test == "lern"):
        gui.hide_deckmenu()
        acc.deck_load(deck)
        lernen_a(deck, True)
    else:
        gui.hide_deckmenu()
        acc.deck_load(deck)
        start_testen(deck)

def editor_quit():
    # Editor beendet
    gui.hide_editor()
    gui.show_mainmenu()

def editor_next(a,b):
    # neues Element zum Editor hinzufuegen
    acc.editor_write(a,b)
    
def editor():
    gui.hide_mainmenu()
    # noch Dateinamen herausbekommen
    gui.show_editor()

def statistik():
    gui.hide_mainmenu()
    gui.show_statistik(acc.statistik())
    # vielleicht per Klick auf Kartenstapel explizite Statistik

def mainmenu():
    # das offene Menü schliessen
    gui.show_mainmenu()
    
def hilfe():
    gui.hide_mainmenu()
    gui.show_hilfe()

def optionen():
    gui.hide_mainmenu()
    gui.show_optionen()

def beenden():
    gui.quit_window()