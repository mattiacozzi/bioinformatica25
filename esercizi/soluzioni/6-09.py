#Traccia:
#Scrivi un algoritmo che mostri le tabelle del database “db-profumi”.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
    
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

print("Ecco le tabelle del database di profumi.")

for x in mycursor:
    print(x)