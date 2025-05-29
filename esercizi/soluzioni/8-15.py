#Traccia:
#Scopri quanti attori uomini hanno vinto un Oscar a più di 60 anni. Stampa a schermo tutti i loro nomi.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

oldMen = attori[(attori.Age > 60) & (attori.Gender == "Male")]

print(len(oldMen), "uomini hanno vinto l'Oscar a più di 60 anni:")

print(oldMen["Name"])