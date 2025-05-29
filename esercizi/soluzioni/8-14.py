#Traccia:
#Calcola la media delle età delle persone che hanno vinto l’Oscar. Non distinguere tra uomini e donne.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

#lunghezza del dataframe
totale = len(attori)

#valore iniziale della somma
somma = 0

#sommo, scorrendo le righe, i valori della quarta colonna, cioè l'età
for riga in range(totale):
    somma = somma + attori.iloc[riga,3]

#stampo la media
print("La media delle età vale", somma/totale)