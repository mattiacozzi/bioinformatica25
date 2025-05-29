#Traccia:
#[db-cosmesi] Estrai dal database i prodotti con una valutazione superiore a 4.2 adatti a pelli sensibili.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT nomeProdotto FROM prodotto WHERE votoProdotto >= 4.2 AND pelliSensibili = 1"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga)