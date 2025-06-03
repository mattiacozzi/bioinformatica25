#Traccia:
#Scrivi un algoritmo che richieda all'utente di inserire un numero intero e che stampi poi a schermo un numero casuale compreso tra 1 e il numero inserito (attenzione a quest'ultima richiesta).

import random

numero = int(input("Inserisci un numero intero: "))

#inizializzo la generazione di numeri casuali
random.seed()

#genero un numero casuale nel range di mio interesse
x = random.randint(1, numero)

#mostro il numero
string = f"Ecco un numero casuale tra 1 e {numero}:\n{x}"
print(string)