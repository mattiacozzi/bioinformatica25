#Traccia:
#Crea due insiemi, con eventualmente elementi in comune. Stampa prima gli insiemi e poi la loro unione.


fiori1 = {
    "Rosa",
    "Girasole",
    "Viola",
    "Orchidea"
}

fiori2 = {
    "Viola",
    "Orchidea",
    "Tulipano",
    "Giglio"
}

#stampo il primo insieme
print("Ecco il primo insieme: ")
for x in fiori1:
    print(x)

#stampo il secondo insieme
print("\nEcco il secondo insieme: ")
for x in fiori2:
    print(x)

# aggiungo al primo gli elementi del secondo
fiori1.update(fiori2)

#stampo l'unione
print("\nEcco la loro unione: ")
for x in fiori1:
    print(x)

# oppure:
# fioriTot = fiori1.union(fiori2)

# print("\nEcco la loro unione: ")
# for x in fioriTot:
#     print(x)