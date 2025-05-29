#Traccia:
#Aggiungi una nuova entità (collegata ad almeno una delle altre) al database dell’esercizio precedente. Mostra poi il nuovo elenco delle tabelle.
import mysql.connector

nome = "animaliDomestici"

#connessione al db 
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database=nome)
mycursor = mydb.cursor()

#comando di creazione tabelle
comando = """CREATE TABLE veterinario (ID_veterinario INT AUTO_INCREMENT,
nomeVeterinario VARCHAR(512),
indirizzo VARCHAR(512),
contatto  VARCHAR(512),
PRIMARY KEY (ID_veterinario)
);
CREATE TABLE visita (ID_visita INT AUTO_INCREMENT,
dataVisita VARCHAR(512),
id_animale INT,
id_veterinario INT,
PRIMARY KEY (ID_visita),
FOREIGN KEY (id_animale) REFERENCES animale(ID_animale),
FOREIGN KEY (id_veterinario) REFERENCES veterinario(ID_veterinario)
)
"""
mycursor.execute(comando)

#riconnessione al db aggiornato
mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "", database=nome)
mycursor = mydb.cursor()

#comando per vedere le tabelle
mycursor.execute("SHOW TABLES")

print("Ecco le tabelle del database " + nome + ":")

for x in mycursor:
    print(x)