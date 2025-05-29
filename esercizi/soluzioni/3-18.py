#Traccia:
#Scrivere un algoritmo che chieda all'utente di inserire una parola e che la scriva successivamente al contrario (in un'unica stringa).

parola = input("Inserisci una parola: ")

for x in range(len(parola)):
    print(parola[-(x+1)])