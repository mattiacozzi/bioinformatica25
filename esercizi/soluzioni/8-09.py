#Traccia:
#Importa in Python tutti i fogli del file “db-profumi.xlsx” e stampane a schermo il contenuto.
import pandas as pd

naso = pd.read_excel("db-profumi.xlsx", "naso")
profumo = pd.read_excel("db-profumi.xlsx", "profumo")
brand = pd.read_excel("db-profumi.xlsx", "brand")

print(naso.to_string())
print(profumo.to_string())
print(brand.to_string())