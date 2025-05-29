#Traccia:
#Crea una lista con un numero dispari di elementi e scrivi l'algoritmo che stampa i tre valori centrali. L'algoritmo deve funzionare per tutte le liste con elementi dispari.

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
]

centro = int(len(fiori)/2)

print(fiori[centro-1])
print(fiori[centro])
print(fiori[centro+1])