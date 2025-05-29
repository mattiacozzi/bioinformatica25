#Traccia:
#Definisci una classe relativa ad un prodotto cosmetico od un profumo e crea almeno due istanze di quella classe.  Stampa a schermo le loro caratteristiche. Scrivi poi un algoritmo che chieda all'utente quale dato di quale istanza vuole modificare. Permetti all'utente di modificare il dato scelto nell'istanza corretta e mostra poi le caratteristiche dell'istanza modificata.

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

prodotto2 = Prodotto("Bleu de Chanel",
                     "2010",
                     "Chanel",
                     "Agrumi, Menta",
                     "Gelsomino, Noce Moscata",
                     "Sandalo, Ambra",
                     "Aromatico, Legnoso",
                     "Molto alto",
                    )   

lista = [prodotto1, prodotto2]

myProdNum = int(input("Quale dei due prodotti vuoi modificare? Digita 1 o 2: ")) - 1

myProd = lista[myProdNum]
stampaCaratt(myProd)

choice = input("Quale dato vuoi modificare? ")
choice = choice.lower()
valore = input("Inserisci il nuovo valore: ")
if choice == "nome":
    myProd.nome = valore
elif choice == "anno":
    myProd.anno = valore
elif choice == "casa":
    myProd.casa = valore
elif choice == "testa":
    myProd.testa = valore
elif choice == "cuore":
    myProd.cuore = valore
elif choice == "base":
    myProd.base = valore
elif choice == "fragranza":
    myProd.fragranza = valore
elif choice == "prezzo100mL":
    myProd.prezzo100mL = valore
else:
    print("ERRORE: Scelta non valida.")
    
stampaCaratt(myProd)