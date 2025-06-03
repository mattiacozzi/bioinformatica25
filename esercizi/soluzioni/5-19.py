#Traccia:
#Richiedi all'utente la sua data di nascita (escludi ore, minuti, ecc.) e calcola l'età dell'utente in giorni.

import datetime

print("Inserisci la tua data di nascita:")

anno = int(input("Inserisci l'anno: "))
mese = int(input("Inserisci il mese: "))
giorno = int(input("Inserisci il giorno: "))

nascita = datetime.date(anno, mese, giorno)

today = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

distanza = (today - nascita).days

string = f"Sei in vita da {distanza} giorni."

print(string)

