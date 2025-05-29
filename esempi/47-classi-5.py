class Persona:
  def __init__(self,nome,cognome,email):
    self.nome = nome
    self.cognome = cognome
    self.email = email

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

choice = input("Che tipo di utente vuoi creare?\np = persona\ts = studente\td=docente\n")
if (choice != "p") and (choice != "s") and (choice != "d"):
  print("Errore!")
else:
  nome = input("Inserisci nome:\n")
  cognome = input("Inserisci cognome:\n")
  email = input("Inserisci email:\n")
  if (choice == "s"):
    matricola = input("Inserisci matricola:\n")
    media = input("Inserisci media:\n")
    studente1 = Studente(nome,cognome,email,matricola,media)
    print("Utente creato con successo!")
    print(studente1.nome + " " + studente1.cognome + "\nContatto: " + studente1.email)
    print("Matricola: " + studente1.matricola + "\nMedia: " + studente1.media)
  elif (choice == "d"):
    materia = input("Inserisci materia:\n")
    docente1 = Docente(nome,cognome,email,materia)
    print("Utente creato con successo!")
    print(docente1.nome + " " + docente1.cognome + "\nContatto: " + docente1.email)
    print("Materia: " + docente1.materia)
  else:
    persona1 = Persona(nome,cognome,email)
    print("Utente creato con successo!")
    print(persona1.nome + " " + persona1.cognome + "\nContatto: " + persona1.email)

