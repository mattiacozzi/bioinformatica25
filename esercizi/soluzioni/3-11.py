#Traccia:
#Scrivere un algoritmo che chieda un numero all'utente e calcoli il fattoriale di quel numero.

numero = int(input("Inserisci un numero positivo: "))

#creo la variabile per contare fino a numero
#è come un indicatore che mi dice a che numero sono arrivato
contatore = 1

#inizialmente il prodotto vale 1
prod = 1

#inizio a moltiplicare, finché contatore non raggiunge numero
while (contatore <= numero):
    #la prima volta faccio 0+1=1, poi 1+2=3, poi 3+3=6, 6+4=10, ecc 
    prod = prod * contatore
    #ad ogni ciclo, passo al valore successivo per il contatore
    contatore = contatore + 1 

string = "{}! =  {}."
print(string.format(numero, prod))