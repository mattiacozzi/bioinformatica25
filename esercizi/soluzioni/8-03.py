#Traccia:
#Crea una serie identica a quella dell’esercizio precedente, ma stampa a schermo solo il nome dell’esame e il voto.
import pandas as pd

#creazione lista di partenza
esame = {"nome": "Informatica", "voto": 27, "data": "2025-06-03"}

#creazione della serie in pandas
myExam = pd.Series(esame)

#stampa di alcuni elementi
print(myExam["nome"])
print(myExam["voto"])