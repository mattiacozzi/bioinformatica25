#Traccia:
#Crea un file CSV a tua scelta, importalo in un algoritmo e stampane il contenuto. Il file CSV dovrà contenere almeno 5 record con almeno 4 attributi.
import pandas as pd

gatti = pd.read_csv("myCSV.csv")

print(gatti.to_string())