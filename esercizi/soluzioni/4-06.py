#Traccia:
#Crea una lista di almeno 5 elementi, stampala e poi creane una nuova con gli elementi in ordine inverso. Stampa anche quella.

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

print("Ecco la lista originaria:")
for x in fiori:
    print(x)

#creo una lista vuota
fiori2 = []

# aggiungo alla nuova lista gli elementi dell'altra partendo dal fondo
for y in range(int(len(fiori))):
    fiori2.append(fiori[-(y+1)])

print("Ecco la lista invertita:")
for x in fiori2:
    print(x)