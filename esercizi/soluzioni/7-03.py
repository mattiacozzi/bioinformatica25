#Traccia:
#Inserisci un nuovo record nella tabella creata nell’esercizio precedente.
import mysql.connector

nome = "animaliDomestici"

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database=nome)
mycursor = mydb.cursor()

#creazione comando di inserimento dati
comando = "INSERT INTO veterinario(nomeVeterinario, indirizzo, contatto) VALUES (%s, %s, %s);"
#nota come non venga indicato il valore della colonna ID, che viene automaticamente incrementato
valori = ("Corrado Gentilissimo", "via Fausto Coppi 23, Milano", "corradogent@email.com")

#esecuzione comando con i valori impostati
mycursor.execute(comando, valori)

mydb.commit()