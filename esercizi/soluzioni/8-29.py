#Traccia:
#Scrivi un algoritmo che chieda all’utente se vuole convertire il file “best-actor-age-updated.csv” in formato XLSX o lasciarlo in CSV. Chiedi poi se vuole salvare solo i dati relativi alle donne, agli uomini o a entrambi. Salva poi il file così come l’utente ha richiesto.
import pandas as pd

attori = pd.read_csv("best-actor-age-updated.csv")

#creo una funzione che riceve la scelta dell'utente rispetto al formato
#successivamente fa scegliere il subset di dati e li salva in formato corretto
def restringiDataFrame(choice):
    gender = ""
    #continua il ciclo finché l'utente non inserisce un valore consentito
    while ((gender != "W") and (gender != "M") and (gender != "B")):
        gender = input("Vuoi salvare i dati relativi a donne, uomini o entrambi?\nW = donne\tM = uomini\tB = entrambi\n")
        if gender == "W":
            myDS = attori[attori.Gender == "Female"]
        elif gender == "M":
            myDS = attori[attori.Gender == "Male"]
        elif gender == "B":
            myDS = attori
        else:
            print("Comando errato, riprova.\n")
    #salva in base al formato scelto
    if (choice == "C"):
        myDS.to_excel("best-actor-updated-restricted.xlsx")
    elif (choice == "L"):
        myDS.to_csv("best-actor-updated-restricted.csv")

#variabile per salvare la scelta sul formato
scelta = ""

#ciclo da eseguire finché l'utente non inserisce una risposta accettabile
while ((scelta != "C") and (scelta != "L")):
    scelta = input("Cosa vuoi fare con il file?\nC = converti in XLSX\tL = lascia il file in CSV\n")
    if scelta == "C" or scelta == "L":
        restringiDataFrame(scelta)
    else:
        print("Comando errato, riprova.\n")

print("Finito.")