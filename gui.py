#from interface import *
import tkinter


class gui:
    def __init__(self, title, breite, hoehe, bgfarbe, schriftfarbe, fullscreen = True):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.__breite = breite # Abspeichern wegen Standardgroesse
        self.__hoehe = hoehe
        self.__fullscreen = fullscreen
        if fullscreen:
            self.root.attributes("-fullscreen", True)
        else:
            self.root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
        # self.__root.bind("<F11>", self.fullscreen) ### vielleicht gleich Fullscreen ???
        # self.__root.bind("<Escape>", self.escape)
        # self.__root.bind("<F1>",helpme)
        self.root.config(bg=bgfarbe)
        
        
    def show_window(self):
        """
        Diese Funktion zeigt (pack) das Fenster an.
        """
        self.root.pack()
        
    def check_quit_window(self):
        self.m7.config(text="Sicher?")
        self.m8.config(text="Ja", command=self.quit_window)
        self.m9 = tkinter.Button(self.menu2, text="Nein", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width=self.label_width, command=self.dont_quit_window)
        self.m9.pack()
        self.root.update()

    def quit_window(self):
        """
        Dieses Fenster entfert wieder das Programm.
        """
        self.root.destroy()

    def dont_quit_window(self):
        self.m9.destroy()
        self.m7.config(text="Optionen")
        self.m8.config(text="Verlassen", command=self.check_quit_window)
        self.root.update()
        
    

    def toogle_fullscreen(self):
        """
        Funktion wechselt zwischen Vollbild und Fenster
        Kommentar von Niko: besser wenn es zwei (weitere) Funktionen gäbe für Vollbild und "Normal"
        """
        if self.__fullscreen:
            self.__fullscreen=False
            self.root.attributes("-fullscreen", False)
            self.root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
        else:
            self.__fullscreen=True
            self.root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
            self.root.attributes("-fullscreen", True)

    """
    def escape(self):
        root.attributes("-fullscreen", False)
        # self.__root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
    """

    def show_height(self):
        self.root.update()
        self.__height = self.root.winfo_height()
        #print(self.__height)
        return self.__height
        
    def show_width(self):
        self.root.update()
        self.__width = self.root.winfo_width()
        #print(self.__width)
        return self.__width

    
    #MAIN MENU
    def show_mainmenu(self):
        """
        Diese Funktion erstellt die Elemente des Hauptmenues.
        Voraussetzung: Fenster muss erstellt sein.
        m1 usw. sind der Text der Angezeigt wird
        """
        self.label_width = 40      #gib die Größe für die Labels an
        self.label_color = "#6e6e6e"
        self.text_color = "white"
        m1 = "Auswahl 1"
        m2 = "Auswahl 2"
        m3 = "Auswahl 3"
        m4 = "Auswahl 4"
        m5 = "Auswahl 5"
        m6 = "Auswahl 6"
        self.menu1 = tkinter.Frame(self.root)
        self.menu1.config(bg=self.label_color)
        self.menu1.config(bd = 5, relief = "ridge")
        self.menu1.pack(side="top")
        self.menu2 = tkinter.Frame(self.root)
        self.menu2.config(bg=self.label_color)
        self.menu2.config(bd = 5, relief = "ridge")
        self.menu2.pack(side="bottom")
        self.m0 = tkinter.Label(self.menu1, text="Hauptmenü", font=("Comic Sans MS", 30), fg=self.text_color, bg=self.label_color)
        self.m1 = tkinter.Button(self.menu1, text=str(m1), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m2 = tkinter.Button(self.menu1, text=str(m2), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m3 = tkinter.Button(self.menu1, text=str(m3), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m4 = tkinter.Button(self.menu1, text=str(m4), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m5 = tkinter.Button(self.menu1, text=str(m5), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m6 = tkinter.Button(self.menu1, text=str(m6), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m7 = tkinter.Button(self.menu2, text="Optionen", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m8 = tkinter.Button(self.menu2, text="Verlassen", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command=self.check_quit_window)
        self.m0.pack()
        self.m1.pack()
        self.m2.pack()
        self.m3.pack()
        self.m4.pack()
        self.m5.pack()
        self.m6.pack()
        self.m7.pack()
        self.m8.pack()
    
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
    
test = gui("Test", 500, 500, "#4d4d4d", "black", True)
test.show_mainmenu()
tkinter.mainloop()
