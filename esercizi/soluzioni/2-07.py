#Traccia:
#Creare una stringa con una parola con un numero pari di lettere e stampare le due lettere centrali.

#creo la stringa
string = "Buongiorno" #10 lettere

#scopro la lunghezza della stringa e la dimezzo
lung = len(string)
meta = int(lung/2)

print(string[meta-1:meta+1])