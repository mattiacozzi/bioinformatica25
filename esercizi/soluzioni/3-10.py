#Traccia:
#Scrivere un algoritmo che chieda un numero all'utente ed esegua la somma di tutti gli interi tra 0 e il numero inserito.

numero = int(input("Inserisci un numero positivo: "))

#creo la variabile per contare fino a numero
#è come un indicatore che mi dice a che numero sono arrivato
contatore = 1

#inizialmente la somma vale 0
somma = 0

#inizio a sommare, finché contatore non raggiunge numero
while (contatore <= numero):
    #la prima volta faccio 0+1=1, poi 1+2=3, poi 3+3=6, 6+4=10, ecc 
    somma = somma + contatore
    #ad ogni ciclo, passo al valore successivo per il contatore
    contatore = contatore + 1 

string = f"La somma di tutti i numeri da 0 a {numero} vale {somma}."
print(string)

#questo algoritmo può essere realizzato in forma più semplice facendo diminuire ad ogni ciclo il valore di "numero". Prova!