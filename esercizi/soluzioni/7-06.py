#Traccia:
#[db-cosmesi] Crea un algoritmo che chieda all’utente tutti i dati di un nuovo prodotto. Aggiungi il nuovo prodotto alla tabella corretta e mostra il suo ID a schermo.

import mysql.connector

nomeProd = str(input("Inserisci un nuovo nome per il prodotto cosmetico: "))
brand = input("Inserisci il codice del brand (1-12): ")
categoria = input("Inserisci la categoria (1-5): ")
prezzo = input("Inserisci il prezzo: ")
voto = input("Inserisci la valutazione (1.0-5.0): ")
ingredienti = input("Inserisci la lista degli ingredienti: ")
pelli = input("È adatto a pelli sensibili? (1=sì, 0=no) ")


#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#creazione comando di inserimento dati
comando = "INSERT INTO prodotto(nomeProdotto, id_brand, id_categoria, prezzoProdotto, votoProdotto, ingredienti, pelliSensibili) VALUES (%s, %s, %s, %s, %s, %s, %s);"

valori = (nomeProd, brand, categoria, prezzo, voto, ingredienti, pelli)
#esecuzione comando
mycursor.execute(comando, valori)
mydb.commit()

newId = str(mycursor.lastrowid)
print("Aggiunto un nuovo prodotto con ID " + newId)