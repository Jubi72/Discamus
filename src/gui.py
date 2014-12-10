#from interface import *
import tkinter


class gui:
    def __init__(self, title, breite, hoehe,schriftfarbe, fullscreen = True):
        self.label_width = 40        #gib die Größe für die Labels an
        self.label_color = "#6e6e6e" #Label Hintergrund
        self.text_color = "white"    #Label Text Farbe
        self.bg_color = "#4d4d4d"
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
        self.root.config(bg=self.bg_color)
        
        
    def show_window(self):
        """
        Diese Funktion zeigt (pack) das Fenster an.
        """
        self.root.pack()
        
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
    def create_mainmenu(self):
        """
        Diese Funktion erstellt die Elemente des Hauptmenues.
        Voraussetzung: Fenster muss erstellt sein.
        m1 usw. sind der Text der Angezeigt wird
        """
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
        self.m7 = tkinter.Button(self.menu2, text="Optionen", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command=self.create_options_menu)
        self.m8 = tkinter.Button(self.menu2, text="Verlassen", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command=self.show_exit_menu)
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
        self.m0.destroy()
        self.m1.destroy()
        self.m2.destroy()
        self.m3.destroy()
        self.m4.destroy()
        self.m5.destroy()
        self.m6.destroy()
        self.m7.destroy()
        self.m8.destroy()
        self.menu1.destroy()
        self.menu2.destroy()
        self.root.update()

    #OPTIONS MENU
    def create_options_menu(self):
        """
        zeigt Menue für Optionen an
        """
        self.hide_mainmenu()
        o1 = "Design 1 (Grau-Weiß)"
        o2 = "Design 2 (Weiß-Schwarz)"
        o3 = "Design 3 (Blau-Orange)"
        o4 = "Design 4 (Orange-Blau)"
        self.option1 = tkinter.Frame(self.root)
        self.option1.config(bg=self.label_color)
        self.option1.config(bd = 5, relief = "ridge")
        self.option1.pack(side="top")
        self.option2 = tkinter.Frame(self.root)
        self.option2.config(bg=self.label_color)
        self.option2.config(bd = 5, relief = "ridge")
        self.option2.pack(side="bottom")
        self.o0 = tkinter.Label(self.option1, text="Optionen", font=("Comic Sans MS", 30), fg=self.text_color, bg=self.label_color)
        self.o1 = tkinter.Button(self.option1, text=str(o1), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command = self.change_design1)
        self.o2 = tkinter.Button(self.option1, text=str(o2), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command = self.change_design2)
        self.o3 = tkinter.Button(self.option1, text=str(o3), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command = self.change_design3)
        self.o4 = tkinter.Button(self.option1, text=str(o4), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command = self.change_design4)
        self.o5 = tkinter.Button(self.option2, text="Zurueck", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command=self.hide_options_menu)
        self.o0.pack()
        self.o1.pack()
        self.o2.pack()
        self.o3.pack()
        self.o4.pack()
        self.o5.pack()
        self.root.update()


    def change_design1(self):
        """
        Menue Design 1
        """
        self.label_color = "#6e6e6e" #Label Hintergrund
        self.text_color = "white"    #Label Text Farbe
        self.bg_color =  "#4d4d4d"
        self.hide_options_menu()
        self.root.config(bg=self.bg_color)
        self.root.update()

    def change_design2(self):
        """
        Menue Design 2
        """
        self.label_color = "white" #Label Hintergrund
        self.text_color = "black"    #Label Text Farbe
        self.bg_color = "#D0D0D0"
        self.hide_options_menu()
        self.root.config(bg=self.bg_color)
        self.root.update()

    def change_design3(self):
        """
        Menue Design 3
        """
        self.label_color = "orange" #Label Hintergrund
        self.text_color = "blue"    #Label Text Farbe
        self.bg_color = "#d65a00"
        self.hide_options_menu()
        self.root.config(bg=self.bg_color)
        self.root.update()

    def change_design4(self):
        """
        Menue Design 4
        """
        self.label_color = "blue" #Label Hintergrund
        self.text_color = "orange"    #Label Text Farbe
        self.bg_color = "#000066"
        self.hide_options_menu()
        self.root.config(bg=self.bg_color)
        self.root.update()

    def hide_options_menu(self):
        """
        Versteckt Option Menue
        """
        self.o0.destroy()
        self.o1.destroy()
        self.o2.destroy()
        self.o3.destroy()
        self.o4.destroy()
        self.o5.destroy()
        self.option1.destroy()
        self.option2.destroy()
        self.create_mainmenu()
        self.root.update()

    
    #VOCABLE MENU
    def create_vocmenu(self):
        """
        Diese Funktion erstellt die Elemente des Menue, wo die ganzen Vokabeln angezeigt werden.
        Voraussetzung: Das Fenster muss erstellt sein.
        """
        pass
    
    def hide_vocmenu(self):
        """
        Diese Funktion versteckt die Elemente des Hauptmenues.
        Voraussetzung: Erstellen muss erfolgt sein [create_vocmenu()].
        """
        pass

    #EXIT MENU
    
    def show_exit_menu(self):
        """
        Überprüfen ob wirklich beendet werden soll
        """
        self.hide_mainmenu()
        self.exit = tkinter.Frame(self.root)
        self.exit.config(bg=self.label_color)
        self.exit.config(bd = 5, relief = "ridge")
        self.exit.pack()
        self.e1 = tkinter.Label(self.exit, text= "Wirklich Verlassen?", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.e2 = tkinter.Button(self.exit, text="Ja", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command = self.quit_window)
        self.e3 = tkinter.Button(self.exit, text="Nein", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command = self.dont_quit_window)
        self.e1.pack()
        self.e2.pack()
        self.e3.pack()
        
        

    def quit_window(self):
        """
        Schließen das Programms
        """
        self.root.destroy()

    def dont_quit_window(self):
        """
        Zeigt Hauptmenue an
        """
        
        self.create_mainmenu()
        self.root.update()

    def hide_exit_menu(self):
        self.exit.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        self.show_mainmenu()
        
    

    
test = gui("Test", 500, 500, "black", True)
test.create_mainmenu()
tkinter.mainloop()
