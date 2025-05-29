#Traccia:
#Scrivi un algoritmo che richieda all'utente la data del suo ultimo aggiornamento della password. Se tale data risale a più di 100 giorni fa, richiede all'utente una nuova password e la salva in una variabile. Stampa poi a schermo una stringa che abbia la stessa lunghezza della password ma in cui tutti i caratteri sono stati sostituiti da asterischi.

import datetime

print("Inserisci la data dell'ultimo aggiornamento della password:")

anno = int(input("Anno: "))
mese = int(input("Mese: "))
giorno = int(input("Giorno: "))

lastChange = datetime.date(anno, mese, giorno)

today = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

distanza = (today - lastChange).days

if distanza < 100:
    print("La tua password è recente, non deve essere cambiata.")
else:
    print("Sono passati più di 100 giorni dall'ultima volta che hai aggiornato la password.")
    password = input("Inserisci una nuova password: \n")
    passAsterischi = ""
    for i in password:
        passAsterischi = passAsterischi + "*"
    print("\n\n\n\n\n\n\n\n\n\n\n\n\nPassword aggiornata con successo.\nNuova password: " + passAsterischi)
