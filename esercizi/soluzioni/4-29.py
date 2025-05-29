#Traccia:
#Realizza un dizionario che esprima le caratteristiche, ingredienti compresi, di un profumo o di un prodotto cosmetico. Mostra poi i dati del prodotto formattando l'output in modo chiaro e gradevole.

prodotto = {
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

stringa = "Ecco le informazioni per {}, una {}:"

print(stringa.format(prodotto["nome"], prodotto["categoria"]))

linea = "{}% = {}"

x = list(prodotto.keys())
y = list(prodotto.values())

for z in range(2, len(x)):
    print(str(y[z]) + "%\t" + x[z])
