#Traccia:
#Scrivi un algoritmo che stampi a schermo i primi 10 record del file “best-actor-age.csv”.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

print(attori.head(10))