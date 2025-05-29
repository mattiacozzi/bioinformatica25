#Traccia:
#Traduci in italiano il nome di tutti i film con cui Marlon Brando ha vinto l’Oscar.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

#estraggo i film con cui Marlon Brando ha vinto l'Oscar
filmMB = attori.loc[attori["Name"] == "Marlon Brando", "Movie"]

#scorro tutti i film e ne cambio il nome:
for film in filmMB:
    print("Inserisci il titolo italiano di", film)
    titoloIt = input()
    attori.loc[attori["Movie"] == film, "Movie"] = titoloIt

#aggiorno la variabile che contiene i film e la stampo
filmMB = attori.loc[attori["Name"] == "Marlon Brando", "Movie"]
print("Ecco i film richiesti con il nuovo titolo:")
print(filmMB)