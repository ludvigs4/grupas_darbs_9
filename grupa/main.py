def main():
    print("sveicināti kartiņu programmā!")
    while True:
        izveles=input("Izvēlaties, ko darīt: \n1.)pievienot kartiņu\n2.)mācīties no kartiņām\n3.)beigt programmu\n izvēle: ")
        if izveles=="1":
            pievienot_kartiti()
        elif izveles=="2":
            macities()
        elif izveles=="3":
            print("exit")
main()