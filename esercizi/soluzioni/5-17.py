#Traccia:
#Scrivere un programma che chieda all'utente un numero intero e che costruisca il triangolo di Pascal fino al livello corrispondente al numero inserito.

#                1     n=0
#             1     1     n=1
#          1     2     1     n=2
#       1     3     3     1     n=3
#    1     4     6     4     1     n=4
# 1     5     10    10    5     1     n=5

import math

livelli = int(input("Quante righe deve avere il triangolo di Pascal? "))

#scorro i numeri da 0 al valore inserito (aggiungo 1 perché l'ultimo valore non rientra nel range)
for i in range(livelli+1):
    #svuoto la stringa
    string = "" 
    #la riga n contiene n+1 valori, quindi:
    for j in range(i+1):
        x = math.comb(i,j) #calcolo le combinazioni semplici per ottenere i valori del triangolo
        #aggiungo il nuovo valore alla stringa
        string = string + str(x) + " "
    print(string)