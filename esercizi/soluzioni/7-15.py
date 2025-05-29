#Traccia:
#[db-profumi] Aggiungi la colonna “inVita” all’entità “naso” compilala con un valore booleano che indichi se il naso è ancora vivo.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")

mycursor = mydb.cursor()

#creazione comando per aggiungere una colonna
comando = "ALTER TABLE naso ADD COLUMN inVita BOOLEAN"

#creazione comando per impostare inVita a 1
comando2 = "UPDATE naso SET inVita = 1 WHERE nascitaNaso IS NOT NULL AND morteNaso IS NULL"

#creazione comando per impostare inVita a 0
comando3 = "UPDATE naso SET inVita = 0 WHERE morteNaso IS NOT NULL"

#esecuzione comandi
mycursor.execute(comando)
mycursor.execute(comando2)
mycursor.execute(comando3)

mydb.commit()