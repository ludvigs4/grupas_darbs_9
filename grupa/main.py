import random

def pievienot_kartiti(prieksmets,tema,info,atbilde):
    with open(f"{prieksmets}_{tema}.txt", "a", encoding="utf8") as fails:
        fails.write(f"{info} - {atbilde}")

def macities(prieksmets, tema): #izveido funkciju no, kuras varēs mācīties no kartītēm
    try:
        with open(f"{prieksmets}_{tema}.txt", "r", encoding="utf8") as file: #atver failu ar iedotā priekšmeta un tēmas nosaukumu
            rindas = file.readlines() #izlasa failu un ieraksta to sarakstā
            if len(rindas) > 0: #ja failā ir jautājumi
                random_rinda = random.choice(rindas).strip().split(" - ") #izvēlas nejaušu rindu un to sadala uz jautājumu un atbildi
                print(random_rinda[0])
                input("Spiediet enter lai parādītu atbildi!")
                print("\t>" + random_rinda[1])
            else: #ja failā nav jautājumu
                print("Šajā failā vairs nav datu!")
    except FileNotFoundError: #ja fails neeksistē vai nepareizi ievadīti faili
        print("Jums nav failu vai nepareizi ievadīti dati!💀💀💀")

def izdzest(prieksmets, tema, jautajums, atbilde): #Funkcijas mērķis ir izdzēst kartīti no prieksmets_tema.txt faila, kuru lietotājs jau pirms tam pats ir izveidojis
    kopa = f"{jautajums} - {atbilde}"
    print(kopa)
    rindas = []
    try:
        with open(f"{prieksmets}_{tema}.txt", "r", encoding="utf8") as file:
            rindas = file.readlines()
        with open(f"{prieksmets}_{tema}.txt", "w", encoding="utf8") as file:
            for i in rindas:
                if kopa != i.strip():
                    file.write(i)
    except FileNotFoundError:
        print("Šāda priekšmeta vai tēmas nav!💀💀💀")

def galvena():
    print("Sveicināti kartiņu programmā!")
    while True:
        izveles=input("\nIzvēlieties, ko darīt: \n1.)pievienot kartiņu\n2.)mācīties no kartītēm\n3.)dzēst kartīti\n'iziet' - iziet no programmas\n\nizvēle: ")
        if izveles == "1":
            prieksmets = input("Ievadiet priekšmetu, kurā vēlaties pievienot kartīti: ")
            tema = input("Ievadiet tēmu: ")
            jaut = input("Ievadiet jautājumu: ")
            atb = input("Ievadiet atbildi: ")
            pievienot_kartiti(prieksmets, tema, jaut, atb)
            pass
        elif izveles == "2":
            prieksmets = input("Ievadiet priekšmetu: ")
            tema = input("Ievadiet tēmu: ")
            macities(prieksmets, tema)
        elif izveles == "3":
            prieksmets = input("Ievadiet priekšmetu no, kura vēlaties dzēst: ")
            tema = input("Ievadiet tēmu no, kuras vēlaties dzēst: ")
            jaut = input("Ievadiet jautājumu, kuru vēlaties dzēst: ")
            atb = input("Ievadiet atbildi, kura ir pie jautājuma: ")
            izdzest(prieksmets, tema, jaut, atb)
        elif izveles == "iziet":
            print("Programma beidzas!💀")
            exit()
        else:
            print("Izvēlieties derīgu opciju!")

galvena()
