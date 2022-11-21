list = []

class Pojistenci:
    def __init__(self,jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

def druhy_pokus():
        a = (input("Zadejte JMENO !!!! \n\n"))
        b=  (input("Zadejte PŘÍJMENÍ !! \n\n"))
        try:
            c=  int(input("Zadejte věk \n"))
        except:
            print("Nezadal jste číslo")
            return 
        try:
            d = int(input("Zadejte telefoní číslo \n"))
        except:
            print ("Nezadal jste číslo")
            return
        list.append(Pojistenci(a,b,c,d))  

def regular(poj):
        a = (input("Zadejte jméno \n"))
        b =  (input("Zadejte příjmeni \n"))
        try:
            c =  int(input("Zadejte věk \n"))
        except:
            print("Nezadal jste číslo")
            druhy_pokus() 
            return
        try:
            d = int(input("Zadejte telefoní číslo \n"))
        except:
            print ("Nezadal jste číslo")
            druhy_pokus()
            return
        list.append(poj(a,b,c,d))


    

def vypisvsech():
        a = len (list)
        if a == 0:
            print ("Seznam je prázdný ! \n")
        else:
            for x in list:
                    print(x.jmeno,x.prijmeni,x.vek, x.telefon)

def prohledavacka(param, cislo):
        b = len (list)
        if b == 0:
            print ("Seznam je prázdný !! \n")
        else:
            match cislo:
                case 1: 
                    for i in list:
                        if i.jmeno == param:
                            print(i.jmeno,i.prijmeni,i.vek, i.telefon)    
                case 2: 
                    for i in list:
                        if i.prijmeni == param:
                            print(i.jmeno,i.prijmeni,i.vek, i.telefon)    
                case 3: 
                    for i in list:
                        if i.vek == param:
                            print(i.jmeno,i.prijmeni,i.vek, i.telefon)    
                case 4: 
                    for i in list:
                        if i.telefon == param:
                            print(i.jmeno,i.prijmeni,i.vek, i.telefon)  
