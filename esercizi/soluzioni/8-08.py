#Traccia:
#Importa in Python il foglio “naso” del file “db-profumi.xlsx” e stampane a schermo il contenuto.
import pandas as pd

naso = pd.read_excel("db-profumi.xlsx", "naso")

print(naso.to_string())
