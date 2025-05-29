#Traccia:
#Scrivi un algoritmo che crea una nuova cartella chiamata ``test''. Salva un file di testo a tuo piacere nella cartella appena creata.

import os

#controlla se esiste la cartella, altrimenti la crea
if os.path.exists("test"):
    print("La directory \'test\' esiste già, non è necessario crearla.")
else:
    os.mkdir("test")
    print("Directory \'test\' creata.")

#spostati nella cartella "test"
os.chdir("test")

#come esercizio precedente
filename = input("Inserisci un nome per il nuovo file (ometti l'estensione):\n")
fileExt = filename + ".txt"

#apertura del file in scrittura
myFile = open(fileExt, "w")

content = input("Inserisci il contenuto del nuovo file:\n")

#scrittura sul file
myFile.write(content)

#chiusura del file
myFile.close()

string = "File {} creato correttamente."
print(string.format(fileExt))