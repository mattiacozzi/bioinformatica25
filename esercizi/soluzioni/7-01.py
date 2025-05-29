#Traccia:
#Crea un database con un nome a tua scelta e inserisci in esso almeno due tabelle (ognuna con una chiave primaria) con una relazione che le lega. Mostra poi l'elenco delle tabelle che hai creato.
import mysql.connector
#connessione al server
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "")

mycursor = mydb.cursor()
#variabile per il nome del database
nome = "animaliDomestici"

#comando di creazione database
comando = "CREATE DATABASE " + nome
mycursor.execute(comando)

#connessione al db creato
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database=nome)
mycursor = mydb.cursor()

#comando di creazione tabelle
comando2 = """CREATE TABLE padrone (ID_padrone INT AUTO_INCREMENT,
nomePadrone VARCHAR(512),
indirizzo VARCHAR(512),
contatto  VARCHAR(512),
PRIMARY KEY (ID_padrone)
);
CREATE TABLE animale (ID_animale INT AUTO_INCREMENT,
nomeAnimale VARCHAR(512),
specie VARCHAR(512),
razza  VARCHAR(512),
id_padrone INT,
PRIMARY KEY (ID_animale),
FOREIGN KEY (id_padrone) REFERENCES padrone(ID_padrone)
)
"""
mycursor.execute(comando2)

#riconnessione al db aggiornato
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database=nome)
mycursor = mydb.cursor()

#comando per vedere le tabelle
mycursor.execute("SHOW TABLES")

print("Ecco le tabelle del database " + nome + ":")

for x in mycursor:
    print(x)