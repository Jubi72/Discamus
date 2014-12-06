import os
import time

class funktion:
    def __init__(self):
        self.__deck_list = self.deck_list_update()  #Deckliste wird am Anfang geladen
        self.__deck = str() #Dieser String wird fuer das aktuelle Deck verwendet
        self.__deck_info = list() #Diese Liste beinhaltet die Inforamtionen ueber das aktuelle Deck
        self.__deck_cards = list() #Diese Liste beinhaltet die Karten des aktuellen Deckes
        self.__deck_cards_learning = list() #Diese Liste beinhaltet die Karten des aktuellen Deckes ohne die gelernten
        self.__last_card= str() #Dieser String Beinhaltet die letzte Karte, falls beim Lernen diese nochmal benoetigt wird
        self.__deck_cards_learned = list() #Diese Liste beinhaltet die gelernten Karten und ob sie Richtig oder Falsch beim ersten Versuch angegeben wurden.
        
    #Grundfunktionen, noetig fuer das Programm:
    def str_valid(self, String, max_len=0):
        """
        Diese Funktion prueft, ob der uebergebene String nur Zahlen, Buchstaben (gross, klein),
        einige spezielle (deutsche) sonderzeichen enthaelt, und ob die laenge des Strings stimmt.
        (Bei lenge 0 darf der String beliebig lang sein)
        """
        if(0<max_len<len(String)):
            return False
        for character in String:
            if not 32<=ord(character)<=122:
                return False
        return True
        pass
    
    #Funktionen fuer mehrere Kartenstapel
    def deck_list(self):
        """
        Diese Funktion gibt die Liste aller Kartenstapel zurueck
        Voraussetzung: falls schon laenger nicht getan: deck_list_update noetig.
        """
        return self.__deck_list
    
    def deck_list_update(self):
        """
        Diese Funktion liesst alle Kartenstapel aus und schreibt sie in die Variable self.deck_list
        """
        pass
        
    #Funktionen fuer jeweils ein Kartenstapel
    def deck_create(self, name, kategorie, description):
        """
        Diese Funktion erstellt eine Datei, mit dem namen "name.rna" her, fals noetig: "name_x.rna"
        und dem Inhalt:
        name|timestamp|kategorie|beschreibung
        """
    
    def deck_delet(self, dateiname):
        """
        Diese Funktion löscht das angegebene Deck
        """
        pass
    
    def deck_load_info(self, dateiname):
        #diese Funktion nur beim nicht_laden verwenden
        """
        Diese Funktion laed nur die Infos, 
        damit beim Auflisten der Dateien nur diese Funktion aufgerufen werden muss.
        """
        pass
    
    def deck_load(self, name):
        #Wenn man mit einem Kartenstapel arbeiten moechte, muss mand diese Funktion aufrufen
        """
        Der Deckname (self.__deck) wird auf "name" geaendert und die informationen werden aus der Datei gelesen.
        self.__deck = "Dateiname"
        self.__deck_cards = [[Karte1Vorderseite,Karte1Rueckseite],[Karte2Vorderseite,Karte2Rueckseite],...]
        self.__deck_info = [name, kategorie, letzterAufruf, anzahlKarten, Lernstand]
        Aufbau der Datei:
        + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        | Name|letzterAufruf|AnzahlKarten|Lernstand[0-100] ::infos ueber den Stapel |
        | Vorderseite|Rueckseite|Einseiteig(0)/Zweiseitig(1)|lernstand ::Kartenifos |
        | Vorderseite|Rueckseite|Einseiteig(0)/Zweiseitig(1)|lernstand ::Kartenifos |
        | ...                                                                       |
        + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        """
        pass
    
    def deck_cards(self):
        """
        Diese Funktion gibt die Karten des Decks zurueck und fuegt es einer privaten Liste zurueck
        Voraussetzung: Deck muss geldaden sein (deck_load())
        -Speichert es in zwei variablen fuer random_card()
        """
        return self.__deck_cards
    
    def random_card(self):
        """
        Diese Funktion waehlt aus dem aktuellen Deck eine zufaellige Karte aus,
        speichert sie (als letzte Karte) und loescht diese aus der __deck_card_learn sund gibt diese aus.
        """
        pass
    
    def last_card(self):
        """
        Diese Funktion gibt die letzte Karte, die Variable wurde in random_card erstellt
        """
        return self.__lastcard
    
    def deck_info(self):
        """
        Diese Funktion gibt die Infos des Decks zurueck
        Voraussetzung: Deck muss geladen sein (deck_load oder deck_load_info)
        """
        return self.__deck_info
    
    def pruefe_dateipfade(self):
        """
        Diese Funktion prueft, ob alle noetigen Dateipfade existieren, wenn nicht, werden diese hier erstllt
        noetige Dateipfade:
        %APPDATA%\Rena\
        %APPDATA%\Rena\stapel
        %APPDATA%\Rena\einstellungen
        """
        pass
