#Traccia:
#Crea una serie in pandas che contenga l’elenco dei tuoi voti e stampala a schermo.
import pandas as pd

#creazione lista di partenza
voti = [23, 30, 19, 27, 29, 22]

#creazione della serie in pandas
myGrades = pd.Series(voti)

#stampa della serie
print(myGrades)