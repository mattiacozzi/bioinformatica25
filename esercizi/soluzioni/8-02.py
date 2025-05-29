#Traccia:
#Crea una serie in pandas che contenga i dati relativi ad un esame che hai dato (nome, voto, data). Stampa la serie a schermo.
import pandas as pd

#creazione lista di partenza
esame = {"nome": "Informatica", "voto": 27, "data": "2025-06-03"}

#creazione della serie in pandas
myExam = pd.Series(esame)

#stampa della serie
print(myExam)