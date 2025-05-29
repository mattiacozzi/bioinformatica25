#Traccia:
#Crea un dict per un oggetto a tua scelta. Mostra poi tutte le chiavi presenti all'utente e chiedi se vuole Operare sui dati. Se sì, chiedi quale operazione vuole compiere: aggiunta, eliminazione o modifica di dati. Crea un algoritmo che permetta all'utente di eseguire l'operazione selezionata. Una volta eseguita, deve essere mostrato il dict modificato.

prodotto1 = {
    "categoria":     "crema idratante per il viso",
    "nome":          "SmileyFace",
    "acqua":         65,
    "umidificanti":  10,
    "emollienti":    12,
    "emulsionanti":  5,
    "conservanti":   2,
    "antiossidanti": 5,
    "profumo":       1,
}

print("Ecco le informazioni sul prodotto: ")
for x in prodotto1:
    print(x + ": " + str(prodotto1[x]))

choice = input("Che operazione vuoi fare?\nA = aggiungi dati\tD = elimina dati\tM = modifica dati\n")

if choice == "M":
    chiave = input("Di quale chiave vuoi cambiare il valore? ")
    if chiave in prodotto1:
        prodotto1[chiave] = input("Inserisci il nuovo valore: ")
    else:
        print("ERRORE: Chiave inserita non valida. ")

elif choice == "D":
    chiave = input("Quale chiave vuoi eliminare? ")
    if chiave in prodotto1:
        prodotto1.pop(chiave)
    else:
        print("ERRORE: Chiave inserita non valida. ")
   
elif choice == "A":
    chiave = input("Inserisci la nuova chiave: ")
    prodotto1[chiave] = input("Inserisci il nuovo valore: ")

else:
    print("ERRORE: Operazione non riconosciuta.\n")

for x in prodotto1:
    print(x + ": " + str(prodotto1[x]))