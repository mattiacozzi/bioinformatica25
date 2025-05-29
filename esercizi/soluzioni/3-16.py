#Traccia:
#Usando la funzione range(), scrivere un algoritmo che chieda un numero all'utente e che mostri tutti i numeri interi da 0 a quel numero.

numero = int(input("Inserisci un numero intero: "))

for x in range(numero+1):
    print(x)