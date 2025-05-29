#Traccia:
#Scrivi un algoritmo che chieda all’utente quale tra le seguenti operazioni vuole compiere: mostrare i db, creare un nuovo db, eliminare un db esistente. In base alla scelta dell’utente, esegui l’operazione richiesta e, se necessario, mostra la lista dei db aggiornata.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "")
    
mycursor = mydb.cursor()

scelta = ""
while (scelta != "X"):
    scelta = input("Quale operazione vuoi compiere?\nS = Mostra i db\nC = crea un db\nD = elimina db\nX = esci dal programma\n")

    if (scelta == "S"):
        mycursor.execute("SHOW DATABASES")
        print("Ecco la lista dei database attualmente presenti nel sistema:")
        for x in mycursor:
            print(x)
    elif (scelta =="C"):
        print("Hai scelto di creare un nuovo database.")
        nome = input("Inserisci il nome del nuovo database:\n")
        comando = "CREATE DATABASE " + nome
        mycursor.execute(comando)
        print("Database " + nome + " creato.")
    elif (scelta =="D"):
        print("Hai scelto di eliminare un database.")
        nome = input("Inserisci il nome del database da eliminare:\n")
        comando = "DROP DATABASE " + nome
        mycursor.execute(comando)
        print("Database " + nome + " eliminato.")
    elif (scelta == "X"):
        print("Arrivederci!")
    else:
        print("Inserimento non valido, riprova.")

