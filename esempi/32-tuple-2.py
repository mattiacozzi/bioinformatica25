alberi = ("Quercia",
          "Pino",
          "Faggio",
          "Ontano",
          "Acero")

print("La tupla PRIMA della modifica;")

for x in alberi:
    print(x)

alberi2 = list(alberi)

alberi2[3] = "Palma"

alberi = tuple(alberi2)

print("La tupla DOPO la modifica:")
for x in alberi:
    print(x)

#codice alternativo, per mostrare le tuple fianco a fianco
# alberi = ("Quercia","Pino","Faggio","Ontano","Acero")
# alberi2 = list(alberi)
# alberi2[3] = "Palma"
# alberi3 = tuple(alberi2)
# string = "{}\t\t{}"
# for x in range(len(alberi)):
#     print(string.format(alberi[x],alberi3[x]))