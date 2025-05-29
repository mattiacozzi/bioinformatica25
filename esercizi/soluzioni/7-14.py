#Traccia:
#[db-profumi] Elimina la colonna creata nell’esercizio precedente.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando per aggiungere colonne
comando = "ALTER TABLE naso DROP COLUMN nazione"

#esecuzione comando
mycursor.execute(comando)
mydb.commit()