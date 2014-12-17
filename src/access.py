import os
import time

"""
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + - - - - - - +
 | Anleitung, fuer die Nutzung der Funktionen der Klasse                                         | Fortschritt |
 | Autor: Manuel                                                                                 |             |
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + - - - - - - +
 | config() :: gibt die Kofigationen, die in der config.cfg gespeichert sind zurueck             | TODO 6      |
 | deck_list() :: gibt alle Decks zurueck                                                        | Fertig      |
 | deck_list_info() :: gibt alle Decks mit den Infos zurueck                                     | Fertig      |
 | deck_create(str:name, str:kategorie, str:description) :: erstellt ein Kartenstapel            | Fertig      |
 | deck_delete(str:dateiname) :: loescht ein Kartenstapel                                        | Fertig      |
 | deck_load(str:dateiname) :: Laden eines Kartenstapels, notwendig um dieses zu nutzen          | Fertig      |
 |  deck_info() :: gibt die Infos des aktuellen Kartenstapels zurueck                            | Fertig      |
 |  deck_cards() :: gibt alle Karten eines Deckes zurueck (mit id)                               | TODO 1      |
 |  card_create(str:seite1, str:seite2) :: fuegt zum aktuellen Kartestapel eine Karte hinzu      | TODO 4      |
 |  card_delete(str:id) :: loescht eine Karte                                                    | TODO 5      |
 |  random_card() :: gibt eine zufaellige Karte aus dem geladenen Deck zurueck und loescht diese | TODO 2      |
 |  last_card() :: gibt die zuletzt ausgegebene Karte zurueck                                    | TODO 3      |
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + - - - - - - +
"""

# -*- coding: utf-8 -*-
class funktion:
    def __init__(self):
        self.__deck_list = list() #liste der Decks
        self.__deck = str() #Dieser String wird fuer das aktuelle Deck verwendet
        self.__deck_info = list() #Diese Liste beinhaltet die Inforamtionen ueber das aktuelle Deck
        self.__deck_cards = list() #Diese Liste beinhaltet die Karten des aktuellen Deckes mit ids
        self.__deck_cards_learn = list() #Diese Liste beinhaltet die Karten des aktuellen Deckes ohne die gelernten
        self.__last_card = str() #Dieser String Beinhaltet die letzte Karte, falls beim Lernen diese nochmal benoetigt wird
        self.__deck_cards_learned = list() #Diese Liste beinhaltet die gelernten Karten und ob sie Richtig oder Falsch beim ersten Versuch angegeben wurden.
        
        #Dateinamen, ordnernamen, etc
        #Stammverzeichnis
        self.__root_dir = "..\\"
        #    unterverzeichnisse
        self.__data_dir = self.__root_dir + "data\\"
        #        unterverzeicnhisse von "data"
        self.__deck_dir = self.__data_dir + "stapel\\"
        self.__config_dir = self.__data_dir + "config\\"
        #            dateien unter config
        self.__config_file = self.__config_dir + "general.cfg"
        
        #Dateiendungen
        self.__card_suffix = ".rna"
        
    #Grundfunktionen, noetig fuer das Programm:
    def __str_valid(self, String, max_len=0):
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
    
    def __deck_list_update(self):
        """
        Diese Funktion liesst alle Kartenstapel aus und schreibt sie in die Variable self.deck_list
        """
        self.__deck_list=[]
        for datei in os.listdir(self.__deck_dir):
            if len(datei)>4 and datei[-len(self.__card_suffix):-1]+datei[-1]==self.__card_suffix:
                self.__deck_list.append(datei)
 
    def __einrueckenZahl(self, zahl, laenge):
        """
        Diese Funktion schreibt in einem String vor die eingegebene Zahl so viele Nullen,
        dass die laenge erreicht wird.
        """
        anzahlLeerzeichen = laenge-len(str(zahl))
        return max(0, anzahlLeerzeichen)*"0"+str(zahl)
    
    def __timestamp(self):
        lk = time.localtime()
        timestamp  = self.__einrueckenZahl(lk[0],4) #Jahre (laenge 4)
        timestamp += self.__einrueckenZahl(lk[1],2) #Monate (laenge 2)
        timestamp += self.__einrueckenZahl(lk[2],2) #Tage (laenge 2)
        timestamp += self.__einrueckenZahl(lk[3],2) #Stunden (laenge 2)
        timestamp += self.__einrueckenZahl(lk[4],2) #Minuten (laenge 2)
        timestamp += self.__einrueckenZahl(lk[5],2) #Sekunden (laenge 2)
        return timestamp
    
    def __deck_load_info(self, dateiname):
        """
        Diese Funktion laed nur die Infos, 
        damit beim Auflisten der Dateien nur diese Funktion aufgerufen werden muss.
        """
        datei = open(self.__deck_dir+dateiname, "r")
        inhalt = datei.readlines()[0]
        info = inhalt.split("|")
        datei.close()
        info[-1]=info[-1].replace("\n", "")
        return info
    
    def __deck_cards_load(self):
        """
        Diese Funktion laed die Karten aus der Datei
        Voraussetzung: deck_load muss erfolgt sein
        """
        pass

    def deck_list(self):
        """
        Diese Funktion gibt die Liste aller Kartenstapel zurueck
        """
        self.__deck_list_update()      
        return self.__deck_list
    
    def deck_list_info(self):
        """
        Diese Funktion gibt die Liste aller Kartenstapel mit Infos zurueck
        Keine Voraussetzungen
        Liste: [[dateiname, name, fortschritt, ...],[]
        """
        self.__deck_list_update()
        self.__deck_list_info=[]
        for deck in self.__deck_list:
            self.__deck_list_info.append([deck]+self.__deck_load_info(deck))
        return self.__deck_list_info    
        
    def deck_create(self, name, kategorie, description):
        """
        Diese Funktion erstellt eine Datei, mit dem namen "name.rna" her, fals noetig: "name_x.rna"
        und dem Inhalt:
        name|timestamp|kategorie|beschreibung
        und updatet die Deck-Liste
        """
        self.__deck_list_update()
        dateiname = name+self.__card_suffix
        #Erstellen des Dateinamens
        if dateiname in self.__deck_list:
            i=2
            dateiname = name+"_"+str(i)+self.__card_suffix in self.__deck_list
            while dateiname in self.__deck_list:
                i+=1
                dateiname = name+"_"+str(i)+self.__card_suffix in self.__deck_list
        #Schreiben in die Datei
        datei = os.open(self.__deck_dir+dateiname, "r")
        timestamp =self.__timestamp()
        datei.write(name+"|"+kategorie+"|"+timestamp+"|"+kategorie+"|"+description)
        datei.close()
        self.__deck_list_update()
    
    def deck_delete(self, dateiname):
        """
        Diese Funktion loescht das angegebene Deck und updatet die Deck-Liste
        """
        self.__deck_list_update()
        if dateiname in self.__deck_list:
            os.remove(self.__deck_dir+dateiname)
        self.__deck_list_update()
    
    #Laden des Deckes
    
    
    def deck_load(self, dateiname):
        #Wenn man mit einem Kartenstapel arbeiten moechte, muss man diese Funktion aufrufen
        """
        Der Deckname (self.__deck) wird auf "name" geaendert und die informationen werden aus der Datei gelesen.
        self.__deck = "Dateiname"
        self.__deck_cards = [[Karte1Vorderseite,Karte1Rueckseite],[Karte2Vorderseite,Karte2Rueckseite],...]
        self.__deck_info = [name, kategorie, letzterAufruf, anzahlKarten, Lernstand]
        Aufbau der Datei:
        + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        | Name|letzterAufruf|AnzahlKarten|Lernstand[0-100] ::infos ueber den Stapel |
        | id|Seite1|Seite2|Einseiteig(0)/Zweiseitig(1)|lernstand ::Kartenifos       |
        | id|Seite1|Seite2|Einseiteig(0)/Zweiseitig(1)|lernstand ::Kartenifos       |
        | ...                                                                       |
        + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        """
        self.__deck=dateiname
        pass
    
    def deck_info(self):
        """
        Diese Funktion gibt die Infos des Decks zurueck
        Voraussetzung: Deck muss geladen sein (deck_load oder deck_load_info)
        """
        return self.__deck_load_info(self.__deck) 
        
    
    def deck_cards(self):
        """
        Diese Funktion gibt alle Karen eines Decks mit ids zurueck.
        [id,[Seite1, Seite2], id2, [Seite1, Seite2],...]
        """
        pass
        return self.__deck_cards
    
    def card_create(self, Seite1, Seite2):
        """
        Diese Funktion fuegt die Karte hinzu
        """
        
    def card_delete(self, card_id):
        """
        Diese Funktion loescht die Karte
        """
    
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
    
    
    def config(self):
        """
        Diese Funktion gibt die Konfigationen aus der config datei zurueck oder die Standardeistellungen
        """
    
    def pruefe_dateipfade(self):
        """
        Diese Funktion prueft, ob alle noetigen Dateipfade existieren, wenn nicht, werden diese hier erstllt
        noetige Dateipfade:
        """
        pass

if __name__=="__main__":
    f = funktion()
    deck_list = f.deck_list()
    print(deck_list)
    deck_list_info = f.deck_list_info()
    print(deck_list_info)
    print(deck_list[0])
    f.deck_load(deck_list[0])
    print(f.deck_info())
