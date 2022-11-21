import utils


poj = utils.Pojistenci


def menu ():
    exit = "false"
    print ("Vítejte v menu\n")
    while (exit == "false"):
        try:
            vstup = int(input("Vyberte z možností \n 1: vytvoření nového pojištěnce \n 2: Vypsat všechny pojištěnce\n 3: Vyhledat pojištence\n 4: Konec\n "))
            if 0 < vstup and vstup< 5:
                match vstup: 
                    case 1:
                        print ("Zvolil jsme volbu 1\n")
                        utils.regular(poj)
                    case 2:
                        print ("Zvolil jsme volbu 2\n")
                        utils.vypisvsech()
                    case 3:
                        vyber = int(input("Zvolil jsme volbu 3\n Kritéria výběru \n 1: Podle jména\n 2: Podle příjmení\n 3: Podle věku\n 4: Podle telefoního čísla\n"))
                        if 0 < vyber and vyber < 5:
                            match vyber:
                                case 1: 
                                    jmeno = input ("Zadej jméno\n")
                                    utils.prohledavacka (jmeno, 1)
                                case 2:
                                    prijmeni = input ("Zadejte příjmení\n")
                                    utils.prohledavacka(prijmeni,2)
                                case 3:
                                    vek = int (input ("Zadejte věk\n"))
                                    utils.prohledavacka(vek, 3)
                                case 4:
                                    cislo = int (input ("Zadejte telefon\n"))
                                    utils.prohledavacka(cislo, 4)
                        else:
                            print ("Nezadali jste platnou volbu")           
                    case 4:
                        print ("Zvolil jsme volbu 4\n")
                        exit = "true"
            else:
                print ("Nezadali jste platnou volbu\n")
        except:
            print ("Zadejte ČÍSLO !!\n")    
        


menu()




