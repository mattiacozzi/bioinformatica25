#Traccia:
#[db-cosmesi] Estrai dal database i tre prodotti più economici.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT nomeProdotto, prezzoProdotto FROM prodotto ORDER BY prezzoProdotto LIMIT 3"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga)