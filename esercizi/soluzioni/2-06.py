#Traccia:
#Creare una stringa casuale e stamparne gli ultimi tre caratteri usando la funzione len().

#creo la stringa
string = "Hello world!"

#scopro quanto è lunga e salvo il valore in una variabile
lung = len(string)

#stampo i caratteri che mi interessano
print(string[lung-3:lung])