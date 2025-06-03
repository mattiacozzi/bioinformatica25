#Traccia:
#Scrivere un algoritmo che contenga la ricetta per una torta per quattro persone. L'algoritmo deve poi chiedere all'utente per quante persone deve calcolare gli ingredienti della torta e deve poi mostrare a schermo gli ingredienti da utilizzare.

#parametri della torta
torta = "di mele"
persone = 4

#ingredienti e quantità
mele = 700
farina = 250
latte = 150
limoni = 1
cannella = 0.5
zucchero = 200
burro = 100
uova = 2
lievito = 16
sale = 1

#preparo le stringhe
intro = "Ecco gli ingredienti per una torta {} per {} persone:"
ricetta = """mele      {0} grammi
farina    {1} grammi
latte     {2} mL
limoni    {3}
cannella  {4} cucch.
zucchero  {5} grammi
burro     {6} grammi
uova      {7}
lievito   {8} grammi
sale      {9} pizzichi"""

#stampo le stringhe
print(intro.format(torta, persone))
print(ricetta.format(mele, farina, latte, limoni, cannella, zucchero, burro, uova, lievito, sale))

#chiedo un nuovo valore per il numero di persone e converto in intero
persone = int(input("Per quante persone stai preparando la torta? "))

#stampo le stringhe aggiornate
print(intro.format(torta, persone))

#calcolo direttamente qui le nuove quantità
print(ricetta.format(mele*persone/4, farina*persone/4, latte*persone/4, limoni*persone/4, cannella*persone/4, zucchero*persone/4, burro*persone/4, uova*persone/4, lievito*persone/4, sale*persone/4))