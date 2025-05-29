#definizione della funzione:
def spelling(nome = "Mario"):
  print("Il tuo nome è " + nome)
  print("Ecco lo spelling del tuo nome")
  for x in nome:
    print(x)

#invocazione con parametro di default
spelling()

#invocazione con parametro personalizzato:
utente = input("Ora dimmi come ti chiami: ")
spelling(utente)