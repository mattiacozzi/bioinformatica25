#gestire date con il modulo datetime
# https://www.youtube.com/watch?v=Q3VMnNw1pHw&list=PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF&index=32

#per lavorare con le date, importiamo il seguente modulo
import datetime

#ora attuale
x = datetime.datetime.now()
print("Ora sono le:")
print(x)

#data specifica
y = datetime.datetime(2025, 10, 31)
print("Il prossimo Halloween sarà il:")
print(y)

#data formattata
#documentazione: https://www.w3schools.com/python/python_datetime.asp
print("Un formato personalizzato per l'ora attuale:")
print(x.strftime("%A, %d %B %Y"))

