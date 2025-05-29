#Traccia:
#Scrivere un algoritmo che chieda all'utente di inserire una stringa, una lettera e un numero e che sostituisca poi nella stringa tutte le occorrenze della lettera con il numero.

stringa = input("Inserisci una stringa: ")
lettera = input("Inserisci una lettera: ")
numero = input("Inserisci un numero intero: ")

print(stringa.replace(lettera, numero))