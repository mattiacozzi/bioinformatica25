#Traccia:
#Crea una lista di almeno 8 elementi e scrivi l'algoritmo che stampa solo il secondo, il quarto, il sesto, ecc.

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
 
for x in range(int(len(fiori)/2)):
    print(string.format(2*(x+1), fiori[2*x+1]))