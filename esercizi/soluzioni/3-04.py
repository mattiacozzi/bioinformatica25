#Traccia:
#Scrivere un algoritmo che chieda all'utente di inserire il suo mese di nascita e il mese corrente e stabilisca poi, mostrandolo a schermo, se al mese corrente è più vicino il compleanno passato oppure il prossimo compleanno. Se i compleanni sono equidistanti, scegliere liberamente quale alternativa mostrare.


meseNascita = int(input("In che mese sei nato/a? (inserisci un numero) "))
meseCorrente = int(input("In che mese siamo ora? (inserisci un numero) "))

if meseNascita >= meseCorrente:
    distFut = meseNascita - meseCorrente
    distPast = 12 - distFut
else:
    distPast = meseCorrente - meseNascita
    distFut = 12 - distPast

if distPast < distFut:
    string = "Siamo più vicini al tuo compleanno passato ({} mesi) che al prossimo compleanno ({} mesi)."
    print(string.format(distPast, distFut))
else:
    string = "Siamo più vicini al tuo prossimo compleanno ({} mesi) che al compleanno passato ({} mesi)."
    print(string.format(distFut, distPast))

