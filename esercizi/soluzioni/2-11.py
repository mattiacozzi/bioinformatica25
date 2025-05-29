#Traccia:
#Partendo dalla variabile "numero" con valore a piacere, creare una stringa che dica "Il quadrato di X è Y".

#creo la variabile
numero = 23

#calcolo il quadrato
quadrato = pow(numero, 2)

#preparo la stringa
string = "Il quadrato di {} è {}"

#stampo la stringa coi valori
print(string.format(numero, quadrato))