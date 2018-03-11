# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:08:17 2018

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
Funktion Gravitation
Der Funktion werden die Werte von Weiß oder Schwarz übergeben.
A - D sind die Matrizen die im Vorraus erzeugt werden.
"""

def Gravitation(z,s): # sorgt dafür das die Werte durchrutschen
    if B[z,s] == 0:
        B[z,s] = A[z,s]
        A[z,s] = 0
        if C[z,s] == 0:
            C[z,s] = B[z,s]
            B[z,s] = 0
            if D[z,s] == 0:
                D[z,s] = C[z,s]
                C[z,s] = 0
                return D, z, s # Bin mit dem Output nicht zu frieden, hätte gern den  Namen der Matrix als Output
            else:
                return C, z, s
        else:
            return B, z, s
    else:
        return A, z, s 
# Der Output soll genutzt werden, um später die Kugel an die richtige Stelle zu plotten.

"""
Funktion weiß
"""

# eingabe = input(" Weiß ist dran. Geben sie Zeile, Spalte ein:") # Erzeugt inputline

def weiß(eingabe): # wandelt die Eingabe in eine Position in den Matrizen um
    L = list(eingabe)
    L[0] = int(L[0])
    L[2] = int(L[2])
    s = L[0] - 1 #sorgt dafür, dass man von 1-4 angeben kann anstatt von 0-3
    z = L[2] -1
    A[s,z] = 1
    Gravitation(s,z)
    
    return (print(A),
        print("__________________________________"),
        print(B),
        print("__________________________________"),
        print(C),
        print("__________________________________"),
        print(D)) #wird noch geändert, ist erstmal zur Kontrolle



"""
Funktion schwarz
"""

# eingabe = input( "Schwarz ist dran. Geben sie Zeile, Spalte ein:")

def schwarz(eingabe):
    L = list(eingabe)
    L[0] = int(L[0])
    L[2] = int(L[2])
    s = L[0] - 1
    z = L[2] - 1
    A[s,z] = 2
    Gravitation(s,z)
    
    return (print(A),
            print("__________________________________"),
            print(B),
            print("__________________________________"),
            print(C),
            print("__________________________________"),
            print(D)) #wird noch geändert, ist erstmal zur Kontrolle

    
"""
Funktion Gewinner
Testet anhand der gesetzten Einsen und Zweien, ob jemand gewonnen hat.
"""

def Gewinner(A,B,C,D):
    #Enthält alle Gewinnmöglichkeiten
    Gewinnerliste = [[A[0,0],A[0,1],A[0,2],A[0,3]],
 [A[1,0],A[1,1],A[1,2],A[1,3]],
 [A[2,0],A[2,1],A[2,2],A[2,3]],
 [A[3,0],A[3,1],A[3,2],A[3,3]],
 [B[0,0],B[0,1],B[0,2],B[0,3]],
 [B[1,0],B[1,1],B[1,2],B[1,3]],
 [B[2,0],B[2,1],B[2,2],B[2,3]],
 [B[3,0],B[3,1],B[3,2],B[3,3]],
 [C[0,0],C[0,1],C[0,2],C[0,3]],
 [C[1,0],C[1,1],C[1,2],C[1,3]],
 [C[2,0],C[2,1],C[2,2],C[2,3]],
 [C[3,0],C[3,1],C[3,2],C[3,3]],
 [D[0,0],D[0,1],D[0,2],D[0,3]],
 [D[1,0],D[1,1],D[1,2],D[1,3]],
 [D[2,0],D[2,1],D[2,2],D[2,3]],
 [D[3,0],D[3,1],D[3,2],D[3,3]],


 [A[0,0],A[1,0],A[2,0],A[3,0]],
 [A[0,1],A[1,1],A[2,1],A[3,1]],
 [A[0,2],A[1,2],A[2,2],A[3,2]],
 [A[0,3],A[1,3],A[2,3],A[3,3]],
 [B[0,0],B[1,0],B[2,0],B[3,0]],
 [B[0,1],B[1,1],B[2,1],B[3,1]],
 [B[0,2],B[1,2],B[2,2],B[3,2]],
 [B[0,3],B[1,3],B[2,3],B[3,3]],
 [C[0,0],C[1,0],C[2,0],C[3,0]],
 [C[0,1],C[1,1],C[2,1],C[3,1]],
 [C[0,2],C[1,2],C[2,2],C[3,2]],
 [C[0,3],C[1,3],C[2,3],C[3,3]],
 [D[0,0],D[1,0],D[2,0],D[3,0]],
 [D[0,1],D[1,1],D[2,1],D[3,1]],
 [D[0,2],D[1,2],D[2,2],D[3,2]],
 [D[0,3],D[1,3],D[2,3],D[3,3]],

 [A[0,0],B[0,0],C[0,0],D[0,0]],
 [A[1,0],B[1,0],C[1,0],D[1,0]],
 [A[2,0],B[2,0],C[2,0],D[2,0]],
 [A[3,0],B[3,0],C[3,0],D[3,0]],
 [A[0,1],B[0,1],C[0,1],D[0,1]],
 [A[1,1],B[1,1],C[1,1],D[1,1]],
 [A[2,1],B[2,1],C[2,1],D[2,1]],
 [A[3,1],B[3,1],C[3,1],D[3,1]],
 [A[0,2],B[0,2],C[0,2],D[0,2]],
 [A[1,2],B[1,2],C[1,2],D[1,2]],
 [A[2,2],B[2,2],C[2,2],D[2,2]],
 [A[3,2],B[3,2],C[3,2],D[3,2]],
 [A[0,3],B[0,3],C[0,3],D[0,3]],
 [A[1,3],B[1,3],C[1,3],D[1,3]],
 [A[2,3],B[2,3],C[2,3],D[2,3]],
 [A[3,3],B[3,3],C[3,3],D[3,3]],

 [A[0,0],A[1,1],A[2,2],A[3,3]],
 [B[0,0],B[1,1],B[2,2],B[3,3]],
 [C[0,0],C[1,1],C[2,2],C[3,3]],
 [D[0,0],D[1,1],D[2,2],D[3,3]],


 [A[0,3],A[1,2],A[2,1],A[3,0]],
 [B[0,3],B[1,2],B[2,1],B[3,0]],
 [C[0,3],C[1,2],C[2,1],C[3,0]],
 [D[0,3],D[1,2],D[2,1],D[3,0]],


 [A[0,0],B[1,0],C[2,0],D[3,0]],
 [A[0,1],B[1,1],C[2,1],D[3,1]],
 [A[0,2],B[1,2],C[2,2],D[3,2]],
 [A[0,3],B[1,3],C[2,3],D[3,3]],


 [D[0,0],C[1,0],B[2,0],A[3,0]],
 [D[0,1],C[1,1],B[2,1],A[3,1]],
 [D[0,2],C[1,2],B[2,2],A[3,2]],
 [D[0,3],C[1,3],B[2,3],A[3,3]],


 [D[0,0],C[0,1],B[0,2],A[0,3]],
 [D[1,0],C[1,1],B[1,2],A[1,3]],
 [D[2,0],C[2,1],B[2,2],A[2,3]],
 [D[3,0],C[3,1],B[3,2],A[3,3]],

 [A[0,0],B[0,1],C[0,2],D[0,3]],
 [A[1,0],B[1,1],C[1,2],D[1,3]],
 [A[2,0],B[2,1],C[2,2],D[2,3]],
 [A[3,0],B[3,1],C[3,2],D[3,3]],

 [A[0,3],B[1,2],C[2,1],D[3,0]],
 [D[0,0],C[1,1],B[2,2],A[3,3]],
 [A[0,0],B[1,1],C[2,2],D[3,3]],
[D[0,3],C[1,2],B[2,1],A[3,0]] ]
    
    #Testet, ob jemand gewonnen hat und gibt den Sieger zurück
    for i in range(0,76):
        if Gewinnerliste[i] == [1.0, 1.0, 1.0, 1.0]: # Das ist die Gewinnbedingung für Weiß
            return ("Weiß")
        if Gewinnerliste [i] == [2.0, 2.0, 2.0, 2.0]: # Das ist die Gewinnbedingung für Schwarz
            return ("Schwarz")
        
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
        
