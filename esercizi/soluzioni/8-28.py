#Traccia:
# Salva in formato XLSX i dati relativi alle vittorie agli Oscar, per uomini e donne, precedenti alla fine della Seconda Guerra Mondiale.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

attoriRestrict = attori[attori.Year < 1945]

attoriRestrict.to_excel("best-actor-restrictedWW2.xlsx")