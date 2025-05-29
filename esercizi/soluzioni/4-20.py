#Traccia:
#Crea un insieme con quanti elementi preferisci e mostralo all'utente. Chiedi poi "Che cosa vuoi fare?". 
# - Se l'utente digita "A",allora dovrà poter aggiungere un elemento, avendo controllato che esso esista (può essere utile try/except).
# - Se l'utente digita "D",allora dovrà poter eliminare un elemento, avendo controllato che esso esista.
# - Se l'utente digita "S",dovrà essere mostrato l'insieme. 
# - Se l'utente digita "X",l'algoritmo deve salutare e terminare.
# - Se l'utente digita altro, dovrà essere mostrato un messaggio di errore e si dovrà chiedere una nuova immissione.

fiori = {"Rosa","Girasole","Viola","Orchidea"}

print("Ecco un insieme di fiori:")

for x in fiori:
    print(x)

risp = ""

while risp != "X":
    risp = input("\nCosa vuoi fare?\nA = aggiungi elemento\tD = elimina elemento\nS = mostra l'insieme\tX = esci\n")

    if risp == "A":
        elemento = input("\nQuale elemento vuoi aggiungere? ")
        if elemento in fiori:
            print("\nL'elemento esiste già!")
        else:
            fiori.add(elemento)
            print("Fatto!")

    elif risp == "D":
        elemento = input("\nQuale elemento vuoi eliminare? ")
        if elemento in fiori:
            fiori.remove(elemento)
            print("Fatto!")
        else:
            print("\nL'elemento non è presente nell'insieme. Riprova.")

    elif risp == "S":
        print("\nEcco l'insieme con i suoi elementi attuali: ")
        for x in fiori:
            print(x)

    elif risp == "X":
        print("\nAlla prossima!")

    else:
        print("\nComando non riconosciuto. Riprova.")