# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:04:06 2018

@author: Moritz
"""

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