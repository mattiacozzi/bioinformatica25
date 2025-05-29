#Traccia:
#[db-cosmesi] Estrai dal database una tabella che mostri la categoria di appartenenza di tutti i prodotti con valutazione maggiore di 4.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT * FROM prodotto LEFT JOIN categoria ON prodotto.id_categoria = categoria.ID_categoria WHERE prodotto.votoProdotto > 4"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga[1], "appartiene alla categoria", riga[9])