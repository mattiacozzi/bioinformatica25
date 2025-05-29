#Traccia:
#Crea un dict per un oggetto a tua scelta. Mostra poi tutte le chiavi presenti all'utente e chiedi se vuole modificare qualche valore. Se sì, crea un algoritmo che permetta all'utente di cambiare il valore di una chiave.

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

chiavi = prodotto1.keys()

stringa = "Il prodotto ha le seguenti chiavi:\n{}"

print(stringa.format(chiavi))

choice = input("Vuoi cambiare il valore di qualche chiave? Y/N: ")

if choice == "Y":
    choice2 = input("Di quale chiave vuoi cambiare il valore? ")
    if choice2 in chiavi:
        prodotto1[choice2] = input("Inserisci il nuovo valore: ")
else:
    print("Hai scelto di non fare nulla.\n")

for x in prodotto1:
    print(x + ": " + str(prodotto1[x]))