#Traccia:
#Definisci una classe relativa ad un prodotto cosmetico od un profumo e crea almeno due istanze di quella classe. Stampa poi a schermo tutte le caratteristiche degli oggetti che hai creato.

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

prodotti = [prodotto1, prodotto2]

for x in prodotti:
    print("\nNome:              " + x.nome)
    print("Anno:              " + x.anno)
    print("Casa:              " + x.casa)
    print("Testa:             " + x.testa)
    print("Cuore:             " + x.cuore)
    print("Base:              " + x.base)
    print("Fragranza:         " + x.fragranza)
    print("Prezzo per 100 mL: " + x.prezzo100mL)