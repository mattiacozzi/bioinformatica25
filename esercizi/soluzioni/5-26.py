#Traccia:
#Scrivi un algoritmo che permetta di creare un file di testo con un nome definito dall'utente. Scrivi successivamente la stringa ``I <3 Python'' nel file appena creato.

filename = input("Inserisci un nome per il nuovo file (ometti l'estensione):\n")

#aggiunta dell'estensione
fileExt = filename + ".txt"

#apertura del file in scrittura
myFile = open(fileExt, "w")

#scrittura sul file
myFile.write("I <3 Python")

#chiusura del file
myFile.close()

string = f"File {fileExt} creato correttamente."
print(string)