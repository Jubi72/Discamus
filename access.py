import os
import time

class funktion:
    def __init__(self):
        self.__deck_list = self.deck_list_update() #
        self.__deck = str()
        self.__deck_info = list()
        self.__deck_cards = list()
        
    #Grundfunktionen, noetig fuer das Programm:
    def str_valid(self, String, max_len=0):
        """
        Diese Funktion prueft, ob der uebergebene String nur Zahlen, Buchstaben (gross, klein),
        einige spezielle (deutsche) sonderzeichen enthaelt, und ob die laenge des Strings stimmt.
        (Bei lenge 0 darf der String beliebig lang sein)
        """    
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
        Diese Funktion gibt die Karten des Decks zurueck
        """
        return self.__deck_cards
    
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
