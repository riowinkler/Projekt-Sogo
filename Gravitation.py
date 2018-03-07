# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:59:01 2018

@author: Moritz
"""

"""

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