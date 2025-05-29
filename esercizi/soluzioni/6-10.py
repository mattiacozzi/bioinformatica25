#Traccia:
#Scrivi un algoritmo che mostri le tabelle del database “db-pharma”.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-pharma")
    
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

print("Ecco le tabelle del database di prodotti farmaceutici.")

for x in mycursor:
    print(x)