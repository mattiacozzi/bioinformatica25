#Traccia:
#Crea un dataframe in pandas che contenga i dati (nome, voto, data) relativi a tutti gli esami che hai dato. Stampa il dataframe a schermo.
import pandas as pd

#creazione dataset di partenza
esami = {
    "nome": ["Informatica", "Bioinformatica", "Chimica organica", "Matematica", "Chimica inorganica", "Fisica"], 
    "voto": [23, 30, 19, 27, 29, 22], 
    "data": ["2025-06-03", "2025-05-20", "2025-02-01", "2025-06-10", "2025-02-18", "2025-05-30"]}

#creazione del dataframe in pandas
myExams = pd.DataFrame(esami)

#stampa del dataset
print(myExams)