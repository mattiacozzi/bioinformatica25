#Traccia:
#Scrivere un programma che chieda un input numerico all'utente e ne calcoli il quadrato, mostrandolo a schermo.

#chiedo un numero e lo converto in intero
numero = int(input("Inserisci un numero: "))

#calcolo il quadrato
quad = pow(numero, 2)

#imposto la stringa
string = f"Il quadrato di {numero} è {quad}."

#stampo la stringa
print(string)