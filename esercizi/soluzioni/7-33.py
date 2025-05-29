#Traccia:
#[db-profumi] Estrai dal database a quanti anni di età ognuno dei nasi di cui conosci l’anno di nascita hanno creato i profumi a loro associati.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando
comando = "SELECT * FROM profumo LEFT JOIN naso ON profumo.id_naso = naso.ID_naso WHERE profumo.id_naso IS NOT NULL AND naso.nascitaNaso IS NOT NULL"

#esecuzione comando
mycursor.execute(comando)

#salvo il risultato
result = mycursor.fetchall()

print("Ecco l'elenco dei prodotti richiesti:")
#stampo i nomi dei prodotti
for riga in result:
    print(riga[1], "creato da", riga[10], riga[11], "a", riga[3] - riga[12], "anni.")