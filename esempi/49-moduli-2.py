import mioModulo2 as my

#questo code è QUASI identico a quello dell'esempio 39 sui dizionari
print("Ecco le tracce presenti sul disco del " + str(my.disco1.get("Rilascio")) + " dei " + my.disco1.get("Artista"))
for x in range(len(my.disco1["Tracce"])):
    print(str(x+1) + ". " + my.disco1["Tracce"][x+1])
print("Durata totale: " + my.disco1.get("Durata"))