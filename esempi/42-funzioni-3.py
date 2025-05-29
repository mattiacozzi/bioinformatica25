#definizione della funzione:
def calcolo_discriminante(a, b, c):
  d = b*b - 4*a*c
  return d  #la funzione "restituisce" il valore calcolato

primo = float(input("Primo coefficiente: "))
secondo = float(input("Secondo coefficiente: "))
terzo = float(input("Terzo coefficiente: "))
#delta assume il valore ritornato dalla funzione
delta = calcolo_discriminante(primo, secondo, terzo)
print("Il discriminante vale:")
print(delta)