from interface import *
import tkinter as tk

class gui:
    def create_window(self):
        """
        Voraussetzung: folgende Variablen muessen gesetzt sein:
                            - __fullscreen [true, false]
                            - __breite
                            - __hoehe
                            - __titel
        """
        self.__root = tk.Tk()
        if self.__fullscreen:
            self.__root.tk.attributes("-fullscreen", True)
        else:
            self.__root.tk.geometry(str(self.__breite) + "x" + str(self.__hoehe))
        
    def show_window(self):
        """
        Diese Funktion zeigt (pack) das Fenster an.
        """
        self.__root.tk.pack()
        
    def quit_window(self):
        """
        Dieses Fenster entfert wieder das Programm.
        """
        self.__root.tk.destroy()
    
    def __init__(self, titel, breite, hoehe, fullscreen = True):
        #Abspeichern der Variablen
        self.__breite = breite
        self.__hoehe = hoehe
        self.__fullscreen = fullscreen
        self.__titel= titel
        self.create_window()
        # self.__root.tk.bind("<F11>", self.fullscreen) ### vielleicht gleich Fullscreen ???
        # self.__root.tk.bind("<Escape>", self.escape)
        # self.__root.tk.bind("<F1>",helpme)

    def toogle_fullscreen(self):
        """
        Funktion wechselt zwischen Vollbild und Fenster
        Kommentar von Niko: besser wenn es zwei (weitere) Funktionen gäbe für Vollbild und "Normal"
        """
        if self.__fullscreen:
            self.__fullscreen=False
            self.__root.tk.attributes("-fullscreen", False)
            self.__root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
        else:
            self.__fullscreen=True
            self.__root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
            self.__root.tk.attributes("-fullscreen", True)

    def width(self):
        """
        Funktion gibt die aktuelle Breite des Fensters zurueck
        """
        self.__root.tk.update()
        self.__weidth = self.__root.tk.winfo_weidth()
        return self.__weidth

    def height(self):
        """
        Funktion gibt die aktuelle Hoehe des Fensters zurueck
        """
        self.__root.tk.update()
        self.__height = self.__root.tk.winfo_height()
        return self.__height
    
    #MAIN MENU
    def create_mainmenu(self):
        """
        Diese Funktion erstellt die Elemente des Hauptmenues.
        Voraussetzung: Fenster muss erstellt sein.
        """
        pass
    
    def show_mainmenu(self):
        """
        Diese Funktion zeigt die Elemente des Hauptmenues an.
        Voraussetzung: Das Erstellen [create_mainmenu()] muss erfolgt sein.
        """
        pass
    
    def hide_mainmenu(self):
        """
        Diese Funktion versteckt die Elemente des Hauptmenues.
        Voraussetzung: Das ertellen muss erfolgt sein.
        """
        pass
    
    #VOCABLE MENU
    def create_vocmenu(self):
        """
        Diese Funktion erstellt die Elemente des Menue, wo die ganzen Vokabeln angezeigt werden.
        Voraussetzung: Das Fenster muss erstellt sein.
        """
        pass
    
    def show_vocmenu(self):
        """
        Diese Funktion zeigt die Elemente des Hauptmenues an.
        Voraussetzung: Erstellen muss erfolgt sein [create_vocmenu()].
        """
        pass
    
    def hide_vocmenu(self):
        """
        Diese Funktion versteckt die Elemente des Hauptmenues.
        Voraussetzung: Erstellen muss erfolgt sein [create_vocmenu()].
        """
        pass

    #EXIT MENU
    def create_exitmenu(self):
        """
        Diese Funktion erstellt das Exit-Menue (mit Elementen).
        Voraussetzung: Das Fenster muss erstellt sein.
        """
        pass

    def show_exitmenu(self):
        """
        Diese Funktion zeigt das Exit-Menue.
        Voraussetzung: Menue muss existieren.
        """
        pass
    
    def hide_exitmenu(self):
        """
        Diese Funktion versteckt das Exit-Menue.
        Voraussetzung: Menue muss existieren.
        """
        pass
    
