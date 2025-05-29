#Traccia:
#[db-profumi] Per i nasi il cui anno di nascita e morte è indicato, calcola e mostra a schermo quanti anni hanno vissuto.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT * FROM naso WHERE morteNaso IS NOT NULL"

#esecuzione comando
mycursor.execute(comando)

result = mycursor.fetchall()

for riga in result:
    print(riga[1], riga[2], "ha vissuto", riga[4]- riga[3],"anni.")