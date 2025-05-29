#Traccia:
#Scrivi un algoritmo che stampi a schermo le colonne “Name” e “Year” degli ultimi 20 record del file “best-actor-age.csv”.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

print(attori[["Name", "Year"]].tail(20))