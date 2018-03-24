# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:54:49 2018

@author: Nadja 
    
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Listen für den Plot für Funktion weiß
Zeileweiß = []
Spalteweiß = []
Höheweiß = []

# Listen für den Plot für Funktion schwarz
Zeileschwarz = []
Spalteschwarz = []
Höheschwarz = []

"""
Funktion Plotweiß
"""

def Plotweiß (Zeileweiß, Spalteweiß, Höheweiß): # PLottet mit den Daten aus der Liste die Positionen
    
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

def Plotschwarz (Zeileschwarz, Spalteschwarz, Höheschwarz): # PLottet mit den Daten aus der Liste die Positionen
    
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
