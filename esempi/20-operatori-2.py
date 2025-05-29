numero1 = 27
numero2 = 9
resto = numero1 % numero2
divisibile = not(resto)
stringa = "{} è divisibile per {}? {}"
print(stringa.format(numero1, numero2, divisibile))