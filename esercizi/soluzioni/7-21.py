#Traccia:
#[db-cosmesi] Estrai dal database i prodotti che costano più di 8 € e che hanno una valutazione superiore a 4.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT nomeProdotto FROM prodotto WHERE prezzoProdotto > 8 AND votoProdotto >= 4"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga)