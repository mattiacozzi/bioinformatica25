#Traccia:
#Scrivi un algoritmo che richieda all'utente un numero intero X e restituisca in che giorno della settimana saremo tra X giorni.

import datetime

#creo la lista dei giorni nella settimana
settimana = ["Lunedì","Martedì","Mercoledì","Giovedì","Venerdì","Sabato","Domenica"]

#chiedo un numero intero all'utente
numero = int(input("Inserisci un numero intero: "))

#salvo la data di oggi in una variabile
today = datetime.datetime.now()

#assegno alla variabile giorno il nome del giorno
#l'indice è ottenuto grazie al metodo weekday() applicato alla data di oggi
#(vedi documentazione del modulo datetime)
giorno = settimana[today.weekday()]

#calcolo il nuovo indice con l'operatore modulo e lo uso per recuperare il
#nome del prossimo giorno della settimana che mi interessa
prossimo = settimana[(today.weekday() + numero)%7]

string = f"Oggi è {giorno}.\nTra {numero} giorni sarà {prossimo}."

#stampo la stringa
print(string)