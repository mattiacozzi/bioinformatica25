#Traccia:
#Crea un algoritmo che permetta ad un utente di creare una lista e aggiungerci elementi finché preferisce. Chiedi successivamente se si vuole che venga mostrato il minimo o il massimo valore presenti nella lista. In base alla risposta fornita, mostra l'elemento corretto.

lista = []

choice = " "

while choice != "finito":
    choice = input("Inserisci un numero da aggiungere alla lista (digita \"finito\" per uscire):\n")
    if choice != "finito":
        choice = int(choice)
        lista.append(choice)

min = max = lista[0]

stringa = "Il valore più {} della lista è {}."

choice2 = input("Digita \"min\" per vedere il minimo valore inserito.\nDigita \"max\" per vedere il massimo valore inserito.\n")

if choice2 == "min":
    for x in lista:
        if x < min:
            min = x
    print(stringa.format("basso",min))
elif choice2 == "max":
    for x in lista:
        if x > max:
            max = x
    print(stringa.format("alto",max))
else:
    print("Errore di immissione.")