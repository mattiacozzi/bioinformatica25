#Traccia:
#Crea una variabile intera e una float, scegli per esse un valore e stampa la stringa ``La somma di X e Y è Z'',

#creo le variabili
prima = 12
seconda = 4.23

#converto la prima in float per renderla compatibile con l'altra
prima = float(prima)

#calcolo la somma
somma = prima + seconda

#converto tutte le variabili in stringhe
prima = str(prima)
seconda = str(seconda)
somma = str(somma)

#stampo una stringa appropriata
print("La somma di " + prima + " e " + seconda + " vale " + somma)