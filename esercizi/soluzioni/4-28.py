#Traccia:
#Crea un dizionario che descriva la composizione di un profumo o di un prodotto cosmetico. Stampa poi a schermo la lista chiavi:valori.

prodotto = {
    "categoria":       "Crema idratante per il viso",
    "nome":            "SmileyFace",
    "% acqua":         65,
    "% umidificanti":  10,
    "% emollienti":    12,
    "% emulsionanti":  5,
    "% conservanti":   2,
    "% antiossidanti": 5,
    "% profumo":       1,
}

for x in prodotto:
    print(x + ": " + str(prodotto[x]))