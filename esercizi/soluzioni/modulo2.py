import math

#prima funzione
def welcome():
    print("Questo è il mio risolutore di equazioni di secondo grado.")
    print("Provalo!")
    
#seconda funzione
def calcolaDelta(a, b, c):
    delta = b*b - 4*a*c
    string = "Il discriminante vale {}."
    print(string.format(delta))
    return delta

#terza funzione
def risolvi(a, b, d):
    if (d < 0):
        print("L'equazione non ha soluzioni.")
    elif (d == 0):
        string = "L'equazione ha una sola soluzione:\nx = {}"
        x = -b/(2*a)
        print(string.format(x))
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        string = "L'equazione ha due soluzioni:\nx1 = {}\tx2 = {}"
        print(string.format(x1, x2))