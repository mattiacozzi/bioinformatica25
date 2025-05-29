#Traccia:
#Mostra le tabelle del database “mysql” preimpostato in XAMPP.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="mysql")
    
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

print("Ecco le tabelle del database predefinito di XAMPP.")
for x in mycursor:
    print(x)