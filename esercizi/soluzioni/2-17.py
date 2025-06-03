#Traccia:
#Utilizzare la formattazione delle stringhe per chiedere all'utente un numero intero e mostrare "Il numero binario di X è Y".

#chiedo un numero e lo converto in intero
numero = int(input("Inserisci un numero: "))

#converto in binario e salvo in una nuova variabile
binario = bin(numero)

#imposto la stringa
string = f"Il binario di {numero} è {binario}"

#stampo la stringa
print(string)