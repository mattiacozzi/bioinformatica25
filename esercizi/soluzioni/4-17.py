#Traccia:
#Crea una tupla a tuo piacimento e chiedi una stringa all'utente. Controlla se la stringa è presente nella tupla e mostra il risultato della ricerca a schermo.

fiori = {"Rosa","Girasole","Viola","Orchidea","Tulipano","Giglio","Margherita","Papavero","Garofano","Gardenia"}

elemento = input("Inserisci il nome di un fiore: ")

if elemento in fiori:
    print("Trovato.")
else:
    print("Non trovato.")