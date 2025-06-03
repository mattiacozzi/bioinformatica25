#Traccia:
#In un cinema esistono 5 tipi di biglietti diversi. I bambini sotto i 6 anni pagano 3€, tra i 7 e i 12 anni pagano 5€, i ragazzi tra 13 e 18 anni pagano 7€, gli adulti pagano 10€ e infine gli anziani sopra i 70 anni entrano gratis. Scrivi un algoritmo che chieda all'utente la sua età e che mostri poi il corrispondente prezzo del biglietto.

age = float(input("Quanti anni hai? "))

if age < 7:
    prezzo = 3
elif age < 13:
    prezzo = 5
elif age < 19:
    prezzo = 7
elif age < 71:
    prezzo = 10
else:
    prezzo = 0

string = f"Il tuo biglietto costa {prezzo} €."
print(string)