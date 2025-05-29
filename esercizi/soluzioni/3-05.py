#Traccia:
#Usando una selezione annidata, creare un algoritmo che chieda all'utente di inserire i tre coefficienti di una equazione di secondo grado in forma canonica e che, se possibile, risolva l'equazione.

import math

#welcome
print("Questo è un risolutore di equazioni di secondo grado!")

#input dei coefficienti e conversione in float
a = float(input("Inserisci il primo coefficiente: "))
b = float(input("Inserisci il secondo coefficiente: "))
c = float(input("Inserisci il terzo coefficiente: "))

#calcolo del delta
delta = b*b - 4*a*c

if (delta < 0):
    print("L'equazione non ha soluzioni.")
else:
    if (delta == 0):
        x = (-b)/(2*a)
        string = "L'equazione ha una sola soluzione: x = {}"
        print(string.format(x))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        string = "L'equazione ha due soluzioni: x = {} v x = {}"
        print(string.format(x1, x2))