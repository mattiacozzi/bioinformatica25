#Traccia:
#Crea una lista che contiene dieci elementi, anche ripetuti. Chiedi poi all'utente di inserire una stringa e controlla se tale elemento è presente nella lista. Se è presente, scrivi un algoritmo che conta quante volte quell'elemento si presenta nella lista, usando la funzione count().


fiori = ["Rosa","Girasole","Viola","Orchidea","Tulipano","Giglio","Rosa","Viola","Garofano","Rosa"]

elemento = input("Inserisci il nome di un fiore: ")

string = "Ho trovato {} nella lista. È presente {} volte."

if elemento in fiori:
    presenze = fiori.count(elemento)
    print(string.format(elemento, presenze))
else:
    print("Non trovato.")