#Traccia:
#Mostra a schermo i nomi dei cinque uomini più vecchi ad aver vinto l’Oscar.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

uomini = attori[attori.Gender == "Male"]

attoriSorted = uomini.sort_values(by="Age", ascending=False).head(5)

print(attoriSorted)