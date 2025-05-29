#Traccia:
#[db-profumi] Scrivi un algoritmo che permetta all’utente di modificare il nome di un profumo a tua scelta.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#modifico il nome di un profumo
comando = "UPDATE profumo SET nomeProfumo = 'Eau de Coco' WHERE nomeProfumo = 'Coco'"

mycursor.execute(comando)
mydb.commit()