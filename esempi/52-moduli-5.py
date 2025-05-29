import random

print("Un numero casuale tra 0 e 1")
x = random.random()
print(x)


print("Un numero casuale tra 0 e 10")
y = 10*random.random()
print(y)


print("Un numero casuale tra 2 e 10")
z = random.randrange(2, 10)
print(z)


print("Un multiplo di 3 casuale minore di 100")
w = random.randrange(0, 100, 3) #minimo, massimo, passo
print(w)



