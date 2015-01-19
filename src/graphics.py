# -*- coding: utf-8 -*-
import tkinter
import access

#FINISH: mainmenu
#FINISH: exitmenu
#FINISH: lernmenu
#FINSIH: testmenu #TODO: statistikmenu

#TODO: deckmenu
#TODO: optionmenu
#TODO: hilfsmenu

class gui:
    def __init__(self):
        self.__acc=access.funktion()
        self.__set_vars()
        self.__create_window()
        self.__create_mainmenu()
        self.__create_lernmenu()
        self.__create_testmenu()
        self.__create_deckmenu()
        self.__create_exitmenu()
        self.__show_window()
        self.__show_mainmenu()
        tkinter.mainloop()

    # - - - - - - - - INIT - - - - - - - - 
    
    def __set_vars(self):
        """
        Alle Variablen werden fuer das Programm erstellt werden
        """
        self.__bgcolor    = "#F2F2F2"
        self.__second_color = "orange"
        self.__third_color = "white"
        self.__text_font  = "Courier"
        self.__label_width = int()            #Label-Groesse
        self.__label_bgcolor = "#DDDDDD"   #Label Hintergrundfarbe
        self.__frame_bgcolor = "white"
        self.__text_fgcolor  = "black"     #Label Text Farbe
        self.__label_bgcolor_onmouse = "white"
        self.__text_fgcolor_onmouse  = "black"
        self.__menu = ""
        self.__last_menu = ""
        self.__listbox_elems = int()
        self.__text_height=int()
    def __button_enter(self, button):
        button.config(bg=self.__label_bgcolor_onmouse, fg=self.__text_fgcolor_onmouse)

    def __button_leave(self, button):
        button.config(bg=self.__label_bgcolor, fg=self.__text_fgcolor)

    def __button_normal_binds(self, button):
        button.bind('<Enter>',lambda event: self.__button_enter(button))
        button.bind('<Leave>',lambda event: self.__button_leave(button))
    
    # - - - - - - - - Laenge von Strings veraendern - - - - - - - -
        
    def __text_kuerzen(self, text, maxlength):
        """
        Falls Text laenger als maxlength ist, wird dieser gekuerzt und ein ... wird am Ende hinzugefuegt
        """
        text=str(text)
        if len(text)>maxlength:
            text = text[:maxlength-1]+"\u2026"
        return text
    
    def __einruecken_hinten(self, text, length):
        text=str(text)
        text=self.__text_kuerzen(text, length)
        while(len(text)<length+2):
            text+=" "
        return text
    
    def __einruecken_vorne(self,text, text_vorne_einruecken_zu):
        while text_vorne_einruecken_zu>len(str(text)):
            text=" "+str(text)
        return text
    
    # - - - - - - - - Wechsel zuwischen Menues - - - - - - - -
    
    def __lernen_begin(self, event=0):
        """
        Voraussetzung: Menu muss mainmenu sein.
        """
        if self.__load():
            if self.__acc.deck_hascards():
                self.__hide_menu()
                self.__show_lernmenu()
            else:
                self.__mainmenu_error_deck_no_cards()
        else:
            self.__mainmenu_error_no_deck_selected()    

    def __testen_begin(self, event=0):
        if self.__load():
            if self.__acc.deck_hascards():
                self.__hide_menu()
                self.__show_testmenu()
            else:
                self.__mainmenu_error_deck_no_cards()
        else:
            self.__mainmenu_error_no_deck_selected()

    def __lernmenu_answered(self, event=0):
        if self.__acc.card_correct(self.__lernmenu_answer_entry.get()):
            if self.__acc.deck_hascards():
                self.__lernmenu_newCard()
            else:
                self.__goto_mainmenu()
                #TODO:self.__goto_statistikmenu()
        else:
            self.__lernmenu_give_answer()

    def __testmenu_answered(self, event=0):
        self.__acc.card_correct(self.__testmenu_answer_entry.get())
        if self.__acc.deck_hascards():
            self.__testmenu_newCard()
        else:
            #TODO: Zeige Statistik
            self.__goto_mainmenu()

    def __goto_deckmenu(self, event=0):
        """
        Voraussetzung: Menu muss mainmenu sein.
        """
        if self.__load():
            self.__hide_mainmenu()
            self.__show_deckmenu()
        else:
            self.__mainmenu_error_no_deck_selected() 

    def __goto_mainmenu(self, event=0):
        self.__hide_menu()
        self.__show_mainmenu()

    def __exit(self, event=0):
        self.__hide_menu()
        self.__show_exitmenu()
    
    def __exit_back(self, event=0):
        self.__hide_exitmenu()
        self.__show_last_menu()
    
    # - - - - - - - - FENSTER - - - - - - - - - - - - - - - - - - - - - - -
    def __create_window(self):
        """
        Erstellen des Fensters
        Voraussetzung: Variablen muessen erstellt sein
        """
        self.__acc = access.funktion()
        self.__root = tkinter.Tk()
        self.__root.attributes("-fullscreen", True)
        self.__root.config(bg=self.__bgcolor)
        self.__head = tkinter.Frame(self.__root, bg=self.__second_color, relief = "flat")
        self.__header = tkinter.Label (self.__root, text= "Discamus", font=(self.__text_font, 30), fg=self.__text_fgcolor, bg=self.__second_color, width = self.__root.winfo_screenwidth())
        self.__label_width = 20# self.__root.winfo_screenwidth()//60
        self.__text_height=self.__root.winfo_screenwidth()//80# self.__label_width*22//24
        self.__listbox_elems=int((self.__root.winfo_screenheight()-225)//(self.__text_height*1.5))
        self.__bottom = tkinter.Frame(self.__root, bg=self.__third_color, bd = 5, relief = "flat")
        self.__bottom_menu = tkinter.Frame(self.__bottom, bg=self.__third_color)
        self.__bottom_menu_1 = tkinter.Button(self.__bottom_menu, text= "Optionen",  font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__bottom_menu_2 = tkinter.Button(self.__bottom_menu, text= "Hilfe",     font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__bottom_menu_3 = tkinter.Button(self.__bottom_menu, text= "Verlassen", font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__exit)
        self.__button_normal_binds(self.__bottom_menu_1)
        self.__button_normal_binds(self.__bottom_menu_2)
        self.__button_normal_binds(self.__bottom_menu_3)
        #self.__root.wm_protocol("WM_DELETE_WINDOW", self.__exit)
    
    def __show_window(self):
        self.__head.pack(side="top", fill="x")
        self.__header.pack()
        self.__bottom.pack(side="bottom", fill="x")
        self.__bottom_menu.pack(side="bottom")
        self.__bottom_menu_1.pack(side="left", padx=20, pady=5)
        self.__bottom_menu_2.pack(side="left", padx=20, pady=5)
        self.__bottom_menu_3.pack(side="left", padx=20, pady=5)
        
    def __destroy_window(self, event=0):
        self.__root.destroy()
    
    # - - - - - - - - MAINMENU - - - - - - - - - - - - - - - - - - - - - - -

    def __load(self, event=0):
        """Laed das Uebergebene Deck"""
        try:
            x = self.__mainmenu_decks_list_listbox.curselection()[0]
            self.__acc.deck_load(self.__acc.deck_list_noUpdate(self.__acc.get_config("sort"))[x])
            return True
        except:
            return False

    def __mainmenu_decks_list_listbox_sort(self, elem):
        if self.__acc.get_config("sort")==elem:
            self.__acc.set_config("sort", -elem)
        else:
            self.__acc.set_config("sort", elem)
        self.__mainmenu_decks_list_listbox_update()

    def __mainmenu_decks_list_listbox_update(self):
        sort = self.__acc.get_config("sort")
        if sort==None:
            self.__acc.set_config("sort", 0)
            sort=0
        liste = self.__acc.deck_list_info(self.__acc.get_config("sort"))
        self.__mainmenu_decks_list_listbox.delete(0, "end")
        for elem in liste:
            self.__mainmenu_decks_list_listbox.insert("end", \
                    self.__einruecken_hinten(elem[0], 30)+\
                    self.__einruecken_hinten(elem[1], 12)+\
                    self.__einruecken_hinten(elem[2][6:8]+"."+elem[2][4:6]+"."+elem[2][0:4],10)[:-1]+\
                    self.__einruecken_vorne(elem[3], 4)+" "+\
                    self.__einruecken_vorne(elem[4], 4))
        if len(self.__acc.deck_list())>self.__listbox_elems:
            self.__mainmenu_decks_scrollbar_1.pack(side="right", fill="y")
        else:
            self.__mainmenu_decks_scrollbar_1.pack_forget()
    
    def __mainmenu_question_hide(self, event=0):
        self.__mainmenu_question.pack_forget()
        self.__mainmenu_question_label.pack_forget()
        self.__mainmenu_question_label_frame.pack_forget()
        self.__mainmenu_question_buttons.pack_forget()
        self.__mainmenu_question_buttons_1.pack_forget()
        self.__mainmenu_question_buttons_2.pack_forget()
        self.__mainmenu_question_entry.pack_forget()
        self.__mainmenu_question_entry_1.pack_forget()
        self.__mainmenu_question_entry_2.pack_forget()
        self.__mainmenu_question_entry_3.pack_forget()
        self.__mainmenu_question_buttons_1.config(width = self.__label_width//3)
        self.__mainmenu_question_buttons_2.config(width = self.__label_width//3)
    
    def __mainmenu_error_deck_no_cards(self):
        self.__mainmenu_question_hide()
        self.__mainmenu_question_label.config(text="Fehler:\nDer Kartenstapel ist leer.", wraplength=self.__label_width*15)
        self.__mainmenu_question_buttons_2.config(text="OK", command=self.__mainmenu_question_hide)
        self.__mainmenu_question.pack(side="bottom", pady=7)
        self.__mainmenu_question_label_frame.pack(side="top", fill="y",padx=0)
        self.__mainmenu_question_label.pack(side="left",pady=5)
        self.__mainmenu_question_buttons.pack(side="bottom", pady=5)
        self.__mainmenu_question_buttons_2.pack(side="left", padx=self.__label_width*2//3)
        self.__mainmenu_question_buttons_2.focus_set()
    
    def __mainmenu_error_no_deck_selected(self, event=0):
        self.__mainmenu_question_hide()
        self.__mainmenu_question_label.config(text="Fehler:\nKein Kartenstapel ausgew\xe4hlt.",wraplength=self.__label_width*15)
        self.__mainmenu_question_buttons_2.config(text="OK", command=self.__mainmenu_question_hide)
        self.__mainmenu_question.pack(side="bottom", pady=7)
        self.__mainmenu_question_buttons.pack(side="bottom", pady=5)
        self.__mainmenu_question_buttons_2.pack(side="left", padx=self.__label_width*2//3)
        self.__mainmenu_question_buttons_2.focus_set()
        self.__mainmenu_question_label_frame.pack(side="top", fill="y")
        self.__mainmenu_question_label.pack(side="left",pady=5)
    
    def __mainmenu_loeschen_deck(self, event=0):
        self.__acc.deck_delete_loaded()
        self.__mainmenu_question_hide()
        self.__mainmenu_decks_list_listbox_update()
        #TODO: bind Esc verlasssen
    
    def __mainmenu_hinzufuegen_deck(self, event=0):
        name=self.__mainmenu_question_entry_1.get()
        kategorie=self.__mainmenu_question_entry_2.get()
        beschreibung=self.__mainmenu_question_entry_3.get()
        self.__acc.deck_create(name,kategorie,beschreibung)
        self.__mainmenu_decks_list_listbox_update()
        self.__mainmenu_question_hide()
    
    def __mainmenu_deck_reset(self, event=0):
        self.__acc.deck_statistik_reset()
        self.__mainmenu_question_hide()
    
    def __mainmenu_hinzufuegen(self, event=0):
        self.__mainmenu_question_hide()
        self.__mainmenu_question.pack(side="bottom", pady=5)
        self.__mainmenu_question_entry.pack(side="top", pady=7)
        self.__mainmenu_question_entry_1.delete(0, "end")
        self.__mainmenu_question_entry_1.focus_set()
        self.__mainmenu_question_entry_1.insert(0, "Name")
        self.__mainmenu_question_entry_1.pack(side="top")
        self.__mainmenu_question_entry_2.delete(0, "end")
        self.__mainmenu_question_entry_2.insert(0, "Kategorie")
        self.__mainmenu_question_entry_2.pack(side="top")
        self.__mainmenu_question_entry_3.delete(0, "end")
        self.__mainmenu_question_entry_3.insert(0, "Beschreibung")
        self.__mainmenu_question_entry_3.pack(side="top")
        self.__mainmenu_question_buttons_1.config(text="Ok", command=self.__mainmenu_hinzufuegen_deck)
        self.__mainmenu_question_buttons_2.config(text="Abbrechen", command=self.__mainmenu_question_hide)
        self.__mainmenu_question_buttons_1.config(width = self.__label_width*5//10)
        self.__mainmenu_question_buttons_2.config(width = self.__label_width*5//10)
        self.__mainmenu_question.pack(side="bottom", pady=7)
        self.__mainmenu_question_buttons.pack(side="bottom", pady=5)
        self.__mainmenu_question_buttons_1.pack(side="left", padx=0)
        self.__mainmenu_question_buttons_2.pack(side="left", padx=0)
        
        
    
    def __mainmenu_loeschen(self, event=0):
        self.__mainmenu_question_hide()
        if(self.__load()):
            self.__mainmenu_question_label.config(text="Wollen Sie den Kartenstapel \""+ self.__text_kuerzen(self.__acc.deck_info()[0],17) +"\" wirklich l\xf6schen?", wraplength=self.__label_width*15)
            self.__mainmenu_question_buttons_1.config(text="Ja", command=self.__mainmenu_loeschen_deck)
            self.__mainmenu_question_buttons_2.config(text="Nein", command=self.__mainmenu_question_hide)
            self.__mainmenu_question.pack(side="bottom", pady=7)
            self.__mainmenu_question_buttons.pack(side="bottom", pady=5)
            self.__mainmenu_question_buttons_1.pack(side="left", padx=self.__label_width*2//3)
            self.__mainmenu_question_buttons_2.pack(side="left", padx=self.__label_width*2//3)
            self.__mainmenu_question_label_frame.pack(side="top", fill="y")
            self.__mainmenu_question_label.pack(side="left",pady=5)
            #self.__mainmenu_question.bind("<Escape>", self.__mainmenu_question_hide)
            #self.__mainmenu_question.bind("<Return>", self.__mainmenu_loeschen_deck)
            #TODO: bind Esc Mainmenu question_hide
        else:
            self.__mainmenu_error_no_deck_selected()

    def __button_normal_config(self, button, Master=None, Text=None, Command=None):
        if not type(Master==None):
            button.config(master = Master)
        if not type(Text==None):
            button.config(text = Text)
        if not type(Command==None):
            button.config(command=Command)
        button.config(font  = (self.__text_font, self.__text_height) ,\
                      fg    = self.__text_fgcolor    ,\
                      bg    = self.__label_bgcolor   ,\
                      width = self.__label_width)
        
    def __create_mainmenu(self):
        #Frames
        self.__mainmenu                      = tkinter.Frame(self.__root,                                            bd = 5, relief = "flat")
        self.__mainmenu_decks                = tkinter.Frame(self.__mainmenu,               bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_decks_list           = tkinter.Frame(self.__mainmenu_decks,         bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_decks_list_head      = tkinter.Frame(self.__mainmenu_decks_list,    bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_decks_scrollbar      = tkinter.Frame(self.__mainmenu_decks_list,    bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_options_question     = tkinter.Frame(self.__mainmenu_decks)
        self.__mainmenu_options              = tkinter.Frame(self.__mainmenu_decks,         bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__mainmenu_question             = tkinter.Frame(self.__mainmenu_decks,         bg=self.__label_bgcolor, bd = 5, relief = "flat" )
        self.__mainmenu_question_label_frame = tkinter.Frame(self.__mainmenu_question, bg=self.__label_bgcolor)
        self.__mainmenu_question_buttons     = tkinter.Frame(self.__mainmenu_question,      bg=self.__label_bgcolor)
        self.__mainmenu_question_entry       = tkinter.Frame(self.__mainmenu_question,      bg=self.__label_bgcolor)
        
        
        #Links
        self.__mainmenu_decks_list_head_1 = tkinter.Label(self.__mainmenu_decks_list_head, text= self.__einruecken_hinten("Name",30),      font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0) 
        self.__mainmenu_decks_list_head_2 = tkinter.Label(self.__mainmenu_decks_list_head, text= self.__einruecken_hinten("Kategorie",12), font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0)
        self.__mainmenu_decks_list_head_3 = tkinter.Label(self.__mainmenu_decks_list_head, text= self.__einruecken_hinten("Datum",10)[:-1],font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0)
        self.__mainmenu_decks_list_head_4 = tkinter.Label(self.__mainmenu_decks_list_head, text= "Karten",                          font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0)
        self.__mainmenu_decks_list_head_5 = tkinter.Label(self.__mainmenu_decks_list_head, text= "  %",                             font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0)
        
        self.__mainmenu_decks_list_head_1.bind("<Button-1>",lambda event:self.__mainmenu_decks_list_listbox_sort(1))
        self.__mainmenu_decks_list_head_2.bind("<Button-1>",lambda event:self.__mainmenu_decks_list_listbox_sort(2))
        self.__mainmenu_decks_list_head_3.bind("<Button-1>",lambda event:self.__mainmenu_decks_list_listbox_sort(3))
        self.__mainmenu_decks_list_head_4.bind("<Button-1>",lambda event:self.__mainmenu_decks_list_listbox_sort(4))
        self.__mainmenu_decks_list_head_5.bind("<Button-1>",lambda event:self.__mainmenu_decks_list_listbox_sort(5))
        
        self.__mainmenu_decks_list_listbox = tkinter.Listbox(self.__mainmenu_decks_list, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, width = 66, height = self.__listbox_elems, bd=0, activestyle="dotbox")
        self.__mainmenu_decks_list_listbox.config(selectbackground=self.__label_bgcolor_onmouse,selectforeground=self.__text_fgcolor_onmouse)
        self.__mainmenu_decks_scrollbar_1 = tkinter.Scrollbar(self.__mainmenu_decks_scrollbar)
        self.__mainmenu_decks_scrollbar_1.config(command=self.__mainmenu_decks_list_listbox.yview)
        self.__mainmenu_decks_list_listbox.config(yscrollcommand=self.__mainmenu_decks_scrollbar_1.set)
        self.__mainmenu_decks_list_listbox.bind("F5", self.__mainmenu_decks_list_listbox_update)
        self.__mainmenu_decks_list_listbox.bind("<Return>", self.__lernen_begin)
        self.__mainmenu_decks_list_listbox.bind("<Double-Button>", self.__lernen_begin)
        
        #Rechts
        self.__mainmenu_options_1 = tkinter.Button(self.__mainmenu_options, text= "Lernen",        font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__lernen_begin)
        self.__mainmenu_options_2 = tkinter.Button(self.__mainmenu_options, text= "Testen",        font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__testen_begin)
        self.__mainmenu_options_3 = tkinter.Button(self.__mainmenu_options, text= "Hinzuf\xfcgen", font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__mainmenu_hinzufuegen)
        self.__mainmenu_options_4 = tkinter.Button(self.__mainmenu_options, text= "Bearbeiten",    font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__goto_deckmenu)
        self.__mainmenu_options_5 = tkinter.Button(self.__mainmenu_options, text= "L\xf6schen",    font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width, command=self.__mainmenu_loeschen)
        self.__button_normal_binds(self.__mainmenu_options_1)
        self.__button_normal_binds(self.__mainmenu_options_2)
        self.__button_normal_binds(self.__mainmenu_options_3)
        self.__button_normal_binds(self.__mainmenu_options_4)
        self.__button_normal_binds(self.__mainmenu_options_5)
        
        
        self.__mainmenu_question_entry_1 = tkinter.Entry(self.__mainmenu_question_entry, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__mainmenu_question_entry_2 = tkinter.Entry(self.__mainmenu_question_entry, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__mainmenu_question_entry_3 = tkinter.Entry(self.__mainmenu_question_entry, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__mainmenu_question_buttons_1 = tkinter.Button(self.__mainmenu_question_buttons, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//3)
        self.__mainmenu_question_buttons_2 = tkinter.Button(self.__mainmenu_question_buttons, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//3)
        self.__mainmenu_question_label = tkinter.Label(self.__mainmenu_question_label_frame, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        
        self.__button_normal_binds(self.__mainmenu_question_buttons_1)
        self.__button_normal_binds(self.__mainmenu_question_buttons_2)
        
        
    def __show_mainmenu(self):
        if self.__menu == "":
            self.__menu = "mainmenu"
            self.__mainmenu.pack(pady=20)
            self.__mainmenu_decks.pack(side="top")
            self.__mainmenu_decks_list.pack(side="left")
            print(len(self.__acc.deck_list()), self.__listbox_elems)
            self.__mainmenu_decks_scrollbar.pack(side="right",fill="y")
            self.__mainmenu_options.pack(side="top", pady=20)
            self.__mainmenu_decks_list_listbox_update()
            self.__mainmenu_decks_list_head.pack(side="top")
            self.__mainmenu_decks_list_head_1.pack(side="left")
            self.__mainmenu_decks_list_head_2.pack(side="left")
            self.__mainmenu_decks_list_head_3.pack(side="left")
            self.__mainmenu_decks_list_head_4.pack(side="left")
            self.__mainmenu_decks_list_head_5.pack(side="right")
            self.__mainmenu_decks_list_listbox.pack(side="bottom")
            self.__mainmenu_options_1.pack(side="top", pady=2, padx=10)
            self.__mainmenu_options_2.pack(side="top", pady=2, padx=10)
            self.__mainmenu_options_3.pack(side="top", pady=2, padx=10)
            self.__mainmenu_options_4.pack(side="top", pady=2, padx=10)
            self.__mainmenu_options_5.pack(side="top", pady=2, padx=10)
    
    def __hide_mainmenu(self):
        self.__menu = ""
        self.__last_menu="mainmenu"
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
        self.__mainmenu_question_hide()
    
    #- - - - - - - - Lernmenu - - - - - - - -
    def __create_lernmenu(self):
        self.__lernmenu = tkinter.Frame(self.__root, bg=self.__bgcolor)
        self.__lernmenu_frame = tkinter.Frame(self.__lernmenu, bg=self.__frame_bgcolor)
        self.__lernmenu_titel = tkinter.Frame(self.__lernmenu_frame, bg=self.__frame_bgcolor)
        self.__lernmenu_question = tkinter.Frame(self.__lernmenu_frame,bg=self.__frame_bgcolor)
        self.__lernmenu_answer = tkinter.Frame(self.__lernmenu_frame,bg=self.__frame_bgcolor)
        self.__lernmenu_buttons = tkinter.Frame(self.__lernmenu_frame, bg=self.__frame_bgcolor)
        self.__lernmenu_info = tkinter.Frame(self.__lernmenu_frame, bg=self.__frame_bgcolor)
        
        self.__lernmenu_titel_label      = tkinter.Label(self.__lernmenu_titel,font=(self.__text_font, self.__text_height*2), fg=self.__text_fgcolor, bg=self.__frame_bgcolor)
        self.__lernmenu_question_label   = tkinter.Label(self.__lernmenu_question, font=(self.__text_font, self.__text_height*2), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, width=self.__text_height*2)
        self.__lernmenu_answer_entry     = tkinter.Entry(self.__lernmenu_answer  , font=(self.__text_font, self.__text_height*2), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, width=self.__text_height*2, justify="center")
        self.__lernmenu_info_label       = tkinter.Label(self.__lernmenu_info, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor)
        self.__lernmenu_answer_button_1  = tkinter.Button(self.__lernmenu_buttons, text = "OK", font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width=self.__label_width, command = self.__lernmenu_answered)
        self.__lernmenu_answer_button_2  = tkinter.Button(self.__lernmenu_buttons, text = "\xdcberspringen", font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width=self.__label_width, command = self.__lernmenu_newCard)
        
        self.__button_normal_binds(self.__lernmenu_answer_button_1)
        self.__button_normal_binds(self.__lernmenu_answer_button_2)
        
    def __show_lernmenu(self):
        if self.__menu=="":
            self.__menu = "lernmenu"
            self.__lernmenu.pack(pady=(self.__root.winfo_screenheight()-420)//2)
            self.__lernmenu_frame.pack(ipadx=30, ipady=10)
            self.__lernmenu_titel_label.config(text=self.__text_kuerzen(self.__acc.deck_info()[0],33))
            self.__lernmenu_titel.pack(pady=10)
            self.__lernmenu_titel_label.pack()
            self.__lernmenu_question.pack()
            self.__lernmenu_question_label.config(text=self.__text_kuerzen(self.__acc.random_card(),33))
            self.__lernmenu_question_label.pack(pady=10)
            self.__lernmenu_answer.pack(pady=10)
            self.__lernmenu_answer_entry.pack()
            self.__lernmenu_info.pack(side="left", padx=30)
            self.__lernmenu_info_label.config(text=str(self.__acc.numberOfCardsLearned())+"/"+str(self.__acc.numberOfCards()))
            self.__lernmenu_info_label.pack(side="left")
            self.__lernmenu_buttons.pack(side="right", padx=30)
            self.__lernmenu_answer_button_2.pack(side="right", padx=10)
            self.__lernmenu_answer_button_1.config(command=self.__lernmenu_answered)
            self.__lernmenu_answer_button_1.pack(side="right", padx=10)
            self.__lernmenu_answer_entry.config(state='normal')
            self.__lernmenu_answer_entry.bind("<Return>", self.__lernmenu_answered)

    def __hide_lernmenu(self):
        self.__last_menu = self.__menu
        self.__menu=""
        self.__lernmenu.pack_forget()
    
    def __lernmenu_give_answer(self):
        self.__lernmenu_answer_button_1.config(command=self.__lernmenu_lastCard)
        self.__lernmenu_answer_entry.delete(0, "end")
        self.__lernmenu_answer_entry.insert("end", "Antwort: " + self.__acc.last_card_answer())
        self.__lernmenu_answer_entry.config(state='disabled')
    
    def __lernmenu_newCard(self, event=0):
        if self.__acc.deck_hascards():
            self.__lernmenu_question_label.config(text=self.__acc.random_card())
            self.__lernmenu_answer_button_1.config(command=self.__lernmenu_answered)
            self.__lernmenu_answer_entry.pack()
            self.__lernmenu_answer_entry.config(state='normal')
            self.__lernmenu_info_label.config(text=str(self.__acc.numberOfCardsLearned())+"/"+str(self.__acc.numberOfCards()))
            self.__lernmenu_answer_entry.delete(0, "end")
        else:
            self.__goto_mainmenu()
            #TODO: self.__goto_statistikmenu()
    
    def __lernmenu_lastCard(self, event=0):
        self.__lernmenu_answer_button_1.config(command=self.__lernmenu_answered)
        self.__lernmenu_answer_entry.config(state='normal')
        self.__lernmenu_answer_entry.delete(0, "end")
    
    def __show_lernmenu_lastCard(self):
        self.__last_menu=self.__menu
        self.__menu = "lernmenu"
        self.__lernmenu_answer_button_1.config(command=self.__lernmenu_answered)
        self.__lernmenu.pack(pady=(self.__root.winfo_screenheight()-410)//2)
        self.__lernmenu_frame.pack()
        self.__lernmenu_question.pack()
        self.__lernmenu_question_label.config(text=self.__acc.last_card())
        self.__lernmenu_answer_entry.config(state='normal')
        self.__lernmenu_answer_entry.delete(0,"end")
        self.__lernmenu_question_label.pack()
        self.__lernmenu_answer.pack()
        self.__lernmenu_answer_entry.pack()
    
    #- - - - - - - - Testmenu - - - - - - - -
    def __create_testmenu(self):
        self.__testmenu = tkinter.Frame(self.__root, bg=self.__bgcolor)
        self.__testmenu_frame = tkinter.Frame(self.__testmenu, bg=self.__frame_bgcolor)
        self.__testmenu_titel = tkinter.Frame(self.__lernmenu_frame, bg=self.__frame_bgcolor)
        self.__testmenu_question = tkinter.Frame(self.__testmenu_frame,bg=self.__frame_bgcolor)
        self.__testmenu_answer = tkinter.Frame(self.__testmenu_frame,bg=self.__frame_bgcolor)
        self.__testmenu_buttons = tkinter.Frame(self.__testmenu_frame, bg=self.__frame_bgcolor)
        self.__testmenu_info = tkinter.Frame(self.__testmenu_frame, bg=self.__frame_bgcolor)
        
        self.__testmenu_titel_label    = tkinter.Label(self.__testmenu_titel,font=(self.__text_font, self.__text_height*2), fg=self.__text_fgcolor, bg=self.__frame_bgcolor)
        self.__testmenu_question_label = tkinter.Label(self.__testmenu_question, font=(self.__text_font, self.__text_height*2), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, width=self.__text_height*2)
        self.__testmenu_answer_entry   = tkinter.Entry(self.__testmenu_answer, font=(self.__text_font, self.__text_height*2), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, width=self.__text_height*2, justify="center")
        self.__testmenu_info_label     = tkinter.Label(self.__testmenu_info, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor)
        self.__testmenu_answer_button  = tkinter.Button(self.__testmenu_buttons, text = "OK", font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width=self.__label_width, command = self.__testmenu_answered)

        
    def __show_testmenu(self):
        if self.__menu=="":
            self.__menu = "testmenu"
            self.__testmenu.pack(pady=(self.__root.winfo_screenheight()-410)//2)
            self.__testmenu_frame.pack(ipadx=30, ipady=10)
            self.__testmenu_titel.pack(pady=10)
            self.__testmenu_titel_label.config(text=self.__text_kuerzen(self.__acc.deck_info()[0],33))
            self.__testmenu_titel_label.pack()
            self.__testmenu_question.pack()
            self.__testmenu_question_label.config(text=self.__text_kuerzen(self.__acc.random_card(),33))
            self.__testmenu_question_label.pack(pady=10)
            self.__testmenu_answer.pack(pady=10)
            self.__testmenu_answer_entry.pack()
            self.__testmenu_info.pack(side="left", padx=30)
            self.__testmenu_info_label.config(text=str(self.__acc.numberOfCardsLearned())+"/"+str(self.__acc.numberOfCards()))
            self.__testmenu_info_label.pack(side="left")
            self.__testmenu_buttons.pack(side="right", padx=30)
            self.__testmenu_answer_button.pack(side="right")
            self.__testmenu_answer_entry.bind("<Return>", self.__testmenu_answered)

    def __hide_testmenu(self):
        self.__last_menu = self.__menu
        self.__menu=""
        self.__testmenu.pack_forget()
        
    def __testmenu_newCard(self, event=0):
        self.__testmenu_question_label.config(text=self.__acc.random_card())
        self.__testmenu_info_label.config(text=str(self.__acc.numberOfCardsLearned())+"/"+str(self.__acc.numberOfCards()))
        self.__testmenu_answer_entry.delete(0, "end")
    
    def __testmenu_lastCard(self, event=0):
        self.__testmenu_answer_entry.delete(0, "end")
    
    def __show_testmenu_lastCard(self):
        if self.__menu=="":
            self.__last_menu=self.__menu
            self.__menu = "testmenu"
            self.__testmenu.pack(pady=(self.__root.winfo_screenheight()-410)//2)
    
    #- - - - - - - - Deckmenu - - - - - - - -
    def __load_card(self, event=0):
        """Laed das Uebergebene Deck"""
        try:
            x = self.__deckmenu_decks_list_listbox.curselection()[0]
            self.__acc.deck_card_load(self.__acc.deck_cards()[x])
            return True
        except:
            return False

    def __deckmenu_decks_list_listbox_update(self):
        liste = self.__acc.deck_cards()
        self.__deckmenu_decks_list_listbox.delete(0, "end")
        for elem in liste:
            if elem[2]=="0":
                richtung = "\u2192 "
            elif elem[2]=="1":
                richtung = "\u2190 "
            elif elem[2]=="2":
                richtung = "\u2194 "
            
            self.__deckmenu_decks_list_listbox.insert("end", \
                    self.__einruecken_hinten(elem[0], 18)+\
                    richtung+\
                    self.__einruecken_hinten(elem[1], 18)+\
                    self.__einruecken_vorne(elem[3], 4))
        if len(self.__acc.deck_cards())>self.__listbox_elems:
            self.__deckmenu_decks_scrollbar_1.pack(side="right", fill="y")
        else:
            self.__deckmenu_decks_scrollbar_1.pack_forget()

    def __deckmenu_question_hide(self, event=0):
        self.__deckmenu_question.pack_forget()
        self.__deckmenu_question_label.pack_forget()
        self.__deckmenu_question_label_frame.pack_forget()
        self.__deckmenu_question_buttons.pack_forget()
        self.__deckmenu_question_buttons_1.pack_forget()
        self.__deckmenu_question_buttons_2.pack_forget()
        self.__deckmenu_question_entry.pack_forget()
        self.__deckmenu_question_entry_1.pack_forget()
        self.__deckmenu_question_entry_2.pack_forget()
        self.__deckmenu_question_entry_3.pack_forget()
        self.__deckmenu_question_buttons_1.config(width = self.__label_width//3)
        self.__deckmenu_question_buttons_2.config(width = self.__label_width//3)

    def __deckmenu_error_no_deck_selected(self, event=0):
        self.__deckmenu_question_hide()
        self.__deckmenu_question_label.config(text="Fehler:\nKein Kartenstapel ausgew\xe4hlt.",wraplength=self.__label_width*15)
        self.__deckmenu_question_buttons_2.config(text="OK", command=self.__deckmenu_question_hide)
        self.__deckmenu_question.pack(side="bottom", pady=7)
        self.__deckmenu_question_buttons.pack(side="bottom", pady=5)
        self.__deckmenu_question_buttons_2.pack(side="left", padx=self.__label_width*2//3)
        self.__deckmenu_question_buttons_2.focus_set()
        self.__deckmenu_question_label_frame.pack(side="top", fill="y")
        self.__deckmenu_question_label.pack(side="left",pady=5)
        
    def __deckmenu_deck_reset(self, event=0):
        self.__acc.deck_statistik_reset()
        self.__deckmenu_question_hide()

    def __create_deckmenu(self):
        #Frames
        self.__deckmenu                      = tkinter.Frame(self.__root,                                            bd = 5, relief = "flat")
        self.__deckmenu_decks                = tkinter.Frame(self.__deckmenu,               bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__deckmenu_decks_list           = tkinter.Frame(self.__deckmenu_decks,         bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__deckmenu_decks_list_head      = tkinter.Frame(self.__deckmenu_decks_list,    bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__deckmenu_decks_scrollbar      = tkinter.Frame(self.__deckmenu_decks_list,    bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__deckmenu_options_question     = tkinter.Frame(self.__deckmenu_decks)
        self.__deckmenu_options              = tkinter.Frame(self.__deckmenu_decks,         bg=self.__frame_bgcolor, bd = 5, relief = "flat")
        self.__deckmenu_question             = tkinter.Frame(self.__deckmenu_decks,         bg=self.__label_bgcolor, bd = 5, relief = "flat" )
        self.__deckmenu_question_label_frame = tkinter.Frame(self.__deckmenu_question,      bg=self.__label_bgcolor)
        self.__deckmenu_question_buttons     = tkinter.Frame(self.__deckmenu_question,      bg=self.__label_bgcolor)
        self.__deckmenu_question_entry       = tkinter.Frame(self.__deckmenu_question,      bg=self.__label_bgcolor)
        
        
        #Links
        self.__deckmenu_decks_list_head_1 = tkinter.Label(self.__deckmenu_decks_list_head, text= self.__einruecken_hinten("Seite 1",20),      font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0) 
        self.__deckmenu_decks_list_head_2 = tkinter.Label(self.__deckmenu_decks_list_head, text= self.__einruecken_hinten("Seite 2",18), font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0)
        self.__deckmenu_decks_list_head_3 = tkinter.Label(self.__deckmenu_decks_list_head, text= "  % ",                                 font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, relief = "flat", takefocus=False, anchor="w", padx=0, pady=0, borderwidth=0)
        #self.__deckmenu_decks_list_head_1.bind("<Button-1>",lambda event:self.__deckmenu_decks_list_listbox_sort(1))
        #self.__deckmenu_decks_list_head_2.bind("<Button-1>",lambda event:self.__deckmenu_decks_list_listbox_sort(2))
        #self.__deckmenu_decks_list_head_3.bind("<Button-1>",lambda event:self.__deckmenu_decks_list_listbox_sort(3))
        
        self.__deckmenu_decks_list_listbox = tkinter.Listbox(self.__deckmenu_decks_list, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__frame_bgcolor, width = 46, height = self.__listbox_elems, bd=0, activestyle="dotbox")
        self.__deckmenu_decks_list_listbox.config(selectbackground=self.__label_bgcolor_onmouse,selectforeground=self.__text_fgcolor_onmouse)
        self.__deckmenu_decks_scrollbar_1 = tkinter.Scrollbar(self.__deckmenu_decks_scrollbar)
        self.__deckmenu_decks_scrollbar_1.config(command=self.__deckmenu_decks_list_listbox.yview)
        self.__deckmenu_decks_list_listbox.config(yscrollcommand=self.__deckmenu_decks_scrollbar_1.set)
        self.__deckmenu_decks_list_listbox.bind("F5", self.__deckmenu_decks_list_listbox_update)
        self.__deckmenu_decks_list_listbox.bind("<Return>", self.__lernen_begin)
        self.__deckmenu_decks_list_listbox.bind("<Double-Button>", self.__lernen_begin)
        
        #Rechts
        self.__deckmenu_options_1 = tkinter.Button(self.__deckmenu_options, text= "Lernen",        font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__deckmenu_options_2 = tkinter.Button(self.__deckmenu_options, text= "Testen",        font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__deckmenu_options_3 = tkinter.Button(self.__deckmenu_options, text= "Hinzuf\xfcgen", font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__deckmenu_options_4 = tkinter.Button(self.__deckmenu_options, text= "Bearbeiten",    font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__deckmenu_options_5 = tkinter.Button(self.__deckmenu_options, text= "L\xf6schen",    font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        
        self.__button_normal_binds(self.__deckmenu_options_1)
        self.__button_normal_binds(self.__deckmenu_options_2)
        self.__button_normal_binds(self.__deckmenu_options_3)
        self.__button_normal_binds(self.__deckmenu_options_4)
        self.__button_normal_binds(self.__deckmenu_options_5)
        
        
        self.__deckmenu_question_entry_1 = tkinter.Entry(self.__deckmenu_question_entry, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__deckmenu_question_entry_2 = tkinter.Entry(self.__deckmenu_question_entry, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__deckmenu_question_entry_3 = tkinter.Entry(self.__deckmenu_question_entry, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        self.__deckmenu_question_buttons_1 = tkinter.Button(self.__deckmenu_question_buttons, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//3)
        self.__deckmenu_question_buttons_2 = tkinter.Button(self.__deckmenu_question_buttons, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//3)
        self.__deckmenu_question_label = tkinter.Label(self.__deckmenu_question_label_frame, font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width)
        
        self.__button_normal_binds(self.__deckmenu_question_buttons_1)
        self.__button_normal_binds(self.__deckmenu_question_buttons_2)
        
        
    def __show_deckmenu(self):
        if self.__menu == "":
            self.__menu = "deckmenu"
            self.__deckmenu.pack(pady=20)
            self.__deckmenu_decks.pack(side="top")
            self.__deckmenu_decks_list.pack(side="left")
            print(len(self.__acc.deck_list()), self.__listbox_elems)
            self.__deckmenu_decks_scrollbar.pack(side="right",fill="y")
            self.__deckmenu_options.pack(side="top", pady=20)
            self.__deckmenu_decks_list_listbox_update()
            self.__deckmenu_decks_list_head.pack(side="top")
            self.__deckmenu_decks_list_head_1.pack(side="left")
            self.__deckmenu_decks_list_head_2.pack(side="left")
            self.__deckmenu_decks_list_head_3.pack(side="right")
            self.__deckmenu_decks_list_listbox.pack(side="bottom")
            self.__deckmenu_options_1.pack(side="top", pady=2, padx=10)
            self.__deckmenu_options_2.pack(side="top", pady=2, padx=10)
            self.__deckmenu_options_3.pack(side="top", pady=2, padx=10)
            self.__deckmenu_options_4.pack(side="top", pady=2, padx=10)
            self.__deckmenu_options_5.pack(side="top", pady=2, padx=10)
    
    def __hide_deckmenu(self):
        self.__menu = ""
        self.__last_menu="deckmenu"
        self.__deckmenu_options_1.pack_forget()
        self.__deckmenu_options_2.pack_forget()
        self.__deckmenu_options_3.pack_forget()
        self.__deckmenu_options_4.pack_forget()
        self.__deckmenu_options_5.pack_forget()
        self.__deckmenu_options.pack_forget()
        self.__deckmenu_decks_list_head_1.pack_forget()
        self.__deckmenu_decks_list_head_2.pack_forget()
        self.__deckmenu_decks_list_head_3.pack_forget()
        self.__deckmenu_decks_list_listbox.pack_forget()
        self.__deckmenu_decks_scrollbar_1.pack_forget()
        self.__deckmenu_decks_list_head.pack_forget()
        self.__deckmenu_decks_list.pack_forget()
        self.__deckmenu_decks_scrollbar.pack_forget()
        self.__deckmenu.pack_forget()
        self.__deckmenu_question_hide()
    
    
    
    #- - - - - - - - Exitmenu - - - - - - - -
    def __create_exitmenu(self):
        self.__exitmenu = tkinter.Frame(self.__root,bg=self.__bgcolor, relief="flat", pady=self.__root.winfo_screenheight()//2-150)
        self.__exitmenu_frame = tkinter.Frame(self.__exitmenu, bg=self.__frame_bgcolor, pady=10,padx=10)
        self.__exitmenu_frame_text = tkinter.Frame(self.__exitmenu_frame, bg=self.__frame_bgcolor)
        self.__exitmenu_frame_buttons  = tkinter.Frame(self.__exitmenu_frame, bg=self.__frame_bgcolor)
        
        
        self.__exitmenu_text_message=tkinter.Label(self.__exitmenu_frame_text, text="Wollen Sie wiklich beenden?", bg=self.__frame_bgcolor, fg=self.__text_fgcolor, font=(self.__text_font, self.__text_height))
        self.__exitmenu_button_1 = tkinter.Button(self.__exitmenu_frame_buttons, text= "Ja",        font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//2, command=self.__destroy_window)
        self.__exitmenu_button_2 = tkinter.Button(self.__exitmenu_frame_buttons, text= "Nein",      font=(self.__text_font, self.__text_height), fg=self.__text_fgcolor, bg=self.__label_bgcolor, width = self.__label_width//2, command=self.__exit_back)
        
    def __show_exitmenu(self):
        if self.__menu=="":
            self.__menu="exitmenu"
            self.__exitmenu.pack()
            self.__exitmenu_frame.pack()
            self.__exitmenu_frame_text.pack()
            self.__exitmenu_text_message.pack(padx=10, pady=10)
            self.__exitmenu_frame_buttons.pack()
            self.__exitmenu_button_1.pack(side="left", padx=10, pady=10)
            self.__exitmenu_button_2.pack(side="left", padx=10, pady=10)
        
    def __hide_exitmenu(self):
        self.__menu=""
        self.__exitmenu.pack_forget()
        self.__exitmenu_frame.pack_forget()
        self.__exitmenu_frame_text.pack_forget()
        self.__exitmenu_text_message.pack_forget()
        self.__exitmenu_frame_buttons.pack_forget()
        self.__exitmenu_button_1.pack_forget()
        self.__exitmenu_button_2.pack_forget()
    
    #- - - - - - - - Alle Menus - - - - - - - -
    def __show_last_menu(self):
        """
        Letztes Menu, ausser Exit-Menu, Options-Menu, Hilfs-Menu
        """
        if self.__last_menu == "mainmenu":
            self.__show_mainmenu()
        elif self.__last_menu == "testmenu":
            self.__show_testmenu_lastCard()
        elif self.__last_menu == "lernmenu":
            self.__show_lernmenu_lastCard()
        elif self.__last_menu == "deckmenu":
            self.__show_deckmenu()

    def __hide_menu(self):
        if self.__menu=="mainmenu":
            self.__hide_mainmenu()
        elif self.__menu=="testmenu":
            self.__hide_testmenu()
        elif self.__menu=="lernmenu":
            self.__hide_lernmenu()
        elif self.__menu == "deckmenu":
            self.__hide_deckmenu()
        elif self.__menu=="exitmenu":
            self.__hide_exitmenu()

gui = gui()