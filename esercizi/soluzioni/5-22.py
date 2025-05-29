#Traccia:
#Installa il pacchetto "camelcase" tramite pip. Importalo in un algoritmo che richieda all'utente una stringa e usi poi il metodo CamelCase() (presente nel nuovo pacchetto) per mostrare all'utente la stringa che ha inserito convertita in camelcase.

import camelcase

string = input("Inserisci una stringa di testo: ")

x = camelcase.CamelCase()

x = x.hump(string)

print("Ecco la stringa convertita in CamelCase:")
print(x)