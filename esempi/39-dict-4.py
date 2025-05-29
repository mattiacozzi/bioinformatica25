disco1 = {
    "Artista":    "Ghost",
    "Titolo":     "Impera",
    "Rilascio":   2022,
    "Durata":     "46 min, 21 sec",
    "Tracce": {
        1:  "Imperium",
        2:  "Kaisarion",
        3:  "Spillways",
        4:  "Call Me Little Sunshine",
        5:  "Hunter's Moon",
        6:  "Watcher in the Sky",
        7:  "Dominion",
        8:  "Twenties",
        9:  "Darkness at the Heart of My Love",
        10: "Griftwood",
        11: "Bite of Passage",
        12: "Respite on the Spitalfields",
    } 
}
print("Ecco le tracce presenti sul disco del " + str(disco1.get("Rilascio")) + " dei " + disco1.get("Artista"))
for x in range(len(disco1["Tracce"])):
    print(str(x+1) + ". " + disco1["Tracce"][x+1])
print("Durata totale: " + disco1.get("Durata"))
