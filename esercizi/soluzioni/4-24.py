#Traccia:
#Crea due insiemi disgiunti e scrivi un algoritmo che confermi che l'intersezione tra essi è vuota.

fiori1 = {"Rosa","Girasole","Viola"}

fiori2 = {"Orchidea","Tulipano","Giglio","Margherita"}

fioriIntersezione = fiori1.intersection(fiori2)

print("La proposizione:\n\n\t\"La cardinalità dell'insieme intersezione \n\ttra due insiemi disgiunti è 0.\"\n\nha il seguente valore di verità:")
print(len(fioriIntersezione) == 0)