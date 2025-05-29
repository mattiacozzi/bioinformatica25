#Traccia:
#Mostra a schermo i nomi delle cinque donne più giovani ad aver vinto l’Oscar.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

donne = attori[attori.Gender == "Female"]

attoriSorted = donne.sort_values(by="Age").head(5)

print(attoriSorted)