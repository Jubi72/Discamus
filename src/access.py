import os
import time

"""
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + - - - - - - +
 | Anleitung, fuer die Nutzung der Funktionen der Klasse                                                 | Fortschritt |
 | Autor: Manuel                                                                                         |             |
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + - - - - - - +
 | config() :: gibt die Konfigationen, die in der config.cfg gespeichert sind zurueck                    | TODO 6      |
 | deck_list() :: gibt alle Decks zurueck                                                                | Fertig      |
 | deck_list_info() :: gibt alle Decks mit den Infos zurueck                                             | Fertig      |
 | deck_create(str:name, str:kategorie, str:description) :: erstellt ein Kartenstapel                    | Fertig      |
 | deck_delete(str:dateiname) :: loescht ein Kartenstapel                                                | Fertig      |
 | deck_load(str:dateiname) :: Laden eines Kartenstapels, notwendig um dieses zu nutzen                  | Fertig      |
 | deck_rename(str:newName) :: benennt ein Kartenstapel um                                               | Fertig      |
 |  deck_change_kategorie(str:newKategorie)                                                              | Fertig      |
 |  deck_change_description(str:newDescription)                                                          | Fertig      |
 |  deck_statistik()                                                                                     | TODO        |
 |  deck_statistik_reset()                                                                               | TODO        |
 |  deck_info() :: gibt die Infos des aktuellen Kartenstapels zurueck                                    | Fertig      |
 |  deck_hascard() :: gibt zurueck (true/false), ob das aktuelle Kartendeck noch zulernende Karten hat   | TODO        |
 |  deck_cards() :: gibt alle Karten eines Deckes zurueck (mit id)                                       | TODO 2      |
 |  card_create(str:seite1, str:seite2) :: fuegt zum aktuellen Kartestapel eine Karte hinzu              | TODO 5      |
 |  card_delete(str:id) :: loescht eine Karte                                                            | TODO 6      |
 |  random_card() :: gibt eine zufaellige Karte aus dem geladenen Deck zurueck und loescht diese         | TODO 3      |
 |  last_card() :: gibt die zuletzt ausgegebene Karte zurueck                                            | TODO 4      |
 |  card_correct(str:answer) :: gibt zuruck, ob die Anwort richtig ist                                   | TODO 7      |
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + - - - - - - +
"""

# -*- coding: utf-8 -*-
class funktion:
    def __init__(self):
        self.__deck = str() #Name der Datei des geladenden Decks
        self.__deck_list = list() #Liste der Decks
        self.__deck_cards = list() #Liste aller Karten des Decks (mit ids)
        self.__deck_cards_learn = list() #Liste aller Karten (ohne ids|ohne die gelernten)
        self.__last_card = str() #letzte gelernte Karte
        self.__deck_cards_learned = list() #Liste gelernter Karten mit angabe, ob diese richtig oder falsch geloest wurde
        
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
        Diese Funktion prueft, ob der uebergebene String nur aus zulaessigen Zeichen besteht
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
        dass die laenge erreicht wird. (ein String wird zurueckgegeben)
        """
        anzahlLeerzeichen = laenge-len(str(zahl))
        return max(0, anzahlLeerzeichen)*"0"+str(zahl)
    
    def __timestamp(self):
        """
        Gibt den aktuellen Zeitstempel zurueck
        """
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
        Diese Funktion laed die Infos aus der uebergebenen Datei
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
        Liste: [[dateiname, [name, timestamp, kategorie, AnzahlKarten], ...]
        """
        self.__deck_list_update()
        self.__deck_list_info=[]
        for deck in self.__deck_list:
            self.__deck_list_info.append([deck]+self.__deck_load_info(deck))
        return self.__deck_list_info    
        
    def deck_create(self, name, kategorie, description):
        #TODO: String auf funktionsfaehigkeit ueberpruefen
        """
        Diese Funktion erstellt eine Datei, mit dem namen "name.rna" her, fals noetig: "name_x.rna"
        und dem Inhalt:
        name|timestamp|kategorie|beschreibung
        und updatet die Deck-Liste
        """
        self.__deck_list_update()
        dateiname = name+self.__card_suffix
        #Erstellen des Dateinamens
        if self.__deck_list.count(dateiname)>0:
            i=2
            dateiname = name+"_"+str(i)+self.__card_suffix
            while self.__deck_list.count(dateiname)>0:
                i+=1
                dateiname = name+"_"+str(i)+self.__card_suffix
        #Schreiben in die Datei
        datei = open(self.__deck_dir+dateiname, "w")
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

    def deck_load(self, dateiname):
        #Wenn man mit einem Kartenstapel arbeiten moechte, muss man diese Funktion aufrufen
        """
        Der Deckname (self.__deck) wird auf "dateiname" geaendert und die informationen werden aus der Datei gelesen.
        self.__deck_cards = [[1,[Karte1Vorderseite,Karte1Rueckseite]],[2,[Karte2Vorderseite,Karte2Rueckseite]],...]
        self.__deck_list_learn = [[Karte1Vorderseite,Karte1Rueckseite],...]
        self.__deck_info = [Name, letzterAufruf, Kategorie, anzahlKarten, Lernstand]
        Aufbau der Datei:
        + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        | Name|letzterAufruf|Kategorie|AnzahlKarten|Lernstand[0-100] ::infos ueber den Stapel |
        | Seite1|Seite2|Einseiteig(0)/Zweiseitig(1)|lernstand                                 |
        | Seite1|Seite2|Einseiteig(0)/Zweiseitig(1)|lernstand                                 |
        | ...                                                                                 |
        + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        """
        self.__deck=dateiname
        pass
    
    def deck_rename(self, newName):
        """
        Benennt das geladene Deck um.
        Voraussetzung: Deck muss geladen sein.
        """
        if not self.__deck == newName+self.__card_suffix:
            self.__deck_list_update()
            name = newName
            newName += self.__card_suffix
            #Erstellen des Dateinamens
            if self.__deck_list.count(newName)>0:
                i=2
                newName = name+"_" + str(i) + self.__card_suffix
                while self.__deck_list.count(newName)>0:
                    i+=1
                    newName = name+"_" + str(i) + self.__card_suffix
            os.rename(self.__deck_dir + self.__deck, self.__deck_dir + newName)
            datei=open(self.__deck_dir + newName, "r")
            inhalt = datei.readlines()
            datei.close()
            inhalt[0]= name + inhalt[0][inhalt[0].find("|"):]
            datei = open(self.__deck_dir + newName,"w")
            datei.writelines(inhalt)
            datei.close()
            self.__deck_list_update()

    #Laden des Deckes
    
    def deck_change_kategorie(self, newKategorie):
        datei=open(self.__deck_dir + self.__deck, "r")
        inhalt = datei.readlines()
        datei.close()
        inhalt[0]= inhalt[0][:inhalt[0].find("|")+1] + newKategorie + inhalt[0][inhalt[0].find("|",inhalt[0].find("|")+1):]
        datei = open(self.__deck_dir + self.__deck,"w")
        datei.writelines(inhalt)
        datei.close()
    
    def __deck_new_timestamp(self):
        datei=open(self.__deck_dir + self.__deck + self.__card_suffix, "r")
        inhalt = datei.readlines()
        datei.close()
        inhalt[0] =   inhalt[0][:inhalt[0].find("|", inhalt[0].find("|")+1)+1] \
                    + self.__timestamp() \
                    + inhalt[0][ inhalt[0].find("|", inhalt[0].find("|", inhalt[0].find("|")+1)+1):]
        datei = open(self.__deck_dir + self.__deck + self.__card_suffix,"w")
        datei.writelines(inhalt)
        datei.close()
        
    def deck_change_description(self, newKategorie):
        datei=open(self.__deck_dir + self.__deck + self.__card_suffix, "r")
        inhalt = datei.readlines()
        datei.close()
        inhalt[0] =   inhalt[0][:inhalt[0].find("|", inhalt[0].find("|", inhalt[0].find("|")+1)+1)+1] \
                    + newKategorie \
                    + inhalt[0][inhalt[0].find("|", inhalt[0].find("|", inhalt[0].find("|", inhalt[0].find("|")+1)+1)+1):]
        datei = open(self.__deck_dir + self.__deck + self.__card_suffix,"w")
        datei.writelines(inhalt)
        datei.close()
    
    def deck_info(self):
        """
        Diese Funktion gibt die Infos des Decks zurueck
        Voraussetzung: Deck muss geladen sein (deck_load)
        """
        return self.__deck_load_info(self.__deck) 
    
    def deck_hascards(self):
        """
        Diese Funktion gibt zurueck, ob es noch zulernende Karten gibt
        Voraussetzung: Deck muss geladen sein
        """
        if len(self.__deck_cards_learn)>0:
            return True
        else:
            return False
    
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
        Voraussetzung: Deck muss geladen sein
        """
        pass
        
    def card_delete(self, card_id):
        """
        Diese Funktion loescht die Karte
        Voraussetzung: Deck muss geladen sein
        """
        pass
    
    def random_card(self):
        """
        Diese Funktion waehlt aus dem aktuellen Deck eine zufaellige Karte aus,
        speichert sie (als letzte Karte) und loescht diese aus der __deck_card_learn und gibt diese aus.
        """
        pass
    
    def last_card(self):
        """
        Diese Funktion gibt die letzte Karte, die Variable wurde in random_card erstellt
        """
        return self.__lastcard
    
    def card_correct(self, answer):
        """
        Diese Funktion prueft die Antwort auf die Korrektheit (True oder False)
        und speicher sich das erste Ergebnis
        """
        pass
    
    def config(self):
        """
        Diese Funktion gibt die Konfigationen aus der config datei zurueck oder die Standardeistellungen
        """
        pass
    
    def pruefe_dateipfade(self):
        """
        Diese Funktion prueft, ob alle noetigen Dateipfade existieren, wenn nicht, werden diese hier erstllt
        noetige Dateipfade:
        """
        pass




if __name__=="__main__":
    #Klasse initialisieren
    f = funktion()
    
    #Decklisten aufrufen
    print(f.deck_list())
    print(f.deck_list_info())
    
    #erstellen, umbenennen und loeschen von Kartenstapel
    f.deck_create("Test", "Testdecke", "Testdeck")
    f.deck_create("Test", "Testdecke", "Testdeck")
    print(f.deck_list())
    f.deck_rename(f.deck_list()[-1], "Tolles Testdeck")
    f.deck_change_kategorie(f.deck_list()[-1], "Echt tolles Deck")
    f.deck_new_timestamp("Tolles Testdeck")
    print(f.deck_list())
    f.deck_delete(f.deck_list()[-1])
    f.deck_delete(f.deck_list()[-1])
    print(f.deck_list())
    
    
    f.deck_load(f.deck_list()[0])
    print(f.deck_info())