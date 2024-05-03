import random

def macities(prieksmets, tema):
    try:
        with open(f"{prieksmets}_{tema}.txt", "r", encoding="utf8") as file:
            rindas = file.readlines()
            random_rinda = random.choice(rindas).strip().split(" - ")
            print(random_rinda[0])
            input("Spiediet enter lai parādītu atbildi!")
            print(random_rinda[1])
    except FileNotFoundError:
        print("Šāda faila nav!💀💀💀")

def izdzest(prieksmets, tema, jautajums, atbilde):
    kopa = f"{jautajums} - {atbilde}"
    print(kopa)
    rindas = []
    try:
        with open(f"{prieksmets}_{tema}.txt", "r", encoding="utf8") as file:
            rindas = file.readlines()
            rindas[0].split(" - ")
        with open(f"{prieksmets}_{tema}.txt", "w", encoding="utf8") as file:
            for i in rindas:
                if kopa != i:
                    file.write(i)
    except FileNotFoundError:
        print("Šāda faila nav!💀💀💀")

def galvena():
    print("sveicināti kartiņu programmā!")
    while True:
        izveles=input("Izvēlaties, ko darīt: \n1.)pievienot kartiņu\n2.)mācīties no kartiņām\n3.)dzēst kartīti\n izvēle: ")
        if izveles == "1":
            #pievienot_kartiti()
            pass
        elif izveles == "2":
            macities("fizika", "energija")
        elif izveles == "3":
            prieksmets = input("Ievadiet priekšmetu no, kura vēlaties dzēst: ")
            tema = input("Ievadiet tēmu no, kuras vēlaties dzēst: ")
            jaut = input("Ievadiet jautājumu, kura vēlaties dzēst: ")
            atb = input("Ievadiet atbildi, kuru vēlaties dzēst: ")
            izdzest(prieksmets, tema, jaut, atb)

galvena()