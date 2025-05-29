#Traccia:
#Scrivi un algoritmo che permetta di aggiungere elementi ad una lista fino a che l'utente non digita "finito". Mostra poi la lista ottenuta in ordine alfabetico e in ordine alfabetico inverso, con un numero davanti ad ogni elemento che ne indichi la posizione nella lista.

lista = []

choice = " "

while choice != "finito":
    choice = input("Inserisci un nuovo elemento della lista (digita \"finito\" per uscire):\n")
    if choice != "finito":
        lista.append(choice)

lista.sort()

string = "{}) {}"

print("Ecco la tua lista in ordine alfabetico: ")
for x in range(len(lista)):
    print(string.format(x+1, lista[x]))

lista.sort(reverse=True)

print("Ecco la tua lista in ordine alfabetico inverso: ")
for x in range(len(lista)):
    print(string.format(x+1, lista[x]))