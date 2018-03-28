from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

print("Herzlich Willkommen bei Sogo.") #Spielanleitung 
print("Hier zeigt sich, ob sie es schaffen, ihren Gegner geschickt an der Nase herumzuführen, um zu gewinnen.")
print("Gewonnen ist das Spiel, wenn Sie in egal welcher Konstellation vier Kugeln einer Farbe in einer Reihe haben.")
print("Das heißt, wenn vier gleichfarbige Steine senkrecht übereinander, waagrecht nebeneinander, diagonal in einer Ebene oder aber auch diagonal nach oben oder von Ecke zu Ecke gesetzt werden.")
print("Um das Spiel zu starten, geben Sie einfach start(eine beliebige natürliche Zahl) ein.")
print("Um ihre Kugel zu setzten, müssen sie die Zeile und die Spalte angeben. es gibt jeweils 4 Zeilen und Spalten, die mit den Zahlen 0 bis 3 ausgewählt werden können.")
print("Um die Position zum Beispiel in der ersten Zeile und der dritten Spalte zu setzten, muss man eingeben: 0,2. Bitte keine Leerzeichen setzen.")
print("Möchten sie das Spiel vorzeitig beenden, dann geben sie einfach exit ein.")
print("Dann viel Spaß beim Spielen.")

def Gravitation(A, B, C, D, z,s): # sorgt dafür, dass die Werte durchrutschen
    if B[z,s] == 0:
        B[z,s] = A[z,s]
        A[z,s] = 0
        h = 2
        if C[z,s] == 0:
            C[z,s] = B[z,s]
            B[z,s] = 0
            h = 1
            if D[z,s] == 0:
                D[z,s] = C[z,s]
                C[z,s] = 0
                h = 0
                return h, z, s # h ist die Höhe, z ist die Zeile und s ist die Spalte
            else:
                return h, z, s
        else:
            return h, z, s
    else:
        h = 3
        return h, z, s # mit dem Output werden die Listen gefüllt
    
"""
Funktion weiß
"""

def weiß(A, B, C, D, Zeileweiß, Spalteweiß, Höheweiß, eingabe): # wandelt die Eingabe in eine Position in den Matrizen um
    L = list(eingabe)
    L[0] = int(L[0])
    L[2] = int(L[2])
    s = L[0] 
    z = L[2] 
    A[s,z] = 1
    Gravitation(A, B, C, D, s,z)
    Zeileweiß.append(z) # fügt die Zahl in eine Liste zu, aus der dann geplottet wird, für die x un y Achse
    Spalteweiß.append(s)
    # sorgt dafür, dass die Höhe angegeben wird
    if Gravitation(A, B, C, D, s,z) == (1, s, z):
        Höheweiß.append(0)
    if Gravitation(A, B, C, D, s,z) == (2, s, z):
        Höheweiß.append(1)
    if A[s,z] == 1:
        Höheweiß.append(3)
    if A[s,z] != 1:
        if Gravitation(A, B, C, D,s,z) == (3, s, z):
            Höheweiß.append(2)
    return 

"""
Funktion schwarz
"""

def schwarz(A, B, C, D, Zeileschwarz, Spalteschwarz, Höheschwarz, eingabe): # wandelt die Eingabe in eine Position in den Matrizen um
    L = list(eingabe)
    L[0] = int(L[0])
    L[2] = int(L[2])
    s = L[0] 
    z = L[2] 
    A[s,z] = 2
    Gravitation(A, B, C, D, s,z)
    Zeileschwarz.append(z) # fügt die Zahl in eine Liste zu, aus der dann geplottet wird, für die x un y Achse
    Spalteschwarz.append(s)
    # sorgt dafür, dass die Höhe angegeben wird
    if Gravitation(A, B, C, D, s,z) == (1, s, z):
        Höheschwarz.append(0)
    if Gravitation(A, B, C, D, s,z) == (2, s, z):
        Höheschwarz.append(1)
    if A[s,z] == 2:
        Höheschwarz.append(3)
    if A[s,z] != 2:
        if Gravitation(A, B, C, D, s,z) == (3, s, z):
            Höheschwarz.append(2)
    return 

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
Funktion Plotweiß
"""

def Plotweiß (Zeileweiß, Spalteweiß, Höheweiß, Zeileschwarz, Spalteschwarz, Höheschwarz): # PLottet mit den Daten aus der Liste die Positionen
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d') # erstellt das Plotfenster
    
    ax.scatter(Zeileweiß, Spalteweiß, Höheweiß, c = 'r', marker = 'o') # plottet die weißen Positionen als rote Kugeln
    ax.scatter(Zeileschwarz, Spalteschwarz, Höheschwarz, c = 'b', marker = 'o') # plottet die schwarzen Positionen als blaue Kugeln


    ax.set_xlim(0,3) # Legt den Bereich der x-Achse fest.
    ax.set_ylim(0,3) # Legt den Bereich der y-Achse fest.
    ax.set_zlim(0,3) # Legt den Bereich der z-Achse fest.

    ax.set_xlabel('Spalten')
    ax.set_ylabel("Zeilen")
    ax.set_zlabel('Höhe')
    plt.show()
    return 


"""
Funktion Plotschwarz
"""

def Plotschwarz (Zeileweiß, Spalteweiß, Höheweiß, Zeileschwarz, Spalteschwarz, Höheschwarz): # PLottet mit den Daten aus der Liste die Positionen
      
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d') # erstellt das Plotfenster
    
    ax.scatter(Zeileweiß, Spalteweiß, Höheweiß, c = 'r', marker = 'o') # plottet die weißen Positionen als rote Kugeln
    ax.scatter(Zeileschwarz, Spalteschwarz, Höheschwarz, c = 'b', marker = 'o') # plottet die schwarzen Positionen als blaue Kugeln


    ax.set_xlim(0,3) # Legt den Bereich der x-Achse fest.
    ax.set_ylim(0,3) # Legt den Bereich der y-Achse fest.
    ax.set_zlim(0,3) # Legt den Bereich der z-Achse fest.

    ax.set_xlabel('Spalten')
    ax.set_ylabel("Zeilen")
    ax.set_zlabel('Höhe')
    
    plt.show()
    return

def start(Zahl):
    print("Falls sie in einer IPython Konsole spielen, schließen sie das Plotfenster, um ihren Zug zu machen.")
    
    #Der Grundplot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d') # erstellt das Plotfenster
    ax.set_xlim(0,3) # Legt den Bereich der x-Achse fest.
    ax.set_ylim(0,3) # Legt den Bereich der y-Achse fest.
    ax.set_zlim(0,3) # Legt den Bereich der z-Achse fest.

    ax.set_xlabel('Spalten')
    ax.set_ylabel("Zeilen")
    ax.set_zlabel('Höhe')
    plt.show()
    
    #Erzeugt die Matrizen als Spielfläche(zum Auftragen der Daten)
    A = np.zeros((4,4))
    B = np.zeros((4,4))
    C = np.zeros((4,4))
    D = np.zeros((4,4))

    # Listen für den Plot für Funktion weiß
    Zeileweiß = []
    Spalteweiß = []
    Höheweiß = []

    # Listen für den Plot für Funktion schwarz
    Zeileschwarz = []
    Spalteschwarz = []
    Höheschwarz = []
    
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
        eingabe = input (" Rot ist dran. Geben sie Zeile, Spalte ein:")
        if eingabe == "exit": # sofortiger Ausstieg
            return "Das Spiel wurde vorzeitig beendet."
        weiß(A, B, C, D, Zeileweiß, Spalteweiß, Höheweiß, eingabe)
        #print(Zeileweiß, Spalteweiß, Höheweiß, Zeileschwarz, Spalteschwarz, Höheschwarz)
        Plotweiß(Zeileweiß, Spalteweiß, Höheweiß, Zeileschwarz, Spalteschwarz, Höheschwarz) # Plot
        Abbruchbedingung = Gewinner(A,B,C,D)
        if Abbruchbedingung == "Weiß":
            break
        eingabe = input( "Blau ist dran. Geben sie Zeile, Spalte ein:")
        if eingabe == "exit": # sofortiger Ausstieg
            return "Das Spiel wurde vorzeitig beendet."
        schwarz(A, B, C, D, Zeileschwarz, Spalteschwarz, Höheschwarz, eingabe)
        #print(Zeileschwarz, Spalteschwarz, Höheschwarz)
        Plotschwarz(Zeileweiß, Spalteweiß, Höheweiß, Zeileschwarz, Spalteschwarz, Höheschwarz) # Plot
        Abbruchbedingung = Gewinner(A,B,C,D)
        # verkündet den Gewinner
    if Abbruchbedingung == "Weiß":
        return("Rot hat gewonnen")
    if Abbruchbedingung == "Schwarz":
        return("Blau hat gewonnen")