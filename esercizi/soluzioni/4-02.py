#Traccia:
#Crea una lista di almeno 8 elementi e scrivi l'algoritmo che li stampa tutti in ordine inverso.

fiori = [
    "Rosa",
    "Girasole",
    "Viola",
    "Orchidea",
    "Tulipano",
    "Giglio",
    "Margherita",
    "Papavero",
    "Garofano",
    "Gardenia"
]

for x in range(len(fiori)):
    print(fiori[-(x+1)])