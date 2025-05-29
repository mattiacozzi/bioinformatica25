#Traccia:
#Crea due istanze della classe ``Gatto'' con le seguenti caratteristiche: nome, padrone, colorePelo, peso, sesso. Crea poi il metodo ``litiga'' e scrivi un algoritmo che mostri a schermo che una istanza sta litigando con l'altra.

class Gatto:
    def __init__(self,nome,padrone,colorePelo,peso,sesso):
        self.nome = nome
        self.padrone = padrone
        self.colorePelo = colorePelo
        self.peso = peso
        self.sesso = sesso
    def litiga(self, x):
        print(self.nome + " litiga con " + x.nome + "!")

gatto1 = Gatto("Spooky","Mattia","calico",4.2, "F")
gatto2 = Gatto("Olivia","Betty","tigrato",4.8, "F")

gatto1.litiga(gatto2)