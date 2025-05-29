alberi = ["Quercia","Pino","Faggio","Ontano","Castagno","Acero","Ciliegio","Salice","Betulla","Magnolia"]
stringa = "{}. {}"
print("Ecco gli elementi della tua lista numerati:")
for x in range(len(alberi)):
    print(stringa.format(x+1, alberi[x]))

print("Ecco adesso gli ultimi tre elementi della lista:")
for y in range(3):
    print(stringa.format(len(alberi)-y, alberi[-1-y]))