#Traccia:
#In un cinema esistono 5 tipi di biglietti diversi. I bambini sotto i 6 anni pagano 3€, tra i 7 e i 12 anni pagano 5€, i ragazzi tra 13 e 18 anni pagano 7€, gli adulti pagano 10€ e infine gli anziani sopra i 70 anni entrano gratis. Scrivi un algoritmo che chieda quanti biglietti si vogliono acquistare e successivamente, per ogni biglietto, chieda l'età dell'acquirente e valuti quindi quanto si deve pagare. L'algoritmo deve infine mostrare il prezzo finale, cioè la somma di tutti i prezzi dei biglietti.

persone = int(input("Quanti biglietti vuoi acquistare? "))
totale = 0
spett = 1 #contatore di biglietti
#preparo le stringhe
string = f"Età spettatore {spett}: "

while (spett <= persone):
    age = int(input(string))
    if age < 7:
        prezzo = 3
    elif age < 13:
        prezzo = 5
    elif age < 19:
        prezzo = 7
    elif age < 71:
        prezzo = 10
    else:
        prezzo = 0
    string2 = f"Il costo del biglietto per spettatore {spett} è di {prezzo} euro."
    print(string2)
    totale = totale + prezzo #aggiorno il totale con il nuovo biglietto
    spett += 1 #aumento il valore del contatore

string3 = f"Il costo totale dei biglietti è {totale} euro."
print(string3)
