#Traccia:
#Definisci e implementa una funzione che richieda una stringa all'utente e la mostri poi al contrario.

def ribalta(stringa):
    stringaInv = ""
    for x in range(len(stringa)):
        stringaInv = stringaInv + stringa[-(x+1)]
    return stringaInv
                
immissione = input("Inserisci una stringa di testo: ")

print("La stringa al contrario è: ")
print(ribalta(immissione))