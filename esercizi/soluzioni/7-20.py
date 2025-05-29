#Traccia:
#[db-cosmesi] Calcola la media delle valutazioni ricevute dai prodotti cosmetici.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT nomeProdotto, votoProdotto FROM prodotto"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

#preparo la somma e calcolo il numero di valori del risultato
totale = 0
numValori = len(result)

#eseguo la somma di tutti i secondi valori del risultato
for riga in range(numValori):
    totale = totale + result[riga][1]

print("La media delle valutazioni dei prodotti vale", totale/numValori)
