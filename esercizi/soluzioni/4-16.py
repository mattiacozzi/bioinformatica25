#Traccia:
#Crea una tupla di valori numerici a tuo piacimento e crea poi un'altra tupla che contenga solo i valori della prima maggiori di 5. Mostra entrambe le tuple a schermo.

fibo = (
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    )

#lista vuota
fiboList = []

print("Tupla originaria: ")
#scorro la tupla
for x in range(len(fibo)):
    #stampo i valori della tupla
    print(fibo[x])
    #se il valore è maggiore di 5, lo aggiungo alla lista
    if fibo[x] > 5:
        fiboList.append(fibo[x])    

#creo la nuova tupla
fibo2 = tuple(fiboList)

print("Tupla degli elementi maggiori di 5: ")
for x in fibo2:
    print(x)