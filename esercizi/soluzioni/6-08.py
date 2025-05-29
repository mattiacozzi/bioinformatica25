#Traccia:
#Scrivi un algoritmo che mostri le tabelle del database “db-cosmesi”.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
    
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

print("Ecco le tabelle del database di prodotti cosmetici.")

for x in mycursor:
    print(x)