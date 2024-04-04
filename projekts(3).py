from random import randint
import datetime


miklas = { "Panest var, izskaitīt nevar" : "mati",            #Vārdnīca, kur atslēgas ir mīklas, bet vērtības ir šo mīklu atminējumi
            "Četras kājas, viena cepure" : "galds",
            "Citam kalpo, pats sevi tērē" : "svece",
            "Siers jūras dibenā":"saule",
            "Brīžam jauns, brīžam vecs":"mēness",
            "Naktī dzimst, dienā mirst":"rasa",
            "Viena kāja, desmit rokas":"koks",
            "Raiba gotiņa, zelta radziņi":"bite",
            "Sešas lapas no sudraba, septītā – zelta": "nedēļa",
            "Otram rāda pats neredz": "brilles"}

x = datetime.datetime.now()
miklas1 = list(miklas.keys()) #Pārliek vārdnīcas atslēgas(mīklas) sarakstā
atbildes=0 

print('\033[1;34;40m Sveicināts! Vēlies pārbaudīt savas spējas mīklu atminēšanā? Tad esi laipni aicināts spēlē \033[1;37;40m"Mīklas✨"')
print('\033[1;34;40m Spēles noteikumi ir vienkārši. Pavisam ir 10 mīklas. Katru tev ir iespēja minēt 3 reizes.')
print('Ja vēlies spēli beigt, atbildes vietā uzraksti \033[1;37;40m "beigt". \033[1;34;40m Mēs tev obligāti paziņosim cik mīklas tu atminēji😉')
print(f"Tu sāci minēt mīklas kad bija {(x)}")

while len(miklas1) > 0:  #Cikls darbosies kamēr mīklas nebeigsies
    gadijums = randint(0,len(miklas1)-1) #Randomā izvelk mīklu no saraksta 1 elementa līdz pēdējam
    minejums = input(f"\033[1;33;40m{miklas1[gadijums]}. Kas tas ir?:") #Lietotāja atbilde uz mīklu
    if minejums.lower() == "beigt": #Apturēs ciklu, ja lietotājs vairs negribēs spēlēt un ievadīs "beigt"
        break
    elif minejums.lower() == miklas[miklas1[gadijums]]: #Pārbauda, vai lietotāja minējums sakrīt ar vārdnīcas vērtībām(mīklu atminējumiem)
        len(miklas1.pop(gadijums)) #Izņem no saraksta tiko atminēto mīklu
        print("\033[1;32;40m Pareizi🎉")
        atbildes += 1 #Palielina lietotāja pareizo atminēto mīklu skaitu par 1
    else: #Ja minējums tomēr nebija pareizs...
        print("\033[1;31;40m Mēģini vēlreiz!")
        nepareizi = 1  #Šajā brīdī nepareizo atbilžu skaits ir 1
        while nepareizi == 1 or nepareizi <= 3: #Palaižas cikls, kurš darbosies kamēr neparreizo minējumu skait būs 1; mazāks vai vienāds ar 3.
            if nepareizi == 3: #Pārbauda vai nepareizo minējumu skaits ir vienāds ar 3
                print(f"\033[1;31;40m Diemžēl mīklu {[miklas1[gadijums]]} tu neatminēji😔.")
                len(miklas1.pop(gadijums)) #Izņem no saraksta tiko atminēto mīklu
                nepareizi = 0 #Nepareizo minējumu skaits ir 0. Ja lietotājs atkal kļūdīsies cikls atkal varēs normāli darboties
                break
            else: #Ja nepareizo minējumu skaits joprojām nav 3...
                minejums = input(f"\033[1;33;40m{miklas1[gadijums]}. Kas tas ir?: ") #Dod minēt to pašu mīklu, kuru tiko neatminēja
                if minejums.lower() == "beigt": 
                    len(miklas1.pop(gadijums))
                    nepareizi = 0 
                    break
                elif minejums.lower() == miklas[miklas1[gadijums]]:
                    len(miklas1.pop(gadijums)) 
                    print("\033[1;32;40m Pareizi🎉")
                    atbildes += 1
                    nepareizi = 0
                    break
                else:
                    nepareizi += 1
                    print("\033[1;31;40m Mēģini vēlreizs!")
    
if atbildes <= 4:
    print (f"\033[1;35;40mTu pareizi atminēji {atbildes} mīklas. Nebēdājies un mēģini vēlreiz!😉")
elif atbildes <= 8:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Tev labi padodas minēt mīklas, tā turpināt!😁")
else:
    print (f"Tu pareizi atminēji {atbildes} mīklas. Tu esi īsts mīklu minētājs😎")
print(f"Tu pabeidzi minēt mīklas kad bija {(x)}")