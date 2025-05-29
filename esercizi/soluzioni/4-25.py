#Traccia:
#Crea due insiemi, eventualmente con elementi in comune, e scrivi un algoritmo che confermi che la cardinalità della loro differenza simmetrica è uguale alla somma delle cardinalità dei due insiemi meno il doppio della cardinalità dell'intersezione tra essi.


fiori1 = {"Rosa","Girasole","Viola"}

fiori2 = {"Rosa","Viola","Orchidea","Tulipano","Giglio","Margherita"}

fioriIntersezione = fiori1.intersection(fiori2)
fioriDiff = fiori1.symmetric_difference(fiori2)

print("Ecco la differenza simmetrica degli insiemi:")
for x in fioriDiff:
    print(x)

stringa = "La cardinalità dell'insieme {} è {}."
print(stringa.format("1",len(fiori1)))
print(stringa.format("2",len(fiori2)))
print(stringa.format("intersezione",len(fioriIntersezione)))
print(stringa.format("differenza",len(fioriDiff)))

print("La proposizione:\n\n\t\"La cardinalità della differenza simmetrica\n\ttra due insiemi è uguale alla somma delle\n\tloro cardinalità meno il doppio della\n\tcardinalità della loro intersezione.\"\n\nha il seguente valore di verità:")
print(len(fiori1) + len(fiori2) - 2*len(fioriIntersezione) == len(fioriDiff))