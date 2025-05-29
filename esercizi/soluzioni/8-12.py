#Traccia:
#Scopri in quali anni Tom Hanks ha vinto l’Oscar come miglior attore.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv", index_col=4)

print(attori.loc[["Tom Hanks"], "Year"])