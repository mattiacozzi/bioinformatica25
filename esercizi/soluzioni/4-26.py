#Traccia:
#Crea un insieme di 3 elementi. Creane poi una copia e fai in modo che l'utente vi possa aggiungere due elementi. Controlla poi che il secondo insieme contenga il primo.

fiori1 = {"Rosa","Girasole","Viola"}
print("Insieme 1:")
print(fiori1)

fiori2 = set(fiori1)

fiori2.add(input("\nAggiungi un nuovo elemento: "))
fiori2.add(input("Aggiungi un altro elemento: "))

print("\nInsieme 2:")
print(fiori2)

print("\nLa proposizione:\n\n\t\"L'insieme 2 contiene l'insieme 1\"\n\nha il seguente valore di verità:")
print(fiori2.issuperset(fiori1))

