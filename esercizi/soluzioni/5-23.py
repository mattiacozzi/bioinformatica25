#Traccia:
#Crea un file di testo con un contenuto a piacere (puoi copiarlo da https://it.lipsum.com/feed/html e scrivi un algoritmo che ne mostri a schermo il contenuto.

#apro il file
myFile = open("lonfo1.txt","r")

#stampo il contenuto
print(myFile.read())

#chiudo il file
myFile.close()