#Traccia:
#Richiedi all'utente due angoli in gradi, convertili in radianti e mostra a schermo: il seno del primo angolo, il seno del secondo angolo, la somma dei due seni e il seno della somma.

import math

def converti(a):
    risultato = a * math.pi / 180
    string = f"L'angolo {a:.3f} in radianti vale {risultato:.3f}.\n"
    print(string)
    return risultato

primo = float(input("Inserisci un angolo in gradi da convertire in radianti: "))
primo = converti(primo)

secondo = float(input("Inserisci un altro angolo in gradi da convertire in radianti: "))
secondo= converti(secondo)

stringSeno = "Il seno di {:.3f} vale {:.3f}.\n"
print(stringSeno.format(primo, math.sin(primo)))
print(stringSeno.format(secondo, math.sin(secondo)))

stringSommaSeni = "La somma dei seni di {:.3f} e {:.3f} vale {:.3f}.\n"
print(stringSommaSeni.format(primo, secondo, math.sin(primo) + math.sin(secondo)))

stringSenoSomma = "Il seno della somma di {:.3f} e {:.3f} vale {:.3f}.\n"
print(stringSenoSomma.format(primo, secondo, math.sin(primo)*math.cos(secondo) + math.sin(secondo)*math.cos(primo)))