prezzo_iniziale = 45.99
sconto = 23
prezzo_finale = prezzo_iniziale * (1 - sconto/100)
stringa = "Il tuo prodotto costava {} euro.\nDopo aver applicato uno sconto del {}%,\nlo pagherai soltanto {:.2f} euro."
print(stringa.format(prezzo_iniziale, sconto, prezzo_finale))