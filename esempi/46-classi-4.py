class Persona:
  def __init__(self,nome,cognome,email):
    self.nome = nome
    self.cognome = cognome
    self.email = email
  def saluta(self):
    print("Ciao, io sono " + self.nome + " " + self.cognome)

class Studente(Persona): #Studente deriva da Persona
  def __init__(self,nome,cognome,email,matricola,media):
    #recupera gli attributi dalla classe madre
    super().__init__(nome,cognome,email)
    #nuovi attributi
    self.matricola = matricola
    self.media = media

class Docente(Persona):
  def __init__(self,nome,cognome,email,materia):
    super().__init__(nome,cognome,email)
    self.materia = materia

#creazione istanze
studente1 = Studente("Andrea","Bianchi","abianchi@mail.com",123456, 27)
docente1 = Docente("Silvia","Neri","sneri@email.com","Informatica")

studente1.saluta()
docente1.saluta()