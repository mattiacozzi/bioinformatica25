prezzo_iniziale = 45.99
sconto = 23
prezzo_finale = prezzo_iniziale * (1 - sconto/100)

stringa = f"Il tuo prodotto costava {prezzo_iniziale} euro.\nDopo aver applicato uno sconto del {sconto}%,\nlo pagherai soltanto {prezzo_finale:.2f} euro."

print(stringa)