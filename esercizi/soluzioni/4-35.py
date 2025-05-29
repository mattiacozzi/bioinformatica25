#Traccia:
#Crea 3 dizionari come descritto nell'esercizio precedente. Una delle chiavi deve essere un codice (da 1 a 3). Chiedi poi all'utente di inserire un numero da 1 a 3 (altrimenti viene mostrato un errore) e in base al codice inserito, mostra le informazioni del prodotto con un output gradevole e leggibile.

prodotto1 = {
    "codice":        1,
    "categoria":     "crema idratante per il viso",
    "nome":          "SmileyFace",
    "composizione": {
            "acqua":         65,
            "umidificanti":  10,
            "emollienti":    12,
            "emulsionanti":  5,
            "conservanti":   2,
            "antiossidanti": 5,
            "profumo":       1,
    },
    "prezzo":       12.99,
}

prodotto2 = {
    "codice":        2,
    "categoria":     "crema idratante per il corpo",
    "nome":          "SmileyBody",
    "composizione": {
            "acqua":         70,
            "umidificanti":  15,
            "emollienti":    10,
            "emulsionanti":  7,
            "conservanti":   1,
            "antiossidanti": 6,
            "profumo":       1,
    },
    "prezzo":       7.25,
}

prodotto3 = {
    "codice":        3,
    "categoria":     "crema idratante per i piedi",
    "nome":          "SmileyFeet",
    "composizione": {
            "acqua":         50,
            "umidificanti":  15,
            "emollienti":    15,
            "emulsionanti":  12,
            "conservanti":   3,
            "antiossidanti": 3,
            "profumo":       2,
    },
    "prezzo":       4.99 

}

scelta = int(input("Su quale prodotto vuoi operare? (inserisci un numero da 1 a 3) "))
if scelta > 3:
    print("ERRORE: Valore non riconosciuto.")
else:
    lista = (prodotto1, prodotto2, prodotto3)
    myProd = lista[scelta-1]
    stringa = "{}{}: {}"
    print(stringa.format("","codice",myProd["codice"]))
    print(stringa.format("","nome",myProd["nome"]))
    print(stringa.format("","categoria",myProd["categoria"]))
    print("composizione: ")
    for x in myProd["composizione"]:
        print(stringa.format("\t",x, myProd["composizione"][x]))
    print(stringa.format("","prezzo",myProd["prezzo"]))