#Traccia:
#Crea una lista che contiene dieci elementi. Chiedi poi all'utente di inserire una stringa e controlla se tale elemento è presente nella lista. Mostra poi a schermo una riga che dice se l'elemento è presente o meno.

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

elemento = input("Inserisci il nome di un fiore: ")

if elemento in fiori:
    print("Trovato.")
else:
    print("Non trovato.")