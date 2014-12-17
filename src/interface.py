import access
from gui import *

# # # # # Todo # # # # #
# - mainmenu           #
# - statistik          #
# # # # # #  # # # # # #

### initialisieren
gui = gui("discamus", 600, 400, "black", "orange", True)
acc = access.funktion()

testen = False # Bei testen = True wird getestet, ansonsten nur gelernt

### alle Menus erstellen ?

### Hauptmenu anzeigen
gui.show_mainmenu()

def lernen_start(deck):
    acc.deck_load(deck)
    if acc.deck_hascard():
        gui.hide_mainmenu() #oder aktuelles am besten waere Funktion: hide_currentmenu()
        gui.show_lernmenu(acc.random_card)
    else:
        gui.hide_mainmenu()
        gui.show_auswertung(acc.statistik())

def lernen_fortsetzung(antwort):
    if acc.deck_hascards():
        if acc.card_correct(antwort):
            gui.hide_lernmenu()
            gui.show_lernmenu(acc.last_card)
        else:
            gui.hide_lernmenu()
            gui.show_lernmenu(acc.random_card)
    else:
        gui.hide_mainmenu()
        gui.show_auswertung(acc.statistik())

def testen_start(deck):
    acc.deck_load(deck)
    if acc.deck_hascard():
        gui.hide_mainmenu() #oder aktuelles am besten waere Funktion: hide_currentmenu()
        gui.show_lernmenu(acc.random_card)
    else:
        gui.hide_mainmenu()
        gui.show_auswertung(acc.statistik())

def testen_fortsetzung(antwort):
    if acc.deck_hascards():
        acc.card_correct(antwort)
        gui.hide_lernmenu()
        gui.show_lernmenu(acc.random_card)
    else:
        gui.hide_mainmenu()
        gui.show_auswertung(acc.statistik())

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
