nome = input("Come ti chiami? ")
lungh = len(nome)
i = 1
print("Ecco il tuo nome al contrario:")
while i<lungh+1:
    print(nome[-i])
    i += 1
