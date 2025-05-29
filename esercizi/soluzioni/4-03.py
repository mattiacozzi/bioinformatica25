#Traccia:
#Crea una lista di almeno 8 elementi e scrivi l'algoritmo che li stampa tutti con davanti un numero crescente.

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

string = "{}) {}"
 
for x in range(len(fiori)):
    print(string.format(x+1, fiori[x]))