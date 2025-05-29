#Traccia:
#Crea una lista di 5 elementi tutti nulli. Chiedi poi all'utente di inserire dei valori nella lista e calcola la somma di tutti i valori inseriti. Mostra come output "La somma di X, Y, Z, ... è W".

numeri = [0, 0, 0, 0, 0]

tot = 0

for x in range(5):
    val = int(input("Inserisci un numero intero da aggiungere alla lista: "))
    numeri[x] = val
    tot = tot + val

string = "La somma di {}, {}, {}, {} e {} è {}."

print(string.format(numeri[0], numeri[1], numeri[2], numeri[3], numeri[4], tot))