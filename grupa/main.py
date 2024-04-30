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

def galvena():
    print("sveicināti kartiņu programmā!")
    while True:
        izveles=input("Izvēlaties, ko darīt: \n1.)pievienot kartiņu\n2.)mācīties no kartiņām\n3.)beigt programmu\n izvēle: ")
        if izveles=="1":
            pievienot_kartiti()
        elif izveles=="2":
            macities()
        elif izveles=="3":
            print("exit")

galvena()
