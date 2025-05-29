#Traccia:
#Crea due insiemi disgiunti e stampali. Crea poi la loro unione e stampala. Concludi poi con un algoritmo che controlla se la somma delle cardinalità del primo e del secondo insieme è uguale alla cardinalità dell'insieme unione.

fiori1 = {"Rosa","Girasole","Viola"}

fiori2 = {"Orchidea","Tulipano","Giglio","Margherita"}

fioriUnione = fiori1.union(fiori2)

print("Ecco l'unione degli insiemi:")
for x in fioriUnione:
    print(x)

stringa = "La cardinalità dell'insieme {} è {}."
print(stringa.format("1",len(fiori1)))
print(stringa.format("2",len(fiori2)))
print(stringa.format("unione",len(fioriUnione)))

print("La proposizione:\n\n\t\"La cardinalità dell'insieme unione \n\tè uguale alla somma delle cardinalità\n\tdi due insiemi disgiunti\"\n\nha il seguente valore di verità:")
print(len(fiori1) + len(fiori2) == len(fioriUnione))