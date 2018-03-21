# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:54:59 2018

@author: Nadja
"""

"""
Funktion Gravitation
Der Funktion werden die Werte von Weiß oder Schwarz übergeben.
A - D sind die Matrizen die im Vorraus erzeugt werden.
"""

def Gravitation(z,s): # sorgt dafür, dass die Werte durchrutschen
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
        return h, z, s # mit dem Output werden die Koordinatenlisten gefüllt

