#Traccia:
#[db-profumi] Estrai dal database i profumi maschili usciti dopo il 2007.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT nomeProfumo, annoProfumo FROM profumo WHERE genere = 'Male' AND annoProfumo > 2007"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga)