#Traccia:
#Usando le classi dell'esercizio precedente, genera delle istanze delle due sottoclassi e fai compiere a queste istanze delle azioni usando i loro metodi specifici.

class Animale:
    def __init__(self,nomeScient,peso,specie):
        self.nomeScient = nomeScient
        self.peso = peso
        self.specie = specie

class gattoDomestico(Animale):
    def __init__(self,nomeScient,peso,specie,nome,padrone,indirizzo):
        #recupera gli attributi dalla classe madre
        super().__init__(nomeScient,peso,specie)
        self.nome = nome
        self.padrone = padrone
        self.indirizzo = indirizzo
    def mangia(self):
        print(self.nome + " mangia i croccantini.")

class gattoSelvatico(Animale):
    def __init__(self,nomeScient,peso,specie,carattere,habitat):
        #recupera gli attributi dalla classe madre
        super().__init__(nomeScient,peso,specie)
        self.carattere = carattere
        self.habitat = habitat
    def caccia(self):
        print(self.nomeScient + " va a caccia.")

gatto1 = gattoDomestico("Felix catus",4.5, "Gatto domestico","Spooky","Mattia","via Dante 89, Milano")
lince1 = gattoSelvatico("Lynx pardinus",32, "Lince pardina","burbero","macchia della penisola iberica")

gatto1.mangia()
lince1.caccia()