#Traccia:
#[db-cosmesi] Scrivi un algoritmo che elimini tutti i prodotti del brand “Dior”
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

#il brand Dior ha ID pari a 6
comando = "DELETE FROM prodotto WHERE id_brand = 6"

mycursor.execute(comando)
mydb.commit()