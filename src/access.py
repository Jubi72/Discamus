# -*- coding: utf-8 -*-
import os
import time
import random

"""
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
 | Anleitung, fuer die Nutzung der Funktionen der Klasse                                                 |
 | Autor: Manuel                                                                                         |
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
 | set_config(str:var, int/var:value) :: speichert den value in einer Datei ab                           |
 | get_config(str:var) :: liesst aus einer Datei einen Wert aus                                          |
 | deck_list() :: gibt alle Decks zurueck                                                                |
 | deck_list_info() :: gibt alle Decks mit den Infos zurueck                                             |
 | deck_create(str:name, str:kategorie, str:description) :: erstellt ein Kartenstapel                    |
 | deck_delete(str:dateiname) :: loescht ein Kartenstapel                                                |
 | deck_load(str:dateiname) :: Laden eines Kartenstapels, notwendig um dieses zu nutzen                  |
 |  deck_rename(str:newName) :: benennt ein Kartenstapel um                                              |
 |  deck_change_kategorie(str:newKategorie)                                                              |
 |  deck_change_description(str:newDescription)                                                          |
 |  deck_statistik() ::gibt die falsch gentworteten karten zurueck                                       |
 |  deck_statistik_reset() :: setzt die Statistik zurueck                                                |
 |  deck_info() :: gibt die Infos des aktuellen Kartenstapels zurueck                                    |
 |  deck_hascard() :: gibt zurueck (true/false), ob das aktuelle Kartendeck noch zulernende Karten hat   |
 |  deck_cards() :: gibt alle Karten eines Kartenstapels zurueck (mit id)                                |
 |  card_create(str:seite1, str:seite2) :: fuegt zum aktuellen Kartestapel eine Karte hinzu              |
 |  card_delete(int:id) :: loescht eine Karte                                                            |
 |  card_change(int:id, str:Seite1 = "", str:Seite2 = "") :: aendert den Karteninhalt                    |
 |  card_toggle_double_sided(int:id) :: aendert von Doppelseitig auf einseitg und andersherum            |
 |  random_card() :: gibt eine zufaellige Karte aus dem geladenen Kartenstapel zurueck und loescht diese |
 |  last_card() :: gibt die zuletzt ausgegebene Karte zurueck                                            |
 |  card_correct(str:answer) :: gibt zuruck, ob die Anwort richtig ist                                   |
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
"""

class funktion:
    def __init__(self):
        self.__deck = str() #Name der Datei des geladenden Decks
        self.__deck_list = list() #Liste der Decks
        self.__deck_cards_loaded = False #Ob schon die Karten des Deckes geladen wurden.
        self.__deck_card_answered = False #Anwort schon gegeben oder nicht
        self.__deck_cards = list() #Liste aller Karten des Decks (mit ids)
        self.__deck_cards_learn = list() #Liste aller Karten (ohne ids|ohne die gelernten)
        self.__last_card = str() #letzte gelernte Karte
        self.__deck_cards_learned = list() #Liste gelernter Karten mit Angabe, ob diese richtig oder falsch geloest wurde
        
        self.__file_separator = "|" *2 #der Separator in den Dateien
        self.__deck_begin_statistik = "00" #Mit welcher Statistik die einzelenen Karten beginnen
        self.__deck_statistik_max_len = 6
        self.__deck_card_id=int()
        self.__numberOfCards=0
        
        #Dateinamen, Ordnernamen, etc
        #Stammverzeichnis
        self.__root_dir = "..\\"
        #    Unterverzeichnisse
        self.__data_dir = self.__root_dir + "data\\"
        #        Unterverzeicnhisse von "data"
        self.__deck_dir = self.__data_dir + "stapel\\"
        self.__config_dir = self.__data_dir + "config\\"
        #            Dateien unter config
        self.__config_suffix = ".cfg"
        
        #Dateiendungen
        self.__card_suffix = ".rna"
        
        self.__pruefe_dateipfade()

    #Grundfunktionen, noetig fuer das Programm:
    
    def __string_lenght(self, String, min_length, max_length):
        """
        Funktion prueft, ob der String die richtige Laenge hat
        """
        if(min_length<=len(String)<=max_length):
            return True
        return False
    
    def __str_make_valid(self, String):
        """
        Diese Funktion aendert den String so, dass er nicht die Funktion des Programmes beeintraechtigt
        """
        valid_str = String.replace(self.__file_separator[0], "<"+self.__file_separator[0]+">")
        return valid_str
    
    def __str_make_normal(self, String):
        """
        Diese Funktion ist die Gegenfunktion von self.__str_make_valid(...)
        Der String wird wieder fuer den Benutzer lesbar gemacht.
        """
        normal_str = String.replace("<"+self.__file_separator[0]+">", self.__file_separator[0])
        return normal_str
    
    def __str_make_valid_filename(self, string):
        """
        Diese Funktion entfernt alle unzulaessigen Zeichen aus eines Dateinamen aus dem String
        """
        dateiname = string.replace("\\","")
        dateiname = dateiname.replace("/","")
        dateiname = dateiname.replace(":","")
        dateiname = dateiname.replace("*","")
        dateiname = dateiname.replace("?","")
        dateiname = dateiname.replace("\"","")
        dateiname = dateiname.replace("<","")
        dateiname = dateiname.replace(">","")
        dateiname = dateiname.replace("|","")
        return dateiname
    
    def __file_string_change_cell(self, string, newCellContent, cellNumber):
        newString = string.split(self.__file_separator)
        newString[cellNumber] = newCellContent
        newLine = newString[0]
        for elem in newString[1:]:
            newLine+=self.__file_separator+str(elem)
        return newLine
    
    def __deck_list_update(self):
        """
        Diese Funktion liesst alle Kartenstapel aus und schreibt sie in die Variable self.deck_list
        """
        self.__deck_list=[]
        for datei in os.listdir(self.__deck_dir):
            if len(datei)>=len(self.__card_suffix) and datei[-len(self.__card_suffix):-1]+datei[-1]==self.__card_suffix:
                self.__deck_list.append(datei)
        
        self.__deck_list_info=[]
        for deck in self.__deck_list:
            deck_info=self.__deck_load_info(deck)
            self.__deck_list_info.append(deck_info[:3]+deck_info[4:])

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
        datei = open(self.__deck_dir+dateiname, "r", encoding='utf8')
        inhalt = datei.readlines()[0]
        info = inhalt.split(self.__file_separator)
        for i in range(len(info)):
            info[i] = self.__str_make_normal(info[i])
        datei.close()
        info[-1]=info[-1].replace("\n", "")
        return info
    
    def __calc_statistik(self, string):
        percent=0
        if len(string)>0:
            percent=string.count("1")*100//len(string)
        return percent
            
    
    def __deck_cards_load(self):
        """
        Diese Funktion laed die Karten aus der Datei in die Listen
        und setzt die Variable self.__deck_cards_loaded auf True
        Voraussetzung: deck_load muss erfolgt sein
        """
        datei = open(self.__deck_dir + self.__deck, encoding='utf8')
        karten = datei.readlines()[1:]
        self.__deck_cards = list()
        self.__deck_cards_learn = list()
        self.__deck_cards_learned = list()
        self.__deck_cards_loaded = True
        self.__numberOfCards=0
        for i in range(len(karten)):
            karte = karten[i].split(self.__file_separator)
            karte[-1]=karte[-1][:-1] #Entfernen des \n am Ende des Strings
            for j in range(len(karte)):
                karte[j] = self.__str_make_normal(karte[j])
            self.__deck_cards.append([karte[0]]+[karte[1]]+[karte[2]]+[self.__calc_statistik(karte[3])])
            self.__deck_cards_learned.append([karte[0],karte[1],[],karte[-1]])
            self.__numberOfCards+=1
            if karte[2]=="0":
                self.__deck_cards_learn.append([i, karte[0],karte[1]])
            elif karte[2]=="1":
                self.__deck_cards_learn.append([i, karte[1],karte[0]])
            elif karte[2]=="2":
                self.__deck_cards_learn.append([i, karte[0],karte[1]])
                self.__deck_cards_learn.append([i, karte[1],karte[0]])
                self.__numberOfCards+=1
                
    
    def __quick_sort_verkleiner(self, liste, sort):
        """
        Unterfunktion von Quicksort
        """
        liste_kleiner=[]
        liste_groesser=[]
        if len(liste)>0:
            pivot=liste[0]
        else:
            pivot=str()
        if sort>0:
            for elem in liste[1:]:
                if elem[abs(sort)].lower()<pivot[abs(sort)].lower():
                    liste_kleiner.append(elem)
                else:
                    liste_groesser.append(elem)
        else:
            for elem in liste[1:]:
                if elem[abs(sort)].lower()>pivot[abs(sort)].lower():
                    liste_kleiner.append(elem)
                else:
                    liste_groesser.append(elem)
        return [liste_kleiner,pivot,liste_groesser]
    
    def __quick_sort(self, liste, sort):
        """
        Quicksort (schnelles Sortierverfahren)
        """
        if liste==[]:
            return []
        else:
            elems=self.__quick_sort_verkleiner(liste, sort)
            kleiner=self.__quick_sort(elems[0], sort)
            groesser=self.__quick_sort(elems[2], sort)
            return kleiner + [elems[1]] + groesser
    
    def __deck_sort(self, sort, info = True):
        """
        Diese Funktion Sortiert die Liste. Positive Zahlen vorwaerts, negative Zahlen rueckwaerts.
        Zahlen von 1-6 (-1 - -5)
        1 Name
        2 Kategorie
        3 Timestamp
        4 Karten
        5 Lernstand
        """
        full_deck_list=[]
        for i in range(len(self.__deck_list)):
            full_deck_list.append([self.__deck_list[i]]+self.__deck_list_info[i][:])
        full_deck_list = self.__quick_sort(full_deck_list, sort)
        self.__deck_list_info_sort = []
        self.__deck_list_sort = []
        for elem in full_deck_list:
            self.__deck_list_sort += [elem[0]]
            self.__deck_list_info_sort += [elem [1:]]
        if info:
            return self.__deck_list_info_sort
        else:
            return self.__deck_list_sort
    
    def deck_list(self, sort=0):
        """
        Diese Funktion gibt die Liste aller Kartenstapel zurueck
        """
        self.__deck_list_update()
        if sort==0:
            return self.__deck_list
        else:
            return self.__deck_sort(sort, False)
    
    def deck_list_info(self, sort=0):
        """
        Diese Funktion gibt die Liste aller Kartenstapel mit Infos zurueck
        Liste: [[name,kategorie, timestamp, AnzahlKarten, Lernstand], ...]
        """
        self.__deck_list_update()
        if sort==0:
            return self.__deck_list_info
        else:
            return self.__deck_sort(sort)
        
    def deck_list_noUpdate(self, sort=0):
        """
        Diese Funktion gibt die Liste aller Kartenstapel zurueck
        """
        if sort==0:
            return self.__deck_list
        else:
            return self.__deck_sort(sort, False)
    
    def deck_list_info_noUpdate(self, sort=0):
        """
        Diese Funktion gibt die Liste aller Kartenstapel mit Infos zurueck
        Liste: [[name,kategorie, timestamp, AnzahlKarten, Lernstand], ...]
        """
        if sort==0:
            return self.__deck_list_info
        else:
            return self.__deck_sort(sort)
    
    def deck_create(self, name, kategorie, description):
        """
        Diese Funktion erstellt eine Datei, mit dem namen "name.rna" her, fals noetig: "name_x.rna"
        und dem Inhalt:
        name||kategorie||timestamp||beschreibung
        und updatet die Deck-Liste
        """
        self.__deck_list_update()
        #Erstellen des Dateinamens
        dateiname = self.__str_make_valid_filename(name)+self.__card_suffix
        #dopplungen vermeiden
        if self.__deck_list.count(dateiname)>0:
            i=2
            dateiname = self.__str_make_valid_filename(name)+"_"+str(i)+self.__card_suffix
            while self.__deck_list.count(dateiname)>0:
                i+=1
                dateiname = self.__str_make_valid_filename(name)+"_"+str(i)+self.__card_suffix
        name = self.__str_make_valid(name)
        kategorie = self.__str_make_valid(kategorie)
        description = self.__str_make_valid(description)
        #Schreiben in die Datei
        datei = open(self.__deck_dir+dateiname, "w", encoding='utf8')
        timestamp = self.__timestamp()
        datei.write(                         name\
                    +self.__file_separator + kategorie\
                    +self.__file_separator + timestamp\
                    +self.__file_separator + description\
                    +self.__file_separator + "0"\
                    +self.__file_separator + "0"\
                    +"\n")
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
        
    def deck_delete_loaded(self):
        """
        Diese Funktion loescht das geladene Deck und updatet die Deck-Liste
        """
        self.__deck_list_update()
        if self.__deck in self.__deck_list:
            os.remove(self.__deck_dir+self.__deck)
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
        self.__deck_cards_loaded = False
    
    def deck_rename(self, newName):
        """
        Benennt das geladene Deck um.
        Voraussetzung: Deck muss geladen sein.
        """
        newName = self.__str_make_valid(newName)
        if not self.__deck == newName+self.__card_suffix:
            self.__deck_list_update()
            name = newName
            newName = self.__str_make_valid_filename(name)+ self.__card_suffix
            #Erstellen des Dateinamens
            if self.__deck_list.count(newName)>0:
                i=2
                newName = self.__str_make_valid_filename(name)+"_" + str(i) + self.__card_suffix
                while self.__deck_list.count(newName)>0:
                    i+=1
                    newName = self.__str_make_valid_filename(name)+"_" + str(i) + self.__card_suffix
            os.rename(self.__deck_dir + self.__deck, self.__deck_dir + newName)
            datei=open(self.__deck_dir + newName, "r", encoding='utf8')
            inhalt = datei.readlines()
            datei.close()
            inhalt[0]= self.__file_string_change_cell(inhalt[0], name, 0)
            datei = open(self.__deck_dir + newName,"w", encoding='utf8')
            datei.writelines(inhalt)
            datei.close()
            self.__deck = newName
            self.__deck_list_update()

    def deck_change_kategorie(self, newKategorie):
        """
        Diese Funktion aendert die Kategorie des geladenen Deckes zur uebergebenen Kategorie
        """
        newKategorie = self.__str_make_valid(newKategorie)
        datei=open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        datei.close()
        inhalt[0]=self.__file_string_change_cell(inhalt[0], newKategorie, 1) 
        datei = open(self.__deck_dir + self.__deck,"w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
    
    def __deck_new_timestamp(self):
        """
        Diese Funktinon erneuert den Zeitstempel des geladenen Deckes.
        """
        datei=open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        datei.close()
        inhalt[0] =   self.__file_string_change_cell(inhalt[0], self.__timestamp(),2)
        datei = open(self.__deck_dir + self.__deck,"w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
        
    def deck_change_description(self, newDescription):
        """
        Diese Funktion aendert die Beschreibung der geladenen Kategorie in die uebergebene Beschreibung.
        Voraussetzung: Deck muss geladen sein.
        """
        newDescription = self.__str_make_valid(newDescription)
        datei=open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        datei.close()
        inhalt[0] = self.__file_string_change_cell(inhalt[0], newDescription, 3)
        datei=open(self.__deck_dir + self.__deck, "w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
    
    def deck_statistik(self):
        """
        Diese Funktion gibt die Statistik des Deckes zurueck
        """
        self.__deck_statistik_generate()
        bad_list = list()
        for elem in self.__deck_cards_learned:
            if not elem[2]==[]:
                bad_list.append(elem[2])
        return bad_list    
    
    def deck_statistik_reset(self):
        """
        Diese Funktion resetet die Statistik des aktuellen Decks
        """
        self.__deck_cards_load()
        datei = open(self.__deck_dir + self.__deck, mode="r", encoding='utf-8')
        inhalt = datei.readlines()
        datei.close()
        newInhalt = [self.__file_string_change_cell(inhalt[0], 0, 5)+"\n"]
        for i in range(len(self.__deck_cards_learned)):
            newInhalt.append(self.__file_string_change_cell(inhalt[i+1], self.__deck_begin_statistik, 3)+"\n")
        datei = open(self.__deck_dir + self.__deck, mode="w", encoding='utf-8')
        datei.writelines(newInhalt)
        datei.close()
    
    def __deck_statistik_generate(self):
        """
        Diese Funktion generiert eine neue Statistik aus der Liste self.__deck_cards_learned.
        """
        result_correct=0
        result_ges=0
        deck_result=0
        for elem in self.__deck_cards_learned:
            if len(elem[-1]) > self.__deck_statistik_max_len:
                elem[-1] = elem[-1][-self.__deck_statistik_max_len:]
            for result in elem[-1]:
                if result == "1":
                    result_correct += 1
                result_ges += 1
        if result_ges>0:
            deck_result = (100 * result_correct)//result_ges
        datei = open(self.__deck_dir + self.__deck, mode="r", encoding='utf-8')
        inhalt = datei.readlines()
        datei.close()
        newInhalt = [self.__file_string_change_cell(inhalt[0], deck_result, 5)+"\n"]
        for i in range(len(self.__deck_cards_learned)):
            newInhalt.append(self.__file_string_change_cell(inhalt[i+1], self.__deck_cards_learned[i][-1], 3)+"\n")
        
        datei = open(self.__deck_dir + self.__deck, mode="w", encoding='utf-8')
        datei.writelines(newInhalt)
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
        if not self.__deck_cards_loaded:
            self.__deck_cards_load()
        if len(self.__deck_cards_learn)>0:
            return True
        else:
            self.__deck_new_timestamp()
            self.__deck_statistik_generate()
            return False
    
    def deck_cards(self):
        """
        Diese Funktion gibt alle Karten eines Decks mit ids zurueck.
        [id,[Seite1, Seite2], id2, [Seite1, Seite2],...]
        """
        self.__deck_cards_load()
        return self.__deck_cards
    
    def __deck_count_cards(self):
        """
        Diese Funktion zaehlt die Anzahl der Karten und aendert die Anzahl in der Datei.
        Voraussetzung: Deck muss geladen sein
        """
        datei = open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        anzahlKarten = len(inhalt[1:])
        datei.close()
        inhalt[0] = self.__file_string_change_cell(inhalt[0], str(anzahlKarten), 4)
        datei = open(self.__deck_dir + self.__deck, "w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
    
    def card_create(self, Seite1, Seite2, doppelseitig = 1):
        """
        Diese Funktion fuegt die Karte hinzu
        Voraussetzung: Deck muss geladen sein
        """
        Seite1 = self.__str_make_valid(Seite1)
        Seite2 = self.__str_make_valid(Seite2)
        datei = open(self.__deck_dir + self.__deck, "a", encoding='utf8')
        datei.write(Seite1 + self.__file_separator + Seite2 + self.__file_separator + str(doppelseitig) + self.__file_separator + self.__deck_begin_statistik + "\n")
        datei.close()
        self.__deck_count_cards()
        
    def deck_card_load(self, card_id):
        self.__deck_card_id = card_id
    
    
    def card_delete(self):
        """
        Diese Funktion loescht die Karte
        Voraussetzung: Deck muss geladen sein
        """
        datei = open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        inhalt = inhalt[:self.__deck_card_id+1]+ inhalt[self.__deck_card_id+2:]
        datei.close()
        datei = open(self.__deck_dir + self.__deck, "w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
        self.__deck_count_cards
    
    def card_change(self, site1 = "", site2 = ""):
        """
        Diese Funktion aendert den inhalt der Karten (jenachdem, welche angegeben wurde).
        Bei leerem String wird nichts geaendert.
        Voraussetzung: Deck muss geladen sein.
        """
        datei = open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        datei.close()
        karte = inhalt[self.__deck_card_id+1].split(self.__file_separator)
        if not site1 == "":
            karte[0] = self.__str_make_valid(site1)
        if not site2 == "":
            karte[1] = self.__str_make_valid(site2)
        inhalt[self.__deck_card_id+1] = ""
        for elem in karte:
            inhalt[self.__deck_card_id+1] += elem + self.__file_separator
        inhalt[self.__deck_card_id+1] = inhalt[self.__deck_card_id+1][:-2]
        datei = open(self.__deck_dir + self.__deck, "w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
    
    def card_lernSide_all(self, setValue):
        """
        Diese Funktion aendert die Lernrichtung von Karten auf "setValue"
        setValue: 0 [Seite1,Seite2], 1 [Seite2, Seite1], 2 [Seite1, Seite2] [Seite2, Seite1]
        """
        datei = open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        datei.close()
        for i in range(1,len(inhalt)):
            inhalt[i]=self.__file_string_change_cell(inhalt[i], setValue, 2)
        datei = open(self.__deck_dir + self.__deck, "w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
    
    def card_lernSide(self, setValue):
        """
        Diese Funktion aendert die Lernrichtung von Karten auf "setValue"
        setValue: 0 [Seite1,Seite2], 1 [Seite2, Seite1], 2 [Seite1, Seite2] [Seite2, Seite1]
        """
        datei = open(self.__deck_dir + self.__deck, "r", encoding='utf8')
        inhalt = datei.readlines()
        datei.close()
        karte = inhalt[self.__deck_card_id+1].split(self.__file_separator)
        karte[2] = setValue
        inhalt[self.__deck_card_id+1] = ""
        for elem in karte:
            inhalt[self.__deck_card_id+1] += elem + self.__file_separator
        inhalt[self.__deck_card_id+1] = inhalt[self.__deck_card_id+1][:-2]
        datei = open(self.__deck_dir + self.__deck, "w", encoding='utf8')
        datei.writelines(inhalt)
        datei.close()
    
    def numberOfCards(self):
        return self.__numberOfCards
    
    def numberOfCardsLearned(self):
        return self.__numberOfCards-len(self.__deck_cards_learn)
    
    def random_card(self):
        """
        Diese Funktion waehlt aus dem aktuellen Deck eine zufaellige Karte aus (nur eine Seite),
        speichert sie (als letzte Karte) und loescht diese aus der __deck_card_learn und gibt diese aus.
        """
        self.__deck_new_timestamp()
        if not self.__deck_cards_loaded:
            self.__deck_cards_load()
        self.__deck_card_answered = False
        self.__last_card = random.choice(self.__deck_cards_learn)
        self.__deck_cards_learn.remove(self.__last_card)
        return self.__last_card[1]

    def last_card(self):
        """
        Diese Funktion gibt die letzte Karte
        """
        return self.__last_card[1]
    
    def last_card_answer(self):
        """
        Diese Funktion gibt die Antwort der letzten Karte zurueck
        """
        return self.__last_card[2]
    
    def card_correct(self, answer):
        """
        Diese Funktion prueft die Antwort auf die Korrektheit (True oder False)
        und speichert sich das erste Ergebnis
        """
        if answer == self.__last_card[2]:
            answer_correct = True
        else:
            answer_correct = False
        self.__deck_statistik_generate()
        if not self.__deck_card_answered:
            self.__deck_card_answered = True
            if answer_correct:
                self.__deck_cards_learned[self.__last_card[0]-1][-1] += "1"
            else:
                self.__deck_cards_learned[self.__last_card[0]-1][-1] += "0"
                self.__deck_cards_learned[self.__last_card[0]-1][2] =[self.__last_card[1], self.__last_card[2], answer]
        return answer_correct
            
        
        
    
    def set_config(self, var, value):
        """
        Diese Funktion schreibt den value in die Konfigurationsdatei hinein
        """
        datei = open(self.__config_dir + var +self.__config_suffix, "w")
        datei.write(str(value))
        
    def get_config(self, var):
        """
        Diese Funktion liesst einen Wert aus Konfigurationsdatei heraus
        Falls die Variable nicht existiert, wird 0 zurueckgegeben
        """
        try:
            datei = open(self.__config_dir + var + self.__config_suffix)
            value = datei.read()
            try:    return int(value)
            except: return value
        except:
            return
    
    def __pruefe_dateipfade(self):
        """
        Diese Funktion prueft, ob alle noetigen Dateipfade existieren, wenn nicht, werden diese hier erstllt
        noetige Dateipfade:
        """
        if not os.path.isdir(self.__root_dir):
            os.mkdir(self.__root_dir)
        if not os.path.isdir(self.__data_dir):
            os.mkdir(self.__data_dir)
        if not os.path.isdir(self.__deck_dir):
            os.mkdir(self.__deck_dir)
        if not os.path.isdir(self.__config_dir):
            os.mkdir(self.__config_dir)

if __name__=="__main__":
    """
    Testumgebung
    """
    acc = funktion()