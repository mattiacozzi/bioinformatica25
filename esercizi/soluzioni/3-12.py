#Traccia:
#Scrivere un algoritmo che chieda numeri all'utente e li sommi. L'algoritmo deve proseguire fino a che l'utente non digita 0.

x = int(input("Inserisci il primo numero (0 per uscire): "))

tot = x

while (x != 0): #ripeti finché non viene inserito 0
    x = int(input("Inserisci il prossimo numero (0 per uscire): "))
    tot = tot + x   #aggiorno il valore del totale, se l'utente inserisce 0, il valore del totale non cambia

string = f"La somma di tutti i numeri che hai immesso vale {tot}."
print(string)