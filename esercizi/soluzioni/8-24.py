#Traccia:
#Scopri quante volte è successo che un attore e un'attrice abbiano vinto l’Oscar con lo stesso film. Stampa a schermo poi il nome del film, il nome dell’attore e il nome dell’attrice.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

uomini = attori[attori.Gender == "Male"]

donne = attori[attori.Gender == "Female"]

#salvo i risultati in una lista di tuple
dataframe = pd.DataFrame()

for riga in range(len(uomini)):
    #se il film è lo stesso per uomini e donne
    if uomini.iloc[riga,5] == donne.iloc[riga,5]:
        nuovo = pd.DataFrame([
            {
                "Movie": uomini.iloc[riga,5],
                "Male": uomini.iloc[riga,4],
                "Female": donne.iloc[riga,4]
            },
        ])
        dataframe = pd.concat([dataframe,nuovo])

print("Un uomo e una donna hanno visto l'Oscar per lo stesso film", len(dataframe), "volte. Nel dettaglio:")
print(dataframe)
