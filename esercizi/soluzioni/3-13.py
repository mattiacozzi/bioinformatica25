#Traccia:
#Scrivere un algoritmo che che chieda all'utente di quale numero voglia calcolare il quadrato, legga l'input dell'utente e ne mostri il quadrato. Successivamente, chiedere se si vuole calcolare un altro quadrato. Se l'utente risponde Y, allora chiedere un altro valore e ripetere il calcolo. Se l'utente risponde N, uscire dall'algoritmo.

risp = "Y"

while (risp == "Y"): #fino a che risp vale Y, esegui:
    x = int(input("Inserisci il numero di cui vuoi scoprire il quadrato: "))
    quad = x*x
    string = f"Il quadrato di {x} è {quad}."
    print(string)

    while (risp != "N"):
        risp = input("Vuoi calcolare un altro quadrato? Y/N: ")
        if (risp == "Y"):
            break #se l'utente inserisce Y, esci da questo ciclo
        elif (risp != "N"): #se l'utente inserisce una lettera scorretta, stampa un errore e vai al prossimo ciclo
            print("Errore. Inserisci una lettera corretta.")
            continue

print("Alla prossima.")