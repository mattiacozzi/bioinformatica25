#Traccia:
#Traduci il nome di almeno 3 film citati nel file “best-actor-age.csv” in italiano. Stampa a schermo i record modificati.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

#estraggo alcuni film
film1 = attori.loc[attori["Index"] == 49, "Movie"]
film2 = attori.loc[attori["Index"] == 64, "Movie"]
film3 = attori.loc[attori["Index"] == 65, "Movie"]

print("Inserisci il titolo italiano del film:", attori.iloc[48,5])
titoloIt = input()
attori.iloc[48,5] = titoloIt
print("Hai cambiato il titolo di", film1.iloc[0], "in", attori.iloc[48,5])

print("Inserisci il titolo italiano del film:", attori.iloc[63,5])
titoloIt = input()
attori.iloc[63,5] = titoloIt
print("Hai cambiato il titolo di", film1.iloc[0], "in", attori.iloc[63,5])

print("Inserisci il titolo italiano del film:", attori.iloc[64,5])
titoloIt = input()
attori.iloc[64,5] = titoloIt
print("Hai cambiato il titolo di", film1.iloc[0], "in", attori.iloc[64,5])