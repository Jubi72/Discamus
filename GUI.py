from interface import *
class GUI:
    def create_window(self):
        """
        Das Fenster wird Erstellt (ohne inhalt, aber mit den ganzen Eigenschaften)
        """
        pass
    
    def show_window(self):
        """
        Diese Funktion Zeigt (pack) das Fenster an.
        """
        pass
        
    def quit_window(self):
        """
        Diese Fenster entfert wieder das Programm.
        """
        pass
    
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
