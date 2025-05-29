alberi1 = {"Quercia","Pino","Faggio","Ontano","Castagno"}
print(alberi1)
alberi2 = {"Ontano","Castagno","Acero","Ciliegio"}
print(alberi2)
alberiIntersection = alberi1.intersection(alberi2)
if (alberiIntersection): #un insieme non vuoto viene valutato come "True"
    print("I due elementi hanno alcuni elementi in comune, ovvero:")
    for x in alberiIntersection:
        print(x)
else: 
    print("I due insiemi non hanno nessun elemento comune")

#prova ad eliminare gli elementi in comune e vedere come cambia l'output