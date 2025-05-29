#Traccia:
#Definisci una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.

def sommaTutto(lista):
    somma = 0
    for x in lista:
        somma = somma + x
    return somma

myList = [1, 4, 67, 4, 879, 34, 11]

print("La lista è:")
print(myList)
print("La somma di tutti gli elementi è:")
print(sommaTutto(myList))