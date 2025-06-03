#Traccia:
#Richiedi un numero intero positivo all'utente e calcola il logaritmo naturale di quel numero.

import math

numero = float(input("Inserisci un numero di cui calcolare il logaritmo naturale: "))
risultato = math.log(numero)

string = f"Il logaritmo naturale di {numero} vale {risultato}."
print(string)