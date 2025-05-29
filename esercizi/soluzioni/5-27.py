#Traccia:
#Scrivi un algoritmo che controlla se un certo file esiste.

import os

file1 = "lonfo1.txt"
file2 = "lonfo100.txt"

if os.path.exists(file1):
    print("Il file " + file1 + " esiste già.")
else:
    print("Il file " + file1 + " non esiste.")

if os.path.exists(file2):
    print("Il file " + file2 + " esiste già.")
else:
    print("Il file " + file2 + " non esiste.")