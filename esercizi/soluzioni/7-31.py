#Traccia:
#[db-profumi] Estrai dal database una tabella che mostri il nome di ogni profumo e il nome del brand che lo ha prodotto.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT * FROM profumo LEFT JOIN brand ON profumo.id_brand = brand.ID_brand"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga[1], "prodotto da", riga[10])