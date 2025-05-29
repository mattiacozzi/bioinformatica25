#Traccia:
#[db-cosmesi] Stampa a schermo l’elenco dei prodotti cosmetici che hanno una valutazione uguale o maggiore di 4.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT nomeProdotto, votoProdotto FROM prodotto WHERE votoProdotto >= 4"

#esecuzione comando
mycursor.execute(comando)

result = mycursor.fetchall()

for riga in result:
    print(riga)