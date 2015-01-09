import tkinter
import access

class gui:
    def __init__(self):
        self.__acc=access.funktion()
        self.__set_vars()
        self.__create_window()
        self.__create_mainmenu()
        self.__show_window()
        self.__show_mainmenu()
        tkinter.mainloop()

    
    def __set_vars(self):
        """
        Alle Variablen werden fuer das Programm erstellt werden
        """
        self.__bgcolor    = "#F2F2F2"
        self.__second_color = "orange"
        self.__text_font  = "Courier"
        self.__label_width = 20            #Label-Groesse
        self.__label_bgcolor = "#C6C6C6"   #Label Hintergrundfarbe
        self.__frame_bgcolor = "white"
        self.__text_fgcolor  = "black"     #Label Text Farbe
        self.__label_bgcolor_onmouse = "white"
        
        self.__text_fgcolor_onmouse  = "black"
        self.__menu = ""
        self.__listbox_elems = 20
        self.__listbox_len_name=30

    def __load(self, event=0):
        """Laed das Uebergebene Deck"""
        try:
            x = self.__mainmenu_decks_list_listbox.curselection()[0]
            print(x)
            print(self.__acc.deck_list(self.__acc.get_config("sort"))[x])
            self.__acc.deck_load(self.__acc.deck_list(self.__acc.get_config("sort"))[x])
            return True
        except:
            return False
    
    def __einruecken(self, text, length):
        text=str(text)
        if len(text)>length:
            text = text[:length]
        while(len(text)<length+2):
            text+=" "
        return text
    
    def __einruecken_2(self,text, text_vorne_einruecken_zu):
        while text_vorne_einruecken_zu>len(text):
            text=" "+text
        return text


    def __mainmenu_decks_list_listbox_update(self):
        sort = self.__acc.get_config("sort")
        if sort==None:
            self.__acc.set_config("sort", 0)
            sort=0
        liste = self.__acc.deck_list_info()
        self.__mainmenu_decks_list_listbox.delete(0, "end")
        for elem in liste:
            self.__mainmenu_decks_list_listbox.insert("end", \
                    self.__einruecken(elem[0], self.__listbox_len_name)+\
                    self.__einruecken(elem[1], 11)+\
                    self.__einruecken(elem[2][6:8]+"."+elem[2][4:6]+"."+elem[2][0:4],10)[:-1]+\
                    self.__einruecken_2(elem[3], 4)+" "+\
                    self.__einruecken_2(elem[4], 4))
    
    def __lernen_begin(self, event=0):
        if self.__load():
            self.__hide_menu()    

    def __mainmenu_question_hide(self, event=0):
        self.__mainmenu_question.pack_forget()
        self.__mainmenu_question_label.pack_forget()
        self.__mainmenu_question_buttons.pack_forget()
        self.__mainmenu_question_buttons_1.pack_forget()
        self.__mainmenu_question_buttons_2.pack_forget()
    
    def __mainmenu_loeschen_deck(self, event=0):
        if(self.__load()):
            self.__acc.deck_delete_loaded()
        self.__mainmenu_question_hide()
        self.__mainmenu_decks_list_listbox_update()
        #TODO: bind Esc verlasssen
    
    def __mainmenu_loeschen(self, event=0):
        self.__mainmenu_question_label.config(text="Wollen Sie den\nKartenstapel\nwirklich l\xf6schen?")
        self.__mainmenu_question_buttons_1.config(text="Ja", command=self.__mainmenu_loeschen_deck)
        self.__mainmenu_question_buttons_2.config(text="Nein", command=self.__mainmenu_question_hide)
        self.__mainmenu_question.pack(side="bottom", pady=7)
        self.__mainmenu_question_buttons.pack(side="bottom", pady=5)
        self.__mainmenu_question_buttons_1.pack(side="left", padx=self.__label_width*2//3)
        self.__mainmenu_question_buttons_2.pack(side="left", padx=self.__label_width*2//3)
        self.__mainmenu_question_label.pack(side="top",pady=5)
        #TODO: bind Esc Mainmenu question_hide
    
    def __mainmenu_hinzufuegen(self, event):
        pass #TODO:
    
    def __mainmenu_statistik_reset(self, event):
        pass #TODO:
        
    def __create_window(self):
        """
        Erstellen des Fensters
        Voraussetzung: Variablen muessen erstellt sein
        """
        self.__acc = access.funktion()
        self.__root = tkinter.Tk()
        self.__root.attributes("-fullscreen", True)
        self.__root.config(bg=self.__bgcolor)
        self.__bottom = tkinter.Frame(self.__root, bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__bottom_menu = tkinter.Frame(self.__bottom, bg=self.__frame_bgcolor)
        self.__bottom_menu_1 = tkinter.Button(self.__bottom_menu, text= "Optionen",  font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__bottom_menu_2 = tkinter.Button(self.__bottom_menu, text= "Hilfe",     font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__bottom_menu_3 = tkinter.Button(self.__bottom_menu, text= "Verlassen", font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__button_normal_binds(self.__bottom_menu_1)
        self.__button_normal_binds(self.__bottom_menu_2)
        self.__button_normal_binds(self.__bottom_menu_3)
        self.__head = tkinter.Frame(self.__root, bg=self.__second_color, relief = "flat")
        self.__header = tkinter.Label (self.__root, text= "Discamus", font=(self.__text_font, 30), fg=self.__text_fgcolor, bg="orange", width = self.__root.winfo_screenwidth())
    
    def __show_window(self):
        self.__head.pack(side="top", pady=0)
        self.__header.pack()
        self.__bottom.pack(side="bottom", fill="x")
        self.__bottom_menu.pack(side="bottom")
        self.__bottom_menu_1.pack(side="left", padx=20, pady=5)
        self.__bottom_menu_2.pack(side="left", padx=20, pady=5)
        self.__bottom_menu_3.pack(side="left", padx=20, pady=5)
        self.__listbox_elems=(self.__root.winfo_screenheight()-250)/30
        self.__listbox_len_name=(self.__root.winfo_screenwidth()-905)//15
    
    def __button_enter(self, button):
        button.config(bg=self.__label_bgcolor_onmouse, fg=self.__text_fgcolor_onmouse)

    def __button_leave(self, button):
        button.config(bg=self.__label_bgcolor, fg=self.__text_fgcolor)

    def __button_normal_binds(self, button):
        button.bind('<Enter>',lambda event: self.__button_enter(button))
        button.bind('<Leave>',lambda event: self.__button_leave(button))

    def __button_normal_config(self, button, Master=None, Text=None, Command=None):
        if not type(Master==None):
            button.config(master = Master)
        if not type(Text==None):
            button.config(text = Text)
        if not type(Command==None):
            button.config(command=Command)
        button.config(font  = (self.__text_font, 18) ,\
                      fg    = self.__text_fgcolor    ,\
                      bg    = self.__label_bgcolor   ,\
                      width = self.__label_width)
        
    def __create_mainmenu(self):
        #Frames
        self.__mainmenu                 = tkinter.Frame(self.__root,                                            bd = 5, relief = "flat")
        self.__mainmenu_decks           = tkinter.Frame(self.__mainmenu,               bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_decks_list      = tkinter.Frame(self.__mainmenu_decks,         bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_decks_list_head = tkinter.Frame(self.__mainmenu_decks_list,    bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_decks_scrollbar = tkinter.Frame(self.__mainmenu_decks_list,    bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_options_question= tkinter.Frame(self.__mainmenu_decks)
        self.__mainmenu_options   = tkinter.Frame(self.__mainmenu_decks,         bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_question        = tkinter.Frame(self.__mainmenu_decks,bg=self.__label_bgcolor, bd = 5, relief = "flat" )
        self.__mainmenu_question_buttons= tkinter.Frame(self.__mainmenu_question,bg=self.__label_bgcolor)
        
        #Links
        self.__mainmenu_decks_list_head_1 = tkinter.Button(self.__mainmenu_decks_list_head, text= self.__einruecken("Name",self.__listbox_len_name)[:-2],font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0) 
        self.__mainmenu_decks_list_head_2 = tkinter.Button(self.__mainmenu_decks_list_head, text= self.__einruecken("Kategorie",12)[:-2],                font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0)
        self.__mainmenu_decks_list_head_3 = tkinter.Button(self.__mainmenu_decks_list_head, text= self.__einruecken("Datum",9)[:-2],                     font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0)
        self.__mainmenu_decks_list_head_4 = tkinter.Button(self.__mainmenu_decks_list_head, text= "Karten",                                              font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0)
        self.__mainmenu_decks_list_head_5 = tkinter.Button(self.__mainmenu_decks_list_head, text= " %",                                                  font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0)
        
        self.__mainmenu_decks_list_listbox = tkinter.Listbox(self.__mainmenu_decks_list, font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, width = 65, height = self.__listbox_elems, bd=0)
        self.__mainmenu_decks_list_listbox.config(selectbackground=self.__label_bgcolor_onmouse,selectforeground=self.__text_fgcolor_onmouse)
        self.__mainmenu_decks_scrollbar_1 = tkinter.Scrollbar(self.__mainmenu_decks_scrollbar)
        self.__mainmenu_decks_scrollbar_1.config(command=self.__mainmenu_decks_list_listbox.yview)
        self.__mainmenu_decks_list_listbox.bind("F5", self.__mainmenu_decks_list_listbox_update)
        self.__mainmenu_decks_list_listbox.bind("<Return>", self.__lernen_begin)
        self.__mainmenu_decks_list_listbox.bind("<Double-Button>", self.__lernen_begin)
        
        #Rechts
        self.__mainmenu_options_1 = tkinter.Button(self.__mainmenu_options, text= "Lernen",     font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__lernen_begin)
        self.__mainmenu_options_2 = tkinter.Button(self.__mainmenu_options, text= "Testen",     font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__mainmenu_options_3 = tkinter.Button(self.__mainmenu_options, text= "Hinzuf\xfcgen", font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__mainmenu_options_4 = tkinter.Button(self.__mainmenu_options, text= "Bearbeiten", font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__mainmenu_options_5 = tkinter.Button(self.__mainmenu_options, text= "L\xf6schen", font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__mainmenu_loeschen)
        self.__button_normal_binds(self.__mainmenu_options_1)
        self.__button_normal_binds(self.__mainmenu_options_2)
        self.__button_normal_binds(self.__mainmenu_options_3)
        self.__button_normal_binds(self.__mainmenu_options_4)
        self.__button_normal_binds(self.__mainmenu_options_5)
        
        self.__mainmenu_question_buttons_1 = tkinter.Button(self.__mainmenu_question_buttons, font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//3)
        self.__mainmenu_question_buttons_2 = tkinter.Button(self.__mainmenu_question_buttons, font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//3)
        self.__mainmenu_question_label = tkinter.Label(self.__mainmenu_question, text="1",font=(self.__text_font, 18), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        
    def __show_mainmenu(self):
        if self.__menu == "":
            self.__menu = "mainmenu"
            self.__mainmenu.pack(pady=20)
            self.__mainmenu_decks.pack(side="top")
            self.__mainmenu_decks_list.pack(side="left")
            if len(self.__acc.deck_list())>self.__listbox_elems:
                self.__mainmenu_decks_scrollbar.pack(side="right", fill="y")
            self.__mainmenu_options.pack(side="top", pady=30)
            self.__mainmenu_decks_list_listbox_update()
            self.__mainmenu_decks_list_head.pack(side="top")
            self.__mainmenu_decks_list_head_1.pack(side="left")
            self.__mainmenu_decks_list_head_2.pack(side="left")
            self.__mainmenu_decks_list_head_3.pack(side="left")
            self.__mainmenu_decks_list_head_4.pack(side="left")
            self.__mainmenu_decks_list_head_5.pack(side="right")
            self.__mainmenu_decks_list_listbox.pack(side="bottom")
            self.__mainmenu_decks_scrollbar_1.pack(side="right",fill="y")
            self.__mainmenu_options_1.pack(side="top", pady=5, padx=10)
            self.__mainmenu_options_2.pack(side="top", pady=5, padx=10)
            self.__mainmenu_options_3.pack(side="top", pady=5, padx=10)
            self.__mainmenu_options_4.pack(side="top", pady=5, padx=10)
            self.__mainmenu_options_5.pack(side="top", pady=5, padx=10)
            
    
    def __hide_mainmenu(self):
        self.__menu = ""
        self.__mainmenu_options_1.pack_forget()
        self.__mainmenu_options_2.pack_forget()
        self.__mainmenu_options_3.pack_forget()
        self.__mainmenu_options_4.pack_forget()
        self.__mainmenu_options_5.pack_forget()
        self.__mainmenu_options.pack_forget()
        self.__mainmenu_decks_list_head_1.pack_forget()
        self.__mainmenu_decks_list_head_2.pack_forget()
        self.__mainmenu_decks_list_head_3.pack_forget()
        self.__mainmenu_decks_list_head_4.pack_forget()
        self.__mainmenu_decks_list_head_5.pack_forget()
        self.__mainmenu_decks_list_listbox.pack_forget()
        self.__mainmenu_decks_scrollbar_1.pack_forget()
        self.__mainmenu_decks_list_head.pack_forget()
        self.__mainmenu_decks_list.pack_forget()
        self.__mainmenu_decks_scrollbar.pack_forget()
        self.__mainmenu.pack_forget()
        self.__mainmenu_question.pack_forget()

    def __hide_menu(self):
        if self.__menu=="mainmenu":
            self.__hide_mainmenu()
"""
    def lernen_begin():
        ""
        Funktion, welche beim vom Hauptmenue zum Lernmenu springt
        ""
        print(1)
        hide_menu()
        #if select():
"""
gui = gui()