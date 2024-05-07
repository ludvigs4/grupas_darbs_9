import random

def pievienot_kartiti(prieksmets,tema,info,atbilde): #funkcija saņem 4 mainīgos, ar kuru palīdzību uztaisa failu, kurā glabāsies jautājums ar atbildi.
    with open(f"{prieksmets}_{tema}.txt", "a", encoding="utf8") as fails: #atver failu, kurā rakstīs. Ja nav faila, tad to uztaisa.
        fails.write(f"{info} - {atbilde}\n")

def macities(prieksmets, tema): #izveido funkciju no, kuras varēs mācīties no kartītēm
    try:
        with open(f"{prieksmets}_{tema}.txt", "r", encoding="utf8") as file: #atver failu ar iedotā priekšmeta un tēmas nosaukumu
            rindas = file.readlines() #izlasa failu un ieraksta to sarakstā
            if len(rindas) > 0: #ja failā ir jautājumi
                random_rinda = random.choice(rindas).strip().split(" - ") #izvēlas nejaušu rindu un sadala to divās daļās - par jautājumu un atbildi
                print("Jautājums\t>" + random_rinda[0])
                input("Spiediet enter lai parādītu atbildi!")
                print("atbilde\t>" + random_rinda[1])
            else: #ja failā nav jautājumu
                print("Šajā failā vairs nav datu!")
    except FileNotFoundError: #ja fails neeksistē vai nepareizi ievadīti faili
        print("Jums nav failu vai nepareizi ievadīti dati!💀💀💀")

def izdzest(prieksmets, tema, jautajums, atbilde): #Funkcijas mērķis ir izdzēst kartīti no prieksmets_tema.txt faila, kuru lietotājs jau pirms tam pats ir izveidojis
    kopa = f"{jautajums} - {atbilde}" #izveido mainīgo, kurš satur jautājumu un atbildi
    rindas = [] # izveido sarakstu, kurš saturēs visas rindas
    try:
        with open(f"{prieksmets}_{tema}.txt", "r", encoding="utf8") as file: #atver failu lasīšanas režīmā
            rindas = file.readlines() #sarakstā pievieno visas rindas
        with open(f"{prieksmets}_{tema}.txt", "w", encoding="utf8") as file: #atver failu rakstīšanas režīmā
            for i in rindas: #ciklē cauri visām rindām
                if kopa != i.strip(): #ja izvēlētā kartīte nav vienāda ar esošo kartīti, tad to ieraksta failā
                    file.write(i)
    except FileNotFoundError: #ja nepareizi ievadīti dati
        print("Šāda priekšmeta vai tēmas nav!💀💀💀")

def galvena(): #izveido galveno funkciju
    print("Sveicināti kartīšu programmā!")
    while True: #galvenais cikls, kurš iet kamēr tiek uzrakstīts "iziet"
        izveles=input("\nIzvēlieties, ko darīt: \n1.)pievienot kartīti\n2.)mācīties no kartītēm\n3.)dzēst kartīti\n'iziet' - iziet no programmas\n\nizvēle: ")
        if izveles == "1": #ja izvēlas opciju pievienot kartīti
            prieksmets = input("Ievadiet priekšmetu, kurā vēlaties pievienot kartīti: ")
            tema = input("Ievadiet tēmu: ")
            jaut = input("Ievadiet jautājumu: ")
            atb = input("Ievadiet atbildi: ")
            pievienot_kartiti(prieksmets, tema, jaut, atb) #izsauc funkciju, kura pievino kartīti
        elif izveles == "2": #ja izvēlas opciju mācīties
            prieksmets = input("Ievadiet priekšmetu: ")
            tema = input("Ievadiet tēmu: ")
            macities(prieksmets, tema) #izsauc funkciju, kurā var mācīties no kartītēm
        elif izveles == "3": #ja izvēlas opciju dzēst kartīti
            prieksmets = input("Ievadiet priekšmetu no, kura vēlaties dzēst: ")
            tema = input("Ievadiet tēmu no, kuras vēlaties dzēst: ")
            jaut = input("Ievadiet jautājumu, kuru vēlaties dzēst: ")
            atb = input("Ievadiet atbildi, kura ir pie jautājuma: ")
            izdzest(prieksmets, tema, jaut, atb) #izsauc funkciju, kura izdzēsīs kartīti
        elif izveles == "iziet": #ja izvēlas iziet no programmas
            print("Programma beidzas!💀")
            exit() #iziet no programmas
        else: #ja ievada, kas nav opcijās
            print("Izvēlieties derīgu opciju!")

galvena() #izsauc galveno funkciju
