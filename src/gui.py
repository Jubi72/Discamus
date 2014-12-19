#from interface import *
import tkinter


class gui:
    def __init__(self, title, breite, hoehe,schriftfarbe, fullscreen = True):
        self.label_width = 25        #gib die Größe für die Labels an
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
        # self.__root.bind("<F1>",self.helpme)
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
    def enterm1(self, event):
        self.m1.config(bg="white", fg="black")
        
    def leavem1(self, event):
        self.m1.config(bg=self.label_color, fg=self.text_color)

    def enterm2(self, event):
        self.m2.config(bg="white", fg="black")
        
    def leavem2(self, event):
        self.m2.config(bg=self.label_color, fg=self.text_color)

    def enterm3(self, event):
        self.m3.config(bg="white", fg="black")
        
    def leavem3(self, event):
        self.m3.config(bg=self.label_color, fg=self.text_color)

    def enterm4(self, event):
        self.m4.config(bg="white", fg="black")
        
    def leavem4(self, event):
        self.m4.config(bg=self.label_color, fg=self.text_color)


    def enterm5(self, event):
        self.m5.config(bg="white", fg="black")
        
    def leavem5(self, event):
        self.m5.config(bg=self.label_color, fg=self.text_color)


    def enterm6(self, event):
        self.m6.config(bg="white", fg="black")
        
    def leavem6(self, event):
        self.m6.config(bg=self.label_color, fg=self.text_color)


    def enterm7(self, event):
        self.m7.config(bg="white", fg="black")
        
    def leavem7(self, event):
        self.m7.config(bg=self.label_color, fg=self.text_color)
        


    def create_mainmenu(self):
        """
        Diese Funktion erstellt die Elemente des Hauptmenues.
        Voraussetzung: Fenster muss erstellt sein.
        m1 usw. sind der Text der Angezeigt wird
        """
        m1 = "Lernen"
        m2 = "Testen"
        m3 = "Editor"
        m4 = "Statistiken"
        self.head = tkinter.Frame(self.root)
        self.head.config(bg=self.label_color)
        self.head.config(bd = 5, relief = "ridge")
        self.head.pack(side="top")
        self.menu = tkinter.Frame(self.root)
        self.menu.config(bg=self.label_color)
        self.menu.config(bd = 5, relief = "ridge")
        self.menu.pack()
        self.menu1 = tkinter.Frame(self.menu)
        self.menu1.config(bg=self.label_color)
        self.menu1.config(bd = 5, relief = "ridge")
        self.menu1.pack(side="left")
        self.menu2 = tkinter.Frame(self.menu)
        self.menu2.config(bg=self.label_color)
        self.menu2.config(bd = 5, relief = "ridge")
        self.menu2.pack(side="left")
        self.menu3 = tkinter.Frame(self.root)
        self.menu3.config(bg=self.label_color)
        self.menu3.config(bd = 5, relief = "ridge")
        self.menu3.pack(side="bottom")
        self.listbox = tkinter.Listbox(self.menu1, font=("Comic Sans MS", 18), fg = self.text_color, bg=self.bg_color)
        self.listbox.config(selectbackground = "white",selectforeground="black")
        self.listbox.pack()
        self.listbox.insert("end", "Kategorie " + "Name " + "Anz. " + "Datum " + "Fortschr.")
        self.m0 = tkinter.Label(self.head, text="Discamus", font=("Comic Sans MS", 30), fg=self.text_color, bg=self.label_color, width = self.label_width*2)
        self.m1 = tkinter.Button(self.menu2, text=str(m1), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m2 = tkinter.Button(self.menu2, text=str(m2), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m3 = tkinter.Button(self.menu2, text=str(m3), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m4 = tkinter.Button(self.menu2, text=str(m4), font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m5 = tkinter.Button(self.menu3, text="Optionen", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command=self.create_options_menu)
        self.m6 = tkinter.Button(self.menu3, text="Hilfe", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width)
        self.m7 = tkinter.Button(self.menu3, text="Verlassen", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command=self.show_exit_menu)
        self.m0.pack()
        self.m1.pack()
        self.m2.pack()
        self.m3.pack()
        self.m4.pack()
        self.m5.pack(side="left")
        self.m6.pack(side="left")
        self.m7.pack(side="left")
        self.m1.bind('<Enter>', self.enterm1)
        self.m1.bind('<Leave>', self.leavem1)
        self.m2.bind('<Enter>', self.enterm2)
        self.m2.bind('<Leave>', self.leavem2)
        self.m3.bind('<Enter>', self.enterm3)
        self.m3.bind('<Leave>', self.leavem3)
        self.m4.bind('<Enter>', self.enterm4)
        self.m4.bind('<Leave>', self.leavem4)
        self.m5.bind('<Enter>', self.enterm5)
        self.m5.bind('<Leave>', self.leavem5)
        self.m6.bind('<Enter>', self.enterm6)
        self.m6.bind('<Leave>', self.leavem6)
        self.m7.bind('<Enter>', self.enterm7)
        self.m7.bind('<Leave>', self.leavem7)

        
    def hide_mainmenu(self):
        """
        Diese Funktion versteckt die Elemente des Hauptmenues.
        Voraussetzung: Das ertellen muss erfolgt sein.
        """
        self.m1.destroy()
        self.m2.destroy()
        self.m3.destroy()
        self.m4.destroy()
        self.m5.destroy()
        self.m6.destroy()
        self.m7.destroy()
        self.menu.destroy()
        self.menu1.destroy()
        self.menu2.destroy()
        self.menu3.destroy()
        self.listbox.destroy()
        self.root.update()

    #OPTIONS MENU
    def entero1(self, event):
        self.o1.config(bg="white", fg="black")
        
    def leaveo1(self, event):
        self.o1.config(bg=self.label_color, fg=self.text_color)

    def entero2(self, event):
        self.o2.config(bg="white", fg="black")
        
    def leaveo2(self, event):
        self.o2.config(bg=self.label_color, fg=self.text_color)

    def entero3(self, event):
        self.o3.config(bg="white", fg="black")
        
    def leaveo3(self, event):
        self.o3.config(bg=self.label_color, fg=self.text_color)

    def entero4(self, event):
        self.o4.config(bg="white", fg="black")
        
    def leaveo4(self, event):
        self.o4.config(bg=self.label_color, fg=self.text_color)


    def entero5(self, event):
        self.o5.config(bg="white", fg="black")
        
    def leaveo5(self, event):
        self.o5.config(bg=self.label_color, fg=self.text_color)




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
        self.o5 = tkinter.Button(self.option2, text="Zurück", font=("Comic Sans MS", 18), fg=self.text_color, bg=self.label_color, width = self.label_width, command=self.hide_options_menu)
        self.o0.pack()
        self.o1.pack()
        self.o2.pack()
        self.o3.pack()
        self.o4.pack()
        self.o5.pack()
        self.o1.bind('<Enter>', self.entero1)
        self.o1.bind('<Leave>', self.leaveo1)
        self.o2.bind('<Enter>', self.entero2)
        self.o2.bind('<Leave>', self.leaveo2)
        self.o3.bind('<Enter>', self.entero3)
        self.o3.bind('<Leave>', self.leaveo3)
        self.o4.bind('<Enter>', self.entero4)
        self.o4.bind('<Leave>', self.leaveo4)
        self.o5.bind('<Enter>', self.entero5)
        self.o5.bind('<Leave>', self.leaveo5) 
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

    #LEARN MENU
    def create_learnmenu(self, liste):
        """
        Diese Funktion erstellt ein Menu zum lernen
        """
        for i in range(len(liste)):
            pass


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

    def entere1(self, event):
        self.e1.config(bg="white", fg="black")
        
    def leavee1(self, event):
        self.e1.config(bg=self.label_color, fg=self.text_color)

    def entere2(self, event):
        self.e2.config(bg="white", fg="black")
        
    def leavee2(self, event):
        self.e2.config(bg=self.label_color, fg=self.text_color)

    def entere3(self, event):
        self.e3.config(bg="white", fg="black")
        
    def leavee3(self, event):
        self.e3.config(bg=self.label_color, fg=self.text_color)



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
        self.e1.bind('<Enter>', self.entere1)
        self.e1.bind('<Leave>', self.leavee1)
        self.e2.bind('<Enter>', self.entere2)
        self.e2.bind('<Leave>', self.leavee2)
        self.e3.bind('<Enter>', self.entere3)
        self.e3.bind('<Leave>', self.leavee3)
        self.root.update()
        

    def quit_window(self):
        """
        Schließen das Programms
        """
        self.root.destroy()

    def dont_quit_window(self):
        """
        Zeigt Hauptmenue an
        """
        
        self.hide_exit_menu()
        self.create_mainmenu()
        self.root.update()

    def hide_exit_menu(self):
        self.exit.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        
    

    
test = gui("Test", 500, 500, "black", True)
test.create_mainmenu()
tkinter.mainloop()
