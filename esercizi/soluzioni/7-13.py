#Traccia:
#[db-profumi] Aggiungi l’attributo “Nazione” all’entità “naso” e compila almeno due record con due diverse nazionalità.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando per aggiungere colonne
comando = "ALTER TABLE naso ADD COLUMN nazione VARCHAR(512)"

#esecuzione comando
mycursor.execute(comando)

#creazione comandi per riempire la nuova colonna
comando2 = "UPDATE naso SET nazione = 'France' WHERE ID_naso = 15;"
comando3 = "UPDATE naso SET nazione = 'Germany' WHERE ID_naso = 43;"

#esecuzione comandi
mycursor.execute(comando2)
mycursor.execute(comando3)
mydb.commit()