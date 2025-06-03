#Traccia:
#Scrivi un algoritmo che richieda all'utente di inserire alcuni suoi dati: nome, cognome, compleanno, ecc. Salva le risposte dell'utente in un file di testo che viene creato all'esecuzione dell'algoritmo.

#recupero dei dati
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
compleanno = input("Inserisci il tuo compleanno: ")
residenza = input("Inserisci la città in cui abiti: ")

#apertura del file in modalità scrittura
myFile = open("userInfo.txt","w")

#stringa multilinea per le info
data = f"""Nome: {nome}
Cognome: {cognome}
Compleanno: {compleanno}
Residenza: {residenza}
"""

#scrittura della stringa nel file
myFile.write(data)

#chiusura del file
myFile.close()

print("Informazioni salvate.")