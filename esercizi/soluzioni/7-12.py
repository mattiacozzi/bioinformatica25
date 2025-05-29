#Traccia:
#[db-cosmesi] Scrivi un algoritmo che richieda all’utente l’ID di un prodotto e chieda successivamente se vuole modificarne il prezzo. Se l’utente accetta, fai inserire un valore e aggiorna il record del prodotto.
import mysql.connector

#raccolta informazioni
id = int(input("Inserisci l'ID di un prodotto (1-216): "))

scelta = ""

while (scelta != "N"):
    scelta = input("Vuoi modificare il prezzo del prodotto? (Y/N)\n")

    if (scelta == "Y"):
        #connessione al db 
        mydb = mysql.connector.connect(
            host = "localhost", user = "root", password = "", database="db-cosmesi")
        mycursor = mydb.cursor()

        #raccolta informazioni
        newPrice = input("Inserisci il nuovo prezzo: ")

        #creazione comando
        comando = "UPDATE prodotto SET prezzoProdotto = %s WHERE ID_prodotto = %s;"
        valori = (newPrice, id)

        #esecuzione comando
        mycursor.execute(comando, valori)
        mydb.commit()
        print("Prezzo aggiornato.")

        scelta = "N"

    elif (scelta == "N"):
        print("Hai scelto di non fare nulla.")
    
    else:
        print("Comando non riconosciuto. Riprova.")

print("Goodbye!")
