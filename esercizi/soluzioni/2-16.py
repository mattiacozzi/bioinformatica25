#Traccia:
#Utilizzare la formattazione delle stringhe per ottenere "Il numero binario di 42 è 0b101010". Per il binario utilizzare la funzione bin(numero).

#creo la variabile
numero = 42

#converto in binario e salvo in una nuova variabile
binario = bin(numero)

#imposto la stringa
string = f"Il binario di {numero} è {binario}"

#stampo la stringa
print(string)
