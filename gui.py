from interface import *
import tkinter

<<<<<<< HEAD:GUI.py
class GUI:
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
=======
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
>>>>>>> origin/master:gui.py

    def toogle_fullscreen(self):
        """
        Funktion wechselt zwischen Vollbild und Fenster
        Kommentar von Niko: besser wenn es zwei (weitere) Funktionen gäbe für Vollbild und "Normal"
        """
        if self.__fullscreen:
            self.__fullscreen=False
<<<<<<< HEAD:GUI.py
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
        return self.__height
        
    def show_width(self):
        self.root.update()
        self.__width = self.root.winfo_width()
        return self.__width
=======
            self.__root.tk.attributes("-fullscreen", False)
            self.__root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
        else:
            self.__fullscreen=True
            self.__root.geometry(str(self.__breite) + "x" + str(self.__hoehe))
            self.__root.tk.attributes("-fullscreen", True)
>>>>>>> origin/master:gui.py

    def width(self):
        """
        Funktion gibt die aktuelle Breite des Fensters zurueck
        """
<<<<<<< HEAD:GUI.py
        self.root.pack()
        
    def quit_window(self):
=======
        self.__root.tk.update()
        self.__weidth = self.__root.tk.winfo_weidth()
        return self.__weidth

    def height(self):
>>>>>>> origin/master:gui.py
        """
        Funktion gibt die aktuelle Hoehe des Fensters zurueck
        """
<<<<<<< HEAD:GUI.py
        self.root.unpack()
=======
        self.__root.tk.update()
        self.__height = self.__root.tk.winfo_height()
        return self.__height
>>>>>>> origin/master:gui.py
    
    #MAIN MENU
    def show_mainmenu(self):
        """
        Diese Funktion erstellt die Elemente des Hauptmenues.
        Voraussetzung: Fenster muss erstellt sein.
        m1 usw. sind der Text der Angezeigt wird
        """
        m1 = "ienfinwfneifnwief"
        m2 = "wefefwf"
        m3 = "wefwefwefwe"
        m4 = "wfeefw"
        m5 = "efffffffffffffffffefewfefwf"
        m6 = "wfwefwefwefwf"
        menu = tkinter.Frame(self.root)
        menu1 = tkinter.Frame(menu)
        menu.config(width= self.show_width()//3, height=self.show_height())
        menu.config(bg="red")
        menu.pack()
        menu.place(x=self.show_width()//3, y=10)
        m0 = tkinter.Label(menu, text="Mainmenu", font=("Comic Sans MS", 30), bg="red", width=self.show_width()//3)
        m1 = tkinter.Button(menu, text=str(m1), font=("Comic Sans MS", 18), bg="white", width=self.show_width()//3)
        m2 = tkinter.Button(menu, text=str(m2), font=("Comic Sans MS", 18), bg="white", width=self.show_width()//3)
        m3 = tkinter.Button(menu, text=str(m3), font=("Comic Sans MS", 18), bg="white", width=self.show_width()//3)
        m4 = tkinter.Button(menu, text=str(m4), font=("Comic Sans MS", 18), bg="white", width=self.show_width()//3)
        m5 = tkinter.Button(menu, text=str(m5), font=("Comic Sans MS", 18), bg="white", width=self.show_width()//3)
        m6 = tkinter.Button(menu, text=str(m6), font=("Comic Sans MS", 18), bg="white", width=self.show_width()//3)
        m0.pack()
        m1.pack()
        m2.pack()
        m3.pack()
        m4.pack()
        m5.pack()
        m6.pack()
    
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
    
test = GUI("Test", 500, 500, "orange", "black", False)
test.show_mainmenu()
tkinter.mainloop()
