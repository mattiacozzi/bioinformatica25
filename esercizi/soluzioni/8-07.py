#Traccia:
#Riscrivi in formato JSON i dati del file CSV dell’esercizio precedente. Importa il file JSON creato in Python e stampane a schermo il contenuto.
import pandas as pd

gatti = pd.read_json("myJSON.json")

print(gatti.to_string())