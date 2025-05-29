#Traccia:
#Scrivi un algoritmo che crea una copia di un certo file di testo in una nuova cartella chiamata ``backup''.

import os

#controlla se esiste la cartella 'backup', altrimenti la crea
if os.path.exists("backup"):
    print("La directory \'backup\' esiste già, non è necessario crearla.")
else:
    os.mkdir("backup")
    print("Directory \'backup\' creata.")

#apri il file
lonfo = open("lonfo1.txt","r")

#copia il contenuto del file in una variabile
contenuto = lonfo.read()

#chiudi il file
lonfo.close()

#spostati nella cartella "backup"
os.chdir("backup")

#apertura del file in scrittura
lonfoCopy = open("lonfo1-backup.txt","w")

#scrittura sul file
lonfoCopy.write(contenuto)

#chiusura del file
lonfoCopy.close()

print("File \'lonfo1-backup.txt\' creato correttamente.")