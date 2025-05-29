def scomponi(a, b, c): #la funzione ha tre parametri
  scomp1 = "a(x - ({0:.2f}))^2"
  scomp2 = "a(x - ({0:.2f}))(x - ({1:.2f}))"
  delta = b*b - 4*a*c
  if (delta < 0):
    print("Il polinomio non si può scomporre.")
  elif (delta == 0):
    radice = (-b)/(2*a)
    print("Il polinomio si può scomporre come:")
    print(scomp1.format(radice))
  else:
    radice1 = (-b - delta) / (2*a)
    radice2 = (-b + delta) / (2*a)
    print("Il polinomio si può scomporre come:")
    print(scomp2.format(radice1, radice2))

print("Inserisci i coefficienti di un polinomio di II grado:")
primo = float(input("Primo coefficiente: "))
secondo = float(input("Secondo coefficiente: "))
terzo = float(input("Terzo coefficiente: "))

#invocazione della funzione con tre argomenti
scomponi(primo, secondo, terzo)