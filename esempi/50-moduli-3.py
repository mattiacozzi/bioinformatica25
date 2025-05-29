import mioModulo3 as calc

print("Benvenuto/a nella mia calcolatrice!\nChe operazione vuoi fare?")
print("s = somma\td = differenza\t\tp = prodotto")
print("q = quoziente\trq = radice quadrata\trc = radice cubica")
print("qu = quadrato\tc = cubo\t\tpot = potenza")
print("l = logaritmo\tln = log. naturale\te = esponenziale")
print("sin = seno\tcos = coseno\t\ttan = tangente")
choice = input()
if choice == "s": #somma
    num1 = float(input("Inserisci il primo termine:\t"))
    num2 = float(input("Inserisci il secondo termine:\t"))
    risultato = calc.somma(num1, num2)
    risposta = "{0:.2f} + {1:.2f} = {2:.2f}"
    print(risposta.format(num1, num2, risultato))
elif choice == "d": #differenza
    num1 = float(input("Inserisci il primo termine:\t"))
    num2 = float(input("Inserisci il secondo termine:\t"))
    risultato = calc.differenza(num1, num2)
    risposta = "{0:.2f} - {1:.2f} = {2:.2f}"
    print(risposta.format(num1, num2, risultato))
elif choice == "p": #prodotto
    num1 = float(input("Inserisci il primo fattore:\t"))
    num2 = float(input("Inserisci il secondo fattore:\t"))
    risultato = calc.prodotto(num1, num2)
    risposta = "{0:.2f} * {1:.2f} = {2:.2f}"
    print(risposta.format(num1, num2, risultato))
elif choice == "q":#divisione
    num1 = float(input("Inserisci il primo numero:\t"))
    num2 = float(input("Inserisci il secondo numero:\t"))
    risultato = calc.quoziente(num1, num2)
    risposta = "{0:.2f} / {1:.2f} = {2:.2f}"
    print(risposta.format(num1, num2, risultato))
elif choice == "rq": #radice quadrata
    num1 = float(input("Inserisci l'argomento:\t"))
    risultato = calc.radiceQuad(num1)
    risposta = "sqrt({0:.2f}) = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "rc": #radice cubica
    num1 = float(input("Inserisci l'argomento:\t"))
    risultato = calc.radiceCub(num1)
    risposta = "cbrt({0:.2f}) = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "qu": #quadrato
    num1 = float(input("Inserisci la base:\t"))
    risultato = calc.quadrato(num1)
    risposta = "{0:.2f}^2 = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "c": #cubo
    num1 = float(input("Inserisci la base:\t"))
    risultato = calc.cubo(num1)
    risposta = "({0:.2f}^3 = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "pot": #potenza
    num1 = float(input("Inserisci la base:\t"))
    num2 = float(input("Inserisci l'esponente:\t"))
    risultato = calc.pot(num1, num2)
    risposta = "{0:.2f}^{1:.2f} = {2:.2f}"
    print(risposta.format(num1, num2, risultato))
elif choice == "l": #logaritmo
    num1 = float(input("Inserisci la base:\t"))
    num2 = float(input("Inserisci l'argomento:\t"))
    risultato = calc.logaritmo(num1, num2)
    risposta = "log({0:.2f}, {1:.2f}) = {2:.2f}"
    print(risposta.format(num1, num2, risultato))
elif choice == "ln": #log nat
    num1 = float(input("Inserisci l'argomento:\t"))
    risultato = calc.logNat(num1)
    risposta = "ln({0:.2f}) = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "e": #exp
    num1 = float(input("Inserisci l'esponente:\t"))
    risultato = calc.expo(num1)
    risposta = "e^{0:.2f} = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "sin": #seno
    num1 = float(input("Inserisci l'argomento:\t"))
    risultato = calc.seno(num1)
    risposta = "sin({0:.2f}) = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "cos": #coseno
    num1 = float(input("Inserisci l'argomento:\t"))
    risultato = calc.coseno(num1)
    risposta = "cos({0:.2f}) = {1:.2f}"
    print(risposta.format(num1, risultato))
elif choice == "tan": #tangente
    num1 = float(input("Inserisci l'argomento:\t"))
    risultato = calc.tangente(num1)
    risposta = "tan({0:.2f}) = {1:.2f}"
    print(risposta.format(num1, risultato))
else:
    print("Errore, riprova!")