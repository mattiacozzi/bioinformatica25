#Traccia:
#Scrivere un algoritmo che chieda all'utente un valore numerico e mostri la sequenza dei numeri di Fibonacci minori del numero inserito.

max = int(input("Inserisci un valore massimo (>0) per i termini della sequenza di Fibonacci: "))

#imposto i primi due valori
primo = 1
secondo = 1

#presento la sequenza
string = f"Ecco la sequenza di Fibonacci con valori minori o uguali a {max}:"
print(string)

#stampo i primi valori
print(primo)
print(secondo)

#finché il prossimo termine è minore del massimo
while primo+secondo < max:
    next = primo + secondo  #calcola il nuovo termine
    print(next)             #stampa il nuovo termine
    primo = secondo         #aggiorna i valori degli addendi
    secondo = next