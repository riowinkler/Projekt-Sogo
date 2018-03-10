# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:02:36 2018

@author: Moritz
"""
from pylab import *

print("Herzlich Willkommen bei Sogo.") #Spielanleitung 
print("Hier zeigt sich, ob sie es schaffen, ihren Gegner geschickt an der Nase herumzuführen, um zu gewinnen.")
print("Gewonnen ist das Spiel, wenn Sie in egal welcher Konstellation vier Kugeln einer Farbe in einer Reihe haben.")
print("Das heißt, wenn vier gleichfarbige Steine senkrecht übereinander, waagrecht nebeneinander, diagonal in einer Ebene oder aber auch diagonal nach oben oder von Ecke zu Ecke gesetzt werden.")
print("Um das Spiel zu starten, geben Sie einfach start(eine beliebige natürliche Zahl) ein.")
print("Um ihre Kugel zu setzten, müssen sie die Zeile und die Spalte angeben. Von oben nach unten gibt es vier Zeilen, die mit 1 bis 4 gewählt werden können.")
print("Von links nach rechts gibt es ebenfalls vier Spalten, die mit 1 bis 4 ausgewählt werden können.")
print("Um die Position zum Beispiel in der ersten Zeile und der dritten Spalte zu setzten, muss man eingeben: 1,3. Bitte keine Leerzeichen setzen.")
print("Dann viel Spaß beim Spielen")

#Erzeugt die Matrizen als Spielfläche(zum Auftragen der Daten)
A = np.zeros((4,4))
B = np.zeros((4,4))
C = np.zeros((4,4))
D = np.zeros((4,4))

"""
Funktion start
Startet das Spiel und beendet es mit der Siegerverkündung
In ihr sind alle FUnktionen integriert
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
    while Abbruchbedingung != "Schwarz": # Lässt die Spieler ihre Züge machen, bis einer gewonnen hat.
        weiß(eingabe = input(" Weiß ist dran. Geben sie Zeile, Spalte ein:"))
        Abbruchbedingung = Gewinner(A,B,C,D)
        if Abbruchbedingung == "Weiß": # Sorgt dafür, dass sofort abgebrochen wird, sobald Weiß 4 in einer Reihe hat.
            break
        schwarz(eingabe = input( "Schwarz ist dran. Geben sie Zeile, Spalte ein:"))
        Abbruchbedingung = Gewinner(A,B,C,D)
        #Verkündet den Gewinner
    if Abbruchbedingung == "Weiß":
        return("Weiß hat gewonnen")
    if Abbruchbedingung == "Schwarz":
        return("Schwarz hat gewonnen")

