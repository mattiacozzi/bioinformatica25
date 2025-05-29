#Traccia:
#[db-cosmesi] Aggiungi l’attributo “Nazione” all’entità “brand” e compila almeno due record con due diverse nazionalità.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando per aggiungere colonne
comando = "ALTER TABLE brand ADD COLUMN nazione VARCHAR(512)"

#esecuzione comando
mycursor.execute(comando)

#creazione comandi per riempire la nuova colonna
comando2 = "UPDATE brand SET nazione = 'France' WHERE ID_brand = 2;"
comando3 = "UPDATE brand SET nazione = 'Japan' WHERE ID_brand = 12;"

#esecuzione comandi
mycursor.execute(comando2)
mycursor.execute(comando3)
mydb.commit()