from random import randint

miklas = { "Panest var, izskaitīt nevar" : "mati",
            "Četras kājas, viena cepure" : "galds",
            "Citam kalpo, pats sevi tērē" : "svece",
            "Siers jūras dibenā":"saule",
            "Brīžam jauns, brīžam vecs":"mēness",
            "Naktī dzimst, dienā mirst":"rasa",
            "Viena kāja, desmit rokas":"koks",
            "Raiba gotiņa, zelta radziņi":"bite", }

miklas1 = list(miklas.keys())
atbildes=0

print("Apraksts")
#sakums = input("Esi gatvs minēt? (ievadiet jā vai nē):")
#if sakums == "jā":
#print(sakums)

while len(miklas1) > 0:
    gadijums = randint(0,len(miklas1)-1)
    minejums = input(f"{miklas1[gadijums]}. Kas tas ir?: ")
    miklas1.pop(gadijums)
    if minejums.lower() == "nezinu" or minejums.lower() == "beigt":
        break
    elif minejums.lower() == miklas[miklas1[gadijums]]:
        print("Pareizi")
        atbildes += 1
    else:
        print("nepareizi")














if atbildes <= 3:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Nebēdājies un mēģini vēlreiz!😉")
elif atbildes <= 7:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Tev labi padodas minēt mīklas, tā turpināt!😁")
else:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Tu si īsts mīklu minētājs😎")
