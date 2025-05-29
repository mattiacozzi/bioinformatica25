class Persona:
  def __init__(self,nome,cognome):
    self.nome = nome
    self.cognome = cognome
  #creazione di un metodo che usa i suoi stessi parametri
  def saluta(self):
    print("Ciao, io sono " + self.nome + " " + self.cognome)
  #creazione di un metodo che ne usa anche altri:
  def occhiolino(self, x):
    print(self.nome + " fa l'occhiolino a " + x.nome + " " + x.cognome)
persona1 = Persona("Andrea","Bianchi")
persona2 = Persona("Napoleone","Bonaparte")
persona1.saluta()
persona1.occhiolino(persona2)