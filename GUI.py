from interface import *
import tkinter as tk

class GUI:
    def __init__(self, title, breite, hoehe, bgfarbe, schriftfarbe):
        self.__root = tk.Tk()
        self.__root.tk.title(title)
        self.__breite = breite # Abspeichern wegen Standardgroesse
        self.__hoehe = hoehe
        self.__root.tk.geometry(str(self.__breite) + "x" + str(self.__hoehe))
        # self.__root.tk.bind("<F11>", self.fullscreen) ### vielleicht gleich Fullscreen ???
        # self.__root.tk.bind("<Escape>", self.escape)
        # self.__root.tk.bind("<F1>",helpme)
        self.__root.tk.configure(bg=bgfarbe)

    """
    def fullscreen(self):
        root.attributes("-fullscreen", True)
    def escape(self):
        root.attributes("-fullscreen", False)
        # self.__root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
    """

    def show_height(self):
        self.__root.tk.update()
        self.__height = self.root.tk.winfo_height()
        return self.__height
        
    def show_width(self):
        self.__root.tk.update()
        self.__width = self.root.tk.winfo_width()
        return self.__width

    def show_window(self):
        """
        Diese Funktion Zeigt (pack) das Fenster an.
        """
        self.__root.tk.pack()
        
    def quit_window(self):
        """
        Diese Fenster entfert wieder das Programm.
        """
        self.__root.tk.unpack()
    
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
    
