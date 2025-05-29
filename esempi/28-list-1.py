alberi = ["Quercia","Pino","Faggio","Ontano","Castagno","Acero","Ciliegio","Salice","Betulla","Magnolia"]
string = "La tua lista è formata da {} elementi"
print(string.format(len(alberi)))
print("Ecco gli elementi della tua lista:")
for x in alberi:
    print(x)