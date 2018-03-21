# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:53:59 2018

@author: Nadja
"""

"""
Funktion weiß
"""

def weiß(eingabe): # wandelt die Eingabe in eine Position in den Matrizen um
    L = list(eingabe)
    L[0] = int(L[0])
    L[2] = int(L[2])
    s = L[0] 
    z = L[2] 
    A[s,z] = 1
    Gravitation(s,z)
    Zeileweiß.append(z) # fügt die Zahl einer Liste hinzu, aus der dann geplottet wird, für die x und y Achse
    Spalteweiß.append(s)
    # sorgt dafür, dass die Höhe angegeben wird
    if Gravitation(s,z) == (1, s, z):
        Höheweiß.append(0)
    if Gravitation(s,z) == (2, s, z):
        Höheweiß.append(1)
    if A[s,z] == 1:
        Höheweiß.append(3)
    if A[s,z] != 1:
        if Gravitation(s,z) == (3, s, z):
            Höheweiß.append(2)
    return 

"""
Funktion schwarz
"""

def schwarz(eingabe): # wandelt die Eingabe in eine Position in den Matrizen um
    L = list(eingabe)
    L[0] = int(L[0])
    L[2] = int(L[2])
    s = L[0] 
    z = L[2] 
    A[s,z] = 2
    Gravitation(s,z)
    Zeileschwarz.append(z) # fügt die Zahl einer Liste hinzu, aus der dann geplottet wird, für die x und y Achse
    Spalteschwarz.append(s)
    # sorgt dafür, dass die Höhe angegeben wird
    if Gravitation(s,z) == (1, s, z):
        Höheschwarz.append(0)
    if Gravitation(s,z) == (2, s, z):
        Höheschwarz.append(1)
    if A[s,z] == 2:
        Höheschwarz.append(3)
    if A[s,z] != 2:
        if Gravitation(s,z) == (3, s, z):
            Höheschwarz.append(2)
    return 