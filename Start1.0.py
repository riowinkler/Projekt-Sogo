# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:56:37 2018

@author: Nadja
"""

"""
Funktion start
Startet das Spiel und beendet es mit der Siegerverkündung
In ihr sind alle Funktionen integriert
"""

def start(Zahl): 
# Hier muss der Grundplot rein
    
    if Zahl == 1:
        print("1 ist die einsamste Zahl, aber ihr scheint zu zweit zu sein.")
    if Zahl == 666:
        print("Hoffentlich ist der Teufel nicht dein Gegner.")
    if Zahl == 42:
        print("Es ist wahrscheinlich nicht der Sinn des Lebens dieses Spiel zu spielen, aber trotzdem viel Spaß.")
    if Zahl == 0:
        print("Wer Nichts wagt, der gewinnt auch Nichts.")
    
    Abbruchbedingung = "Niemand"
    while Abbruchbedingung != "Schwarz":
        eingabe = input (" Weiß ist dran. Geben sie Zeile, Spalte ein:")
        if eingabe == "exit": # sofortiger Ausstieg
            return "ende"
        weiß(eingabe)
        Plotweiß(Zeileweiß, Spalteweiß, Höheweiß) # Plot
        Abbruchbedingung = Gewinner(A,B,C,D)
        if Abbruchbedingung == "Weiß":
            break
        eingabe = input( "Schwarz ist dran. Geben sie Zeile, Spalte ein:")
        if eingabe == "exit": # sofortiger Ausstieg
            return "ende"
        schwarz(eingabe)
        Plotschwarz(Zeileschwarz, Spalteschwarz, Höheschwarz) # Plot
        Abbruchbedingung = Gewinner(A,B,C,D)
        # verkündet den Gewinner
    if Abbruchbedingung == "Weiß":
        return("Weiß hat gewonnen")
    if Abbruchbedingung == "Schwarz":
        return("Schwarz hat gewonnen") 
