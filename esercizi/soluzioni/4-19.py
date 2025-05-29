#Traccia:
#Crea un insieme con quanti elementi preferisci, chiedi all'utente una stringa, controlla se è presente nell'insieme e stampa il risultato della ricerca.

fiori = {"Rosa","Girasole","Viola","Orchidea","Tulipano","Giglio","Margherita","Papavero","Garofano","Gardenia"}

elemento = input("Inserisci il nome di un fiore: ")

if elemento in fiori:
    print("Trovato.")
else:
    print("Non trovato.")