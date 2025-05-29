#Traccia:
#Scrivi un algoritmo in cui viene chiesto all'utente di inserire dei dati numerici fino a che non digita "X". I dati devono essere salvati in una lista. Definisci e implementa una funzione che stampi solo i valori della lista maggiori della media dei valori contenuti nella lista stessa.

def sopraMedia(lista):
    somma = 0
    for x in lista:
        somma = somma + x
    media = somma / len(lista)
    print("Ecco la lista che hai inserito: ")
    print(lista)
    print("La media è " + str(media))
    print("I valori maggiori della media sono:")
    for x in lista:
        if x > media:
            print(x)

myList = []

choice = " "

while choice != "X":
    choice = input("Inserisci un nuovo numero alla lista (digita \"X\" per terminare):\n")
    if choice != "X":
        myList.append(int(choice))

sopraMedia(myList)