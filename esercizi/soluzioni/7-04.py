#Traccia:
#Inserisci almeno quattro nuovi record nella stessa tabella dell’esercizio precedente, usando la sintassi per l’inserimento multiplo.

import mysql.connector

nome = "animaliDomestici"

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database=nome)
mycursor = mydb.cursor()

#creazione comando di inserimento dati
comando = "INSERT INTO veterinario(nomeVeterinario, indirizzo, contatto) VALUES (%s, %s, %s);"
#creo una lista di tuple
valori = [
            ("Corrado Gentilissimo", "via Fausto Coppi 23, Milano", "corradogent@email.com"),
            ("Barbara Burbera", "via Achille 98, Bresso", "barburb@email.com"),
            ("Antonio Vicentino", "via Protagora 4, San Giuliano Milanese", "tonyvice@email.com"),
]
#esecuzione comando con i valori impostati
mycursor.executemany(comando, valori)

mydb.commit()