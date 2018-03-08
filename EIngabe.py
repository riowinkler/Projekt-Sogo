# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:59:01 2018
@author: Moritz
"""

"""
Funktion Gravitation
Der Funktion werden die Werte von weiß oder schwarz übergeben.
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

