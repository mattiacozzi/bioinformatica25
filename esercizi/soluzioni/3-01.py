#Traccia:
#Creare un algoritmo che chiede all'utente di inserire un numero e, se quel numero è multiplo di 3, mostra tale informazione a schermo.

numero = int(input("Inserisci un numero: "))

if (numero % 3 == 0):
    print("Il numero che hai inserito è un multiplo di 3.")
else:
    print("Il numero che hai inserito non è un multiplo di 3.")