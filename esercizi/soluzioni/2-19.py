#Traccia:
#Scrivere un algoritmo che chieda all'utente le masse di due corpi in kg, la loro distanza in metri e calcoli l'intensità della forza di attrazione gravitazionale tra di essi. Il risultato deve essere mostrato in notazione scientifica con tre decimali e deve essere presentato con chiarezza da una stringa appropriatamente costruita.

#La formula per l'attrazione gravitazionale tra due corpi è: F = G * (m_1 * m_2)/(r^2) con  G = 6.673E-11.

#chiedo i valori e converto in float
massa1 = float(input("Massa del primo corpo (in kg): "))
massa2 = float(input("Massa del secondo corpo (in kg): "))
dist = float(input("Distanza tra i corpi (in m): "))

#imposto il valore della costante di gravitazione universale
G = 6.673E-11

#calcolo l'intensità della forza
forza = (G * massa1 * massa2) / (pow(dist, 2))

#preparo la stringa con la formattazione corretta (vedi le opzioni complete di formattazione)
string = f"La forza di attrazione tra due corpi di massa {massa1} kg e {massa2} kg distanti {dist} m vale {forza:.3E} N."

#stampo la stringa
print(string)