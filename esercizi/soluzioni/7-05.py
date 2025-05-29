#Traccia:
#[db-profumi] Aggiungi te stesso/a come “naso” nella tabella corretta e crea un nuovo profumo per il brand “Chanel”. Tu dovrai essere il naso per quel profumo.
import mysql.connector

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database="db-profumi")
mycursor = mydb.cursor()

#creazione comando di inserimento dati
comando = "INSERT INTO naso(nomeNaso, cognomeNaso, nascitaNaso) VALUES (%s, %s, %s);"

valori = ('Mattia', 'Cozzi', 1987)
#esecuzione comando con i valori impostati
mycursor.execute(comando, valori)
mydb.commit()

#salvo l'ID del nuovo naso in una variabile perché dovrò utilizzarlo
#va convertito in stringa per poterlo concatenare al comando che eseguirò
newId = str(mycursor.lastrowid)

#creazione nuovo comando di inserimento dati
comando2 = "INSERT INTO profumo(nomeProfumo,id_brand,annoProfumo,genere,id_naso,topNotes,middleNotes,baseNotes) VALUES ('Spooky Night', 1, 2025, 'Unisex', " + newId +", 'Gatto', 'Pelliccia di gatto', 'Croccantini');"

mycursor.execute(comando2)

mydb.commit()