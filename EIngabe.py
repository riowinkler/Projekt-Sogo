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

