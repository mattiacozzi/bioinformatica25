#creazione della classe Persona
class Persona:
    def __init__(self,nome,cognome,age,altezza,sesso):
        self.nome = nome
        self.cognome = cognome
        self.age = age
        self.altezza = altezza
        self.sesso = sesso

#creazione di una istanza
persona1 = Persona("Mattia","Cozzi",38, 177, "M")

#creazione della classe Gatto
class Gatto:
    def __init__(self,nome,padrone,colorePelo,peso,sesso):
        self.nome = nome
        self.padrone = padrone
        self.colorePelo = colorePelo
        self.peso = peso
        self.sesso = sesso

#creazione di una istanza
gatto1 = Gatto("Spooky","Mattia","calico",4.2, "F")

def coccola(a, b):
    string = "{} coccola {}."
    print(string.format(a, b))