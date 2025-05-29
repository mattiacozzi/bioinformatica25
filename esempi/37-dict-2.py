disco1 = {
    "Artista":    "Ghost",
    "Titolo":     "Impera",
    "Rilascio":   2022,
    "Durata":     "46 min, 21 sec",
}
print("Ecco le informazioni sul disco del " + str(disco1.get("Rilascio")) + " dei " + disco1.get("Artista") )
for x in disco1:
    print(x + ": \t" + str(disco1[x]))