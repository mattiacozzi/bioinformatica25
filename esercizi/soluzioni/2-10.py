#Traccia:
#Contare tutte le volte che la lettera "a" compare nei testi dei due esercizi precedenti.

dante = "
Buongiorno, mi chiamo Dante Alighieri e di professione sono scrittore.
Sono nato a Firenze nel 1265.
"

catullo = "
[Testo originale]
Vivamus, mea Lesbia, atque amemus,
rumoresque senum severiorum
omnes unius aestimemus assis.
Soles occidere et redire possunt;
nobis cum semel occidit brevis lux,
nox est perpetua una dormienda.
Da mi basia mille, deinde centum,
dein mille altera, dein secunda centum,
deinde usque altera mille, deinde centum;
dein, cum milia multa fecerīmus,
conturbabimus illa, ne sciamus,
aut ne quis malus invidere possit,
cum tantum sciat esse basiorum.

[Traduzione]
Viviamo, o mia Lesbia, e amiamoci,
e le dicerie dei vecchi severi
consideriamole tutte di valore pari a un soldo.
I giorni possono tramontare e risorgere;
noi, quando una buona volta finirà questa breve vita,
dobbiamo dormire un'unica notte eterna.
Dammi mille baci, poi cento,
poi ancora mille, poi di nuovo cento,
poi senza smettere altri mille, poi cento;
poi, quando ce ne saremo dati molte migliaia,
li mescoleremo, per non sapere (il loro numero)
e perché nessun malvagio ci possa guardare male,
sapendo che qui ci sono tanti baci.
"

string = "Nella {} stringa la lettera a compare {} volte."
print(string.format("prima",dante.count("a")))
print(string.format("seconda",catullo.count("a")))
