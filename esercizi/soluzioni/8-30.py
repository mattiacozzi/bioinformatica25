#Traccia:
#Scrivi un algoritmo che chieda all’utente una data iniziale e una data finale. Salva in un file CSV i dati relativi alle vittorie agli Oscar negli anni compresi tra i due che l’utente ha inserito. Mostra a schermo il contenuto di tale file.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

inizio = int(input("Inserisci una data iniziale: "))
fine = int(input("Inserisci una data finale: "))

myDS = attori[(attori.Year >= inizio) & (attori.Year <= fine)]

print(myDS)

myDS.to_csv("best-actor-betweenYears.csv")

print("Finito.")