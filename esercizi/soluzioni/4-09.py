#Traccia:
#Chiedi all'utente da quanti elementi deve essere formata una certa lista. Scrivi successivamente un ciclo per farla riempire con valori scelti dall'utente. Quando la lista è completa, mostrala ordinata in ordine alfabetico.

#creo una lista vuota
lista = []

#chiedo quanti elementi vanno inseriti
dim = int(input("Da quanti elementi deve essere formata la lista? "))

#chiedo una parola e la aggiungo alla lista
for x in range(dim):
    parola = input("Inserisci una parola: ")
    lista.append(parola)

#ordino la lista
lista.sort()


#stampo la lista
print("Ecco la lista che hai creato in ordine alfabetico: ")
for x in lista:
    print(x)