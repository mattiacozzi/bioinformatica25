#Traccia:
#Calcola la media delle età degli attori che hanno vinto l’Oscar.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

uomini = attori[attori.Gender == "Male"]

#lunghezza del dataframe
totale = len(uomini)

#valore iniziale della somma
somma = 0

#sommo, scorrendo le righe, i valori della quarta colonna, cioè l'età
for riga in range(totale):
    somma = somma + uomini.iloc[riga,3]

#stampo la media
print("La media delle età degli uomini vincitori dell'Oscar è di", somma/totale, "anni.")