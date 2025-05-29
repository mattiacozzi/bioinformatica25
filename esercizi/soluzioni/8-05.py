#Traccia:
#Importa il file “best-actor-age.csv” e stampalo a schermo nella sua interezza.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

print(attori.to_string())