#Traccia:
#Crea un modulo che contenga almeno due funzioni a tua scelta. Importa il modulo in un algoritmo e utilizza in esso le due funzioni presenti nel modulo.

import modulo2 as my2

my2.welcome()

primo = float(input("Inserisci il primo coefficiente: "))
secondo = float(input("Inserisci il secondo coefficiente: "))
terzo = float(input("Inserisci il terzo coefficiente: "))

delta = my2.calcolaDelta(primo, secondo, terzo)

my2.risolvi(primo, secondo, delta)
