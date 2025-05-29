#Traccia:
#Scrivere un algoritmo che chieda all'utente di inserire il suo nome e che controlli, mostrandolo a schermo, se il nome inizia per vocale.

nome = input("Come ti chiami? ")

#una condizione complessa con degli "oppure"
#(vedremo più avanti un modo migliore per scrivere questa condizione)
if (nome[0] == "A" or nome[0] == "a" or nome[0] == "E" or nome[0] == "e" or nome[0] == "I" or nome[0] == "i" or nome[0] == "O" or nome[0] == "o" or nome[0] == "U" or nome[0] == "u"):
    print("Il tuo nome inizia per vocale.")
else:
    print("Il tuo nome inizia per consonante.")