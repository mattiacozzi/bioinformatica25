#Traccia:
#Crea la classe generale ``Animale'' con le seguenti caratteristiche: nomeScientifico, peso, specie. Crea poi la sottoclasse ``gattoDomestico'', che aggiunge come caratteristiche: nome, padrone, indirizzo. Crea poi un metodo specifico per questa classe, come ``X mangia i croccantini''. Crea infine la sottoclasse ``gattoSelvatico'', che aggiunge come caratteristiche: carattere, habitat e un metodo specifico a tua scelta.

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