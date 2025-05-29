#Traccia:
#Crea un insieme di 5 elementi e un altro insieme con 2 soli elementi scelti tra quelli del primo. Crea poi la loro unione e controlla che la sua cardinalità sia esattamente 5.

fiori1 = {"Rosa","Viola","Orchidea","Tulipano","Giglio"}
print(fiori1)

fiori2 = {"Rosa","Viola"}
print(fiori2)

fioriUnion = fiori1.union(fiori2)

stringa = "La cardinalità dell'unione è {}."

print(stringa.format(len(fioriUnion)))