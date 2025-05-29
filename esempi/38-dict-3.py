disco1 = {
    "Artista":    "Ghost",
    "Titolo":     "Impera",
    "Rilascio":   2022,
    "Durata":     "46 min, 21 sec",
}
disco1["Titolo"] = "Skeleta"
disco1["Rilascio"] = 2025
disco1["Durata"] = "46 min, 43 sec"
print("Ecco le informazioni sul disco del " + str(disco1.get("Rilascio")) + " dei " + disco1.get("Artista") )
for x in disco1:
    print(x + ": \t" + str(disco1[x]))

