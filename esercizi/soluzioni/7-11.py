#Traccia:
#[db-profumi] Scrivi un algoritmo che richieda all’utente l’ID di un profumo e chieda successivamente quale attributo vuole modificare. Fai inserire il nuovo valore ed esegui l’operazione richiesta.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#raccolta informazioni
id = int(input("Scegli l'ID di un profumo da modificare (1-228): "))

campo = input("Quale campo vuoi modificare?\nnomeProfumo, id_brand, annoProfumo, genere, id_naso, topNotes, middleNotes, baseNotes\n")

newVal = input("Inserisci il nuovo valore del campo:\n")

#creazione comando
comando = "UPDATE profumo SET "+campo+" = %s WHERE ID_profumo = %s;"
valori = (newVal, id)

#esecuzione comando
mycursor.execute(comando, valori)
mydb.commit()