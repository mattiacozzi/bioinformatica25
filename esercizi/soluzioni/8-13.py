#Traccia:
#Scopri quante volte Sean Penn ha vinto l’Oscar e con quali film.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv", index_col=4)

pennMovies = attori.loc[["Sean Penn"], "Movie"]

print("Sean Penn ha vinto l'Oscar", len(pennMovies), "volte, con:")
for riga in pennMovies:
    print(riga)