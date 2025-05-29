class Persona:
  def __init__(self,nome,cognome,annoN,meseN,giornoN):
    self.nome = nome
    self.cognome = cognome
    self.annoN = annoN
    self.meseN = meseN
    self.giornoN = giornoN
  def saluta(self):
    print("Ciao, io sono " + self.nome + " " + self.cognome)

#creazione istanza
persona1 = Persona("Andrea","Bianchi",2001, 11, 24)
persona1.saluta()
#cambiamento valore di un attributo
persona1.nome = "Filippo"
persona1.saluta()
#eliminazione di un attributo
del persona1.giornoN