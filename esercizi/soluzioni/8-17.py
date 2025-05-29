#Traccia:
#Calcola la media delle età delle attrici che hanno vinto l’Oscar.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

donne = attori[attori.Gender == "Female"]

#lunghezza del dataframe
totale = len(donne)

#valore iniziale della somma
somma = 0

#sommo, scorrendo le righe, i valori della quarta colonna, cioè l'età
for riga in range(totale):
    somma = somma + donne.iloc[riga,3]

#stampo la media
print("La media delle età delle donne vincitrici dell'Oscar è di", somma/totale, "anni.")