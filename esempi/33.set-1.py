alberi = {"Quercia","Pino","Faggio","Ontano","Castagno","Acero","Ciliegio","Salice","Betulla","Magnolia"}
print("Insieme di partenza")
for x in alberi:
    print(x)
alberi.add("Palma")
alberi.discard("Castagno")
print("Insieme modificato")
for x in alberi:
    print(x)