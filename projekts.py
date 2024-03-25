from random import randint

miklas = { "Panest var, izskaitīt nevar" : "mati",
            "Četras kājas, viena cepure" : "galds",
            "Citam kalpo, pats sevi tērē" : "svece",
            "Siers jūras dibenā":"saule",
            "Brīžam jauns, brīžam vecs":"mēness",
            "Naktī dzimst, dienā mirst":"rasa",
            "Viena kāja, desmit rokas":"koks",
            "Raiba gotiņa, zelta radziņi":"bite",
            "Sešas lapas no sudraba, septītā – zelta": "nedēļa",
            "Otram rāda pats neredz": "brilles"}

miklas1 = list(miklas.keys())
miklas2 = list(miklas.values())
atbildes=0

print('Sveicināts! Vēlies pārbaudīt savas spējas mīklu atminēšanā? Tad esi laipni aicināts spēlē "Mīklas🧶"')
print('Spēles noteikumi ir vienkārši. Pavisam ir 10 mīklas. Katru tev ir iespēja minēt 3 reizes.')
print('Ja vēlies spēli beigt, atbildes vietā uzraksti "beigt". Mēs tev obligāti paziņosim cik mīklas tu atminēji😉')

while len(miklas1) > 0:
    gadijums = randint(0,len(miklas1)-1)
    minejums = input(f"{miklas1[gadijums]}. Kas tas ir?: ")
    
    if minejums.lower() == "nezinu" or minejums.lower() == "beigt":
        break
    elif minejums.lower() == miklas[miklas1[gadijums]]:
        len(miklas1.pop(gadijums)) 
        print("Pareizi🎉")
        atbildes += 1
    else:
        print("Mēģini vēlreiz!")
        nepareizi = 1
        while nepareizi < 3:
            input(f"{miklas1[gadijums]}. Kas tas ir?: ")
            if minejums.lower() == "nezinu" or minejums.lower() == "beigt":
                break
            elif minejums.lower() == miklas[miklas1[gadijums]]:
                len(miklas1.pop(gadijums)) 
                print("Pareizi🎉")
                atbildes += 1
                break
            else:
                nepareizi += 1
        if nepareizi == 3:
            print(f"Diemžēl mīklu {[miklas1[gadijums]]} tu neatminēji😔.")
            len(miklas1.pop(gadijums))  

if atbildes <= 4:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Nebēdājies un mēģini vēlreiz!😉")
elif atbildes <= 8:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Tev labi padodas minēt mīklas, tā turpināt!😁")
else:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Tu esi īsts mīklu minētājs😎")
