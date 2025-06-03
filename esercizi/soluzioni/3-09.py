#Traccia:
#Creare un algoritmo che chieda all'utente di inserire i tre coefficienti di una disequazione di secondo grado in forma canonica e che, se possibile, risolva la disequazione.


import math

#welcome
print("Questo è un risolutore di disequazioni di secondo grado!")
print("Assicurati di aver trasformato la disequazione in forma canonica e di aver cambiato i segni in modo da avere \'>0\'.")

#input dei coefficienti e conversione in float
a = float(input("Inserisci il primo coefficiente: "))
b = float(input("Inserisci il secondo coefficiente: "))
c = float(input("Inserisci il terzo coefficiente: "))

#calcolo del delta
delta = b*b - 4*a*c

#fai una tabella con i casi possibili per capire meglio le seguenti righe di codice.
#una tabella sulle disequazioni di secondo grado è disponibile su:
#https://s3.eu-central-1.wasabisys.com/evulpo-drive-mirror/it_IT/summary_assets/summary_asset_1668460780.svg

if (delta < 0) and (a > 0):
    print("La disequazione è verificata per ogni x appartenente a R.")
elif (delta <= 0) and (a < 0):
    print("La disequazione è impossibile.")
else:
    if (delta == 0):
        x = (-b)/(2*a)
        string = f"La disequazione ha come soluzione: x ≠ {x}"
        print(string.format(x))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        #distinguere tra il valore più piccolo e il più grande tra x1 e x2
        piccolo = min(x1, x2)
        grande = max(x1, x2)
        if (a > 0):
            string = f"La disequazione come soluzione: x < {piccolo} v x > {grande}"
            print(string)
        else:
            string = f"La disequazione come soluzione: {piccolo} < x < {grande}"
            print(string)