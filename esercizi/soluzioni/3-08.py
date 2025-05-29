#Traccia:
#Come l'esercizio precedente, ma controllando se il nome inizia e termina per vocale.

nome = input("Come ti chiami? ")

#una condizione complessa con degli "oppure"
#(vedremo più avanti un modo migliore per scrivere questa condizione)
if (nome[-1] == "A" or nome[-1] == "a" or nome[-1] == "E" or nome[-1] == "e" or nome[-1] == "I" or nome[-1] == "i" or nome[-1] == "O" or nome[-1] == "o" or nome[-1] == "U" or nome[-1] == "u"):
    print("Il tuo nome termina per vocale.")
else:
    print("Il tuo nome termina per consonante.")