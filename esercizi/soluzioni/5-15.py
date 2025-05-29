#Traccia:
#Richiedi all'utente due angoli in gradi e convertili in radianti.

import math

def converti(a):
    risultato = a * math.pi / 180
    string = "L'angolo {} in radianti vale {}."
    print(string.format(a, risultato))

primo = float(input("Inserisci un angolo in gradi da convertire in radianti: "))
converti(primo)

secondo = float(input("Inserisci un altro angolo in gradi da convertire in radianti: "))
converti(secondo)