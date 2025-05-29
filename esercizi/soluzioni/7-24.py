#Traccia:
# [db-profumi] Estrai dal database i profumi femminili usciti tra il 1991 e il 2000 e ordinali per data di uscita.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT nomeProfumo, annoProfumo FROM profumo WHERE genere = 'Female' AND annoProfumo BETWEEN 1991 AND 2000 ORDER BY annoProfumo"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga)