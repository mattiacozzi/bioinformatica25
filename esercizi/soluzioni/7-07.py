#Traccia:
#[db-profumi] Scrivi un algoritmo che chieda all’utente se vuole creare un nuovo profumo oppure eliminarne uno già esistente (usa l’ID del prodotto per l’eliminazione, non il nome). Esegui, se l’utente ha digitato tutto correttamente, l’operazione richiesta. Se l’utente ha commesso errori, mostra un messaggio di errore e chiedi di nuovo cosa si vuole fare.
import mysql.connector

#funzione per creare un nuovo prodotto
def creaProf():
    #raccolta delle informazioni
    nomeProf = input("Inserisci un nuovo nome per il profumo: ")
    brand = input("Inserisci il codice del brand (1-8): ")
    anno = input("Inserisci l'anno di rilascio del profumo: ")
    genere = input("Inserisci il genere (Male, Female, Unisex): ")
    naso = input("Inserisci l'ID del naso (1-45): ")
    topNotes = input("Inserisci le note di testa: ")
    middleNotes = input("Inserisci le note di cuore: ")
    baseNotes = input("Inserisci le note di fondo: ")

    #creazione comando
    comando = "INSERT INTO profumo(nomeProfumo, id_brand, annoProfumo, genere, id_naso, topNotes, middleNotes, baseNotes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    valori = (nomeProf, brand, anno, genere, naso, topNotes, middleNotes, baseNotes, )

    #connessione al db 
    mydb = mysql.connector.connect(
        host = "localhost", user = "root", password = "", database="db-profumi")
    mycursor = mydb.cursor()

    #esecuzione comando
    mycursor.execute(comando,valori)
    mydb.commit()

    #stampa conferma
    newId = str(mycursor.lastrowid)
    print("Aggiunto un nuovo profumo con ID " + newId)

def eliminaProf():
    #raccolta delle informazioni
    elim = input("Inserisci l'ID del profumo da eliminare: ")

    #creazione comando
    comando = "DELETE FROM profumo WHERE ID_profumo = " + elim

    #connessione al db 
    mydb = mysql.connector.connect(
        host = "localhost", user = "root", password = "", database="db-profumi")
    mycursor = mydb.cursor()

    #esecuzione comando
    mycursor.execute(comando)
    mydb.commit()

    print("Eliminato il profumo con ID " + elim)
    

print("Welcome!")

scelta = ""

while (scelta != "X"):
    scelta = input("Che cosa vuoi fare?\nC = crea nuovo profumo\tD = elimina un profumo\tX=esci\n")
    if (scelta == "C"):
        creaProf()
        scelta = "X"
    elif (scelta == "D"):
        eliminaProf()
        scelta = "X"
    elif (scelta != "X"):
        print("Errore di immissione. Riprova.")

print("Goodbye!")



