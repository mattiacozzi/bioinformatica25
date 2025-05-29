#Traccia:
#Realizza un dizionario relativo ad un profumo o ad un prodotto cosmetico. Usa un dizionario annidato per fornire la composizione dettagliata. Mostra i dati a schermo, con una formattazione gradevole e leggibile.

prodotto1 = {
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

stringa = "{}{}: {}"
print(stringa.format("","nome",prodotto1["nome"]))
print(stringa.format("","categoria",prodotto1["categoria"]))
print("composizione: ")
for x in prodotto1["composizione"]:
    print(stringa.format("\t",x, prodotto1["composizione"][x]))
print(stringa.format("","prezzo",prodotto1["prezzo"]))