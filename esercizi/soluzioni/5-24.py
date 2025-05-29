#Traccia:
#Crea un file di testo con un contenuto a piacere e scrivi un algoritmo che aggiunga una nuova linea di testo a tale file.

#apertura del file
myFile = open("lonfo2.txt","a")

#aggiunta delle nuove linee
myFile.write("\ne molto raramente barigatta,")
myFile.write("\nma quando soffia il bego a bisce bisce")
myFile.write("\nsdilenca un poco e gnagio s’archipatta.")

#chiusura del file in modalità append
myFile.close()

#apertura del file in modalità read
myFile = open("lonfo2.txt","r")

#stampa del contenuto
print(myFile.read())

#chiusura del file
myFile.close()