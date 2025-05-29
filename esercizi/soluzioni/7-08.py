#Traccia:
#[db-cosmesi] Scrivi un algoritmo che elimini tutti i prodotti il cui ID è multiplo di 19.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-cosmesi")
mycursor = mydb.cursor()

numero = 0

#per stabilire quante volte va eseguito il ciclo,
#andiamo a vedere quanti record contiene la tabella
#"profumo", dividiamo il totale per 19 e arrotondiamo
#per eccesso
while numero < 11:
    elim = numero * 19
    
    #creazione comando
    comando = "DELETE FROM prodotto WHERE ID_prodotto = %s"
    valore = (numero * 19,)
    
    #esecuzione comando
    mycursor.execute(comando, valore)
    mydb.commit()

    #aumento il valore del contatore
    numero += 1