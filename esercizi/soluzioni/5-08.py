#Traccia:
#Definisci una classe relativa ad un prodotto cosmetico od un profumo e crea una istanza di quella classe.  Stampa a schermo le sue caratteristiche. Scrivi poi un algoritmo che chieda all'utente quale dato di questa istanza vuole modificare. Permetti all'utente di modificare il dato scelto e mostra poi le caratteristiche dell'istanza modificata.

def stampaCaratt(x):
    print("Ecco le caratteristiche attuali:")
    print("\nNome:              " + x.nome)
    print("Anno:              " + x.anno)
    print("Casa:              " + x.casa)
    print("Testa:             " + x.testa)
    print("Cuore:             " + x.cuore)
    print("Base:              " + x.base)
    print("Fragranza:         " + x.fragranza)
    print("Prezzo per 100 mL: " + x.prezzo100mL + "\n")

class Prodotto:
    def __init__(self,nome,anno,casa,testa,cuore,base,fragranza,prezzo100mL):
        self.nome = nome
        self.anno = anno
        self.casa = casa
        self.testa = testa
        self.cuore = cuore
        self.base = base
        self.fragranza = fragranza
        self.prezzo100mL = prezzo100mL

prodotto1 = Prodotto("Chanel No. 5",
                     "1921",
                     "Chanel",
                     "Aldeidi, agrumi (bergamotto, limone)",
                     "Gelsomino, rosa, ylang-ylang",
                     "Vetyver, vaniglia, sandalo, ambra",
                     "Floreale aldeidica",
                     "Variabile, ma generalmente elevato (es. circa 100-200 €)",
                    )

stampaCaratt(prodotto1)

choice = input("Quale dato vuoi modificare? ")
choice = choice.lower()
valore = input("Inserisci il nuovo valore: ")
if choice == "nome":
    prodotto1.nome = valore
elif choice == "anno":
    prodotto1.anno = valore
elif choice == "casa":
    prodotto1.casa = valore
elif choice == "testa":
    prodotto1.testa = valore
elif choice == "cuore":
    prodotto1.cuore = valore
elif choice == "base":
    prodotto1.base = valore
elif choice == "fragranza":
    prodotto1.fragranza = valore
elif choice == "prezzo100mL":
    prodotto1.prezzo100mL = valore
else:
    print("ERRORE: Scelta non valida.")
    
stampaCaratt(prodotto1)