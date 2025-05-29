#Traccia:
#Fai stampare a schermo l’elenco dei database presenti nel sistema, poi elimina il database dell’esercizio 1 e stampa la lista aggiornata.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

print("Eliminazione del database \'Gatti\' in corso.")

mycursor.execute("DROP DATABASE Gatti")

print("Database eliminato. Ecco la list aggiornata:")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)