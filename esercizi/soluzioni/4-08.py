#Traccia:
#Crea una lista con un numero di elementi a piacere, stampala e crea un algoritmo che chieda all'utente cosa vuole fare: modificare un elemento, aggiungerne uno in una certa posizione oppure eliminarlo. Esegui l'operazione che l'utente ha scelto e mostra la stringa modificata.

fibo = [1,
        1,
        2,
        3,
        5,
        8,
        13,
        ]

print("Sequenza predefinita:")
for x in fibo:
    print(x)

choice = " "

while (choice != "m" and choice != "a" and choice != "d"):
    choice = input("Cosa vuoi fare?\nm = modifica un elemento \ta = aggiungi un elemento\td = elimina un elemento\n")

if choice == "m":
    index = int(input("Hai scelto di modificare un elemento. Inserisci l'indice dell'elemento da modificare: "))
    input = input("Inserisci il nuovo valore: ")
    fibo[index] = input
elif choice == "a":
    index = int(input("Hai scelto di aggiungere un elemento. Inserisci l'indice della posizione in cui aggiungerlo: "))
    input = input("Inserisci il nuovo valore: ")
    fibo.insert(index, input)
elif choice == "d":
    index = int(input("Hai scelto di eliminare un elemento. Inserisci l'indice dell'elemento da eliminare: "))
    fibo.pop(index)

print("Sequenza modificata:")
for x in fibo:
    print(x)