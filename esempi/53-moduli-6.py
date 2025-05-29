import random

dadi = {"4","6","8","10","12","20","100"}

choice = 1
while choice != 0:
    print("Che dado vuoi lanciare?\t4\t6\t8\t10\t12\t20\t100\nDigita 0 per uscire")
    choice = input()
    if choice in dadi:
        choice = int(choice)
        string1 = "Hai scelto di lanciare un dado da {}"
        print(string1.format(choice))
        lancio = random.randrange(0, choice) + 1
        string2 = "\nHai tirato un {}!\n"
        print(string2.format(lancio))
    elif choice == "0":
        break
    else:
        print("\nValore non valido. Riprova.\n")
        choice = 1

print("\nAlla prossima!")