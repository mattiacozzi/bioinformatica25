#Traccia:
#Scrivere un algoritmo che chieda all'utente di inserire una parola e che controlli se tale parola è palindroma. Suggerimento: prima di eseguire il controllo, convertire tutta la parola in minuscolo.

parola = input("Inserisci una parola: ")

#converto in minuscolo
parola = parola.lower()

#poiché il devo controllare la prima e l'ultima lettera,
#poi la seconda e la penultima, ecc., il mio controllo
#deve arrivare solo fino a metà parola
contatore = int(len(parola) / 2)

#valore iniziale del controllo
check = True

#scorro la parola fino a dove mi interessa
for x in range(contatore+1):
    #se la prima/seconda/terza lettera sono diverse dall'ultima/penultima/terzultima, ecc
    if parola[x] != parola[-(x+1)]:
        #aggiorna la variabile del controllo
        check = False
        #esci dal ciclo for (basta una lettera diversa per avere una parola NON palindroma)
        break

print("Risultato: ")
if check:
    print("La stringa è palindroma.")
else:
    print("La stringa non è palindroma.")