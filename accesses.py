import os

def pruefe_dateipfade():
    """
    Diese Funktion prueft, ob alle noetigen Dateipfade existieren, wenn nicht, werden diese hier erstllt
    noetige Dateipfade:
    %APPDATA%\Rena\
    %APPDATA%\Rena\stapel
    %APPDATA%\Rena\einstellungen
    """
    pass

def decks_list():
    """
    Funkion liesst alle Kartenstapel aus %APPDATA%\[PROGRAMMNAME]\stapel
    Die Stapel sind Dateien, dessen Dateinamen so aussen: *.rna
    """
    #return liste
    pass

def deck_info(nameofdeck):
    """
    Diese Funktion gibt von einem Stapel die Infos zurueck
    return [name, letzterAufruf, AnzahlKarten, Lernstand]
    """
    #return infos
    pass

def deck_cards():
    """
    Diese Funktion gibt aus der Stapeldatei die Karten als Liste/Dictionary zurueck
    Aufbau der Datei:
    + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    | Name|letzterAufruf|AnzahlKarten|Lernstand[0-100] ::infos ueber den Stapel |
    | Vorderseite|Rueckseite|Einseiteig(0)/Zweiseitig(1)|lernstand ::Kartenifos |
    | ...                                                                       |
    + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    """
    pass



