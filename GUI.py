from interface import *
from tkinter import *

class GUI:
    def __init__(self, title, groesse, bgfarbe, schriftfarbe):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(groesse)
        self.__root.configure(bg=bgfarbe)

    def show_height(self):
        self.__root.update()
        self.__height = self.root.winfo_height()
        return self.__height
        
    def show_width(self):
        self.__root.update()
        self.__width = self.root.winfo_width()
        return self.__width

    def show_window(self):
        """
        Diese Funktion Zeigt (pack) das Fenster an.
        """
        self.__root.pack()
        
    def quit_window(self):
        """
        Diese Fenster entfert wieder das Programm.
        """
        self.__root.unpack()
    
    #MAIN MENU
    def create_mainmenu(self):
        """
        Diese Funktion erstellt die Elemente des Hauptmenues
        Voraussetzung: Fenster muss erstellt sein.
        """
        pass
    
    def show_mainmenu(self):
        """
        Diese Funktion zeigt die Elemente des Hauptmenues an
        Voraussetzung: Das ertellen [create_mainmenu()] muss erfolgt sein
        """
        pass
    
    def hide_mainmenu(self):
        """
        Diese Funktion versteckt die Elemente des Hauptmenue
        Voraussetzung: Das ertellen muss erfolgt sein
        """
        pass
    
    #VOCABLE MENU
    def create_vocmenu(self):
        """
        Diese Funktion erstellt die Elemente des Menue, wo die ganzen Vokabeln angezeigt werden
        Voraussetzung: Das Fenster muss erstellt sein.
        """
        pass
    
    def show_vocmenu(self):
        """
        Diese Funktion zeigt die Elemente des Hauptmenues an.
        Voraussetzung: Erstellen muss erfolgt sein [create_vocmenu()]
        """
        pass
    
    def hide_vocmenu(self):
        """
        Diese Funktion versteckt die Elemente des Hauptmenues.
        Voraussetzung: Erstellen muss erfolgt sein [create_vocmenu()]
        """
        pass

    #EXIT MENU
    def create_exitmenu(self):
        """
        Diese Funktion erstellt das Exit-Menue (mit Elementen)
        Voraussetzung: Das Fenster muss erstellt sein.
        """
        pass

    def show_exitmenu(self):
        """
        Diese Funktion zeigt das Exit-Menue
        Voraussetzung: Menue muss existieren
        """
        pass
    
    def hide_exitmenu(self):
        """
        Diese Funktion versteckt das Exit-Menue
        Voraussetzung: Menue muss existieren
        """
        pass
    
