from interface import *
class GUI:
    
    def __init__(self, title, groesse, bgfarbe, schriftfarbe):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(groesse)
        self.__root.configure(bg=bgfarbe)

    def show_height(self):
        self.__root.update()
        selfheight = self.root.winfo_height()
        return height
        
    def show_width(self):
        self.__root.update()
        width = self.root.winfo_width()
        return width

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
