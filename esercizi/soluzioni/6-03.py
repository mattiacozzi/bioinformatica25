#Traccia:
#Fai stampare a schermo l’elenco dei database presenti sul tuo computer (alcuni sono preimpostati in XAMPP) e controlla che il database creato nell’esercizio 1 esista.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)