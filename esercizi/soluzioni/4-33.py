#Traccia:
#Comportati come nell'esercizio precedente, ma crea tre dict invece di uno e, all'inizio dell'algoritmo, chiedi all'utente su qualche dei tre vuole operare.

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

prodotto2 = {
    "categoria":     "crema idratante per il corpo",
    "nome":          "SmileyBody",
    "acqua":         70,
    "umidificanti":  15,
    "emollienti":    10,
    "emulsionanti":  7,
    "conservanti":   1,
    "antiossidanti": 6,
    "profumo":       1,
}

prodotto3 = {
    "categoria":     "crema idratante per i piedi",
    "nome":          "SmileyFeet",
    "acqua":         50,
    "umidificanti":  15,
    "emollienti":    15,
    "emulsionanti":  12,
    "conservanti":   3,
    "antiossidanti": 3,
    "profumo":       2,
}

lista = (prodotto1, prodotto2, prodotto3)

scelta = int(input("Su quale prodotto vuoi operare? (inserisci un numero da 1 a 3)\n")) - 1

myProd = lista[scelta]

#il resto è come l'esercizio precedente, con la sola differenza che operiamo su "myProd" e non su prodotto1
print("Ecco le informazioni sul prodotto: ")
for x in myProd:
    print(x + ": " + str(myProd[x]))

choice = input("Che operazione vuoi fare?\nA = aggiungi dati\tD = elimina dati\tM = modifica dati\n")

if choice == "M":
    chiave = input("Di quale chiave vuoi cambiare il valore? ")
    if chiave in myProd:
        myProd[chiave] = input("Inserisci il nuovo valore: ")
    else:
        print("ERRORE: Chiave inserita non valida. ")

elif choice == "D":
    chiave = input("Quale chiave vuoi eliminare? ")
    if chiave in myProd:
        myProd.pop(chiave)
    else:
        print("ERRORE: Chiave inserita non valida. ")
   
elif choice == "A":
    chiave = input("Inserisci la nuova chiave: ")
    myProd[chiave] = input("Inserisci il nuovo valore: ")

else:
    print("ERRORE: Operazione non riconosciuta.\n")

for x in myProd:
    print(x + ": " + str(myProd[x]))