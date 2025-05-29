#Traccia:
#Crea due insiemi con almeno un elemento in comune. Stampa prima gli insiemi e poi la loro intersezione.

fiori1 = {"Rosa","Girasole","Viola"}

fiori2 = {"Rosa","Viola","Orchidea","Tulipano","Giglio","Margherita"}

fioriIntersezione = fiori1.intersection(fiori2)

#stampo il primo insieme
print("Ecco il primo insieme: ")
for x in fiori1:
    print(x)

#stampo il secondo insieme
print("\nEcco il secondo insieme: ")
for x in fiori2:
    print(x)

#stampo l'intersezione
print("\nEcco l'intersezione degli insiemi:")
for x in fioriIntersezione:
    print(x)