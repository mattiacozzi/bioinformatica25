#Traccia:
#Dopo aver ricreato i database “Gatti”, “Cani” e “Pappagalli”, scrivi un algoritmo che mostri all’utente l’elenco dei database presenti nel sistema. Fai digitare all’utente il nome del database che vuole eliminare ed esegui l’eliminazione.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Gatti")
mycursor.execute("CREATE DATABASE Cani")
mycursor.execute("CREATE DATABASE Pappagalli")

mycursor.execute("SHOW DATABASES")

print("Ecco la lista dei database attualmente presenti nel sistema:")
for x in mycursor:
    print(x)

nome = input("Inserisci il nome del database che vuoi eliminare: ")

comando = "DROP DATABASE " + nome

mycursor.execute(comando)

print("Database " + nome + " eliminato")

mycursor.execute("SHOW DATABASES")

print("Ecco la lista dei database attualmente presenti nel sistema:")
for x in mycursor:
    print(x)