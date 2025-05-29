class Persona:
  def __init__(self,nome,cognome): #richiede i parametri
    self.nome = nome               #"self" deve sempre
    self.cognome = cognome         #essere riportato!

#creazione istanza con valori personalizzati
persona1 = Persona("Andrea","Bianchi")
persona2 = Persona("Napoleone","Bonaparte")
print(persona1.nome)
print(persona1.cognome)
print(persona2.nome)
print(persona2.cognome)