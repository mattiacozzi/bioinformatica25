#Traccia:
#Scrivi un algoritmo che chieda all’utente il nome del nuovo database e crei poi un database con il nome inserito.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "")

mycursor = mydb.cursor()

nome = input("Inserisci un nome per il nuovo database: ")

comando = "CREATE DATABASE " + nome

mycursor.execute(comando)