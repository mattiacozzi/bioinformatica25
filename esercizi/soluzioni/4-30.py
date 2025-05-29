#Traccia:
#Crea due dizionari per due prodotti, in modo simile all'esercizio precedente. Scegli poi due chiavi numeriche (come il peso, una percentuale, il prezzo o un codice) e scrivi un algoritmo che controlli, per i due prodotti creati, quale dei due ha il valore maggiore per la chiave prescelta. Dovrà mostrare "Il valore [NomeChiave] è più alto per [prodotto1/prodotto2]"

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

chiave = "acqua"

if prodotto1[chiave] < prodotto2[chiave]:
    print("La percentuale di acqua è maggiore nel prodotto2.")
elif prodotto1[chiave] == prodotto2[chiave]:
    print("La percentuale di acqua è uguale nei due prodotti.")
else:
    print("La percentuale di acqua è maggiore nel prodotto1.")