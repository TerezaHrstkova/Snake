from random import randrange
zadani = [(0, 0), (1, 0), (2, 0)]
seznam_ovoce = [(2,3)]
cislo = len(zadani)

def nakresli_mapu(seznam, ovoce):
    tabulka = []
    for radek in range(10):
        radek = []
        for sloupec in range(10):
            radek.append(".")
        tabulka.append(radek)

    for radek, sloupec in seznam:
        tabulka[sloupec][radek] = 'X'

    for radek, sloupec in ovoce:
        tabulka[sloupec][radek] = '0'

    for radek in tabulka:
        for prvek in radek:
            print(prvek, end=" ")
        print()

def nove_ovoce(ovoce, souradnice):
    while True:
        x = randrange(10)
        y = randrange(10)
        if (x,y) not in souradnice and (x,y) not in ovoce:
            ovoce.append((x,y))
            break

def pohyb(souradnice, svetova_strana, ovoce):
    "Dostane seznam souřadnic a světovou stranu a přidá k seznamu poslední bod „posunutý“ v daném směru."
    posledni = souradnice[-1]
    if svetova_strana =="s":
        nova_souradnice = (posledni[0], posledni[1]-1)
    elif svetova_strana =="j":
        nova_souradnice = (posledni[0], posledni[1]+1)
    elif svetova_strana =="v":
        nova_souradnice = (posledni[0]+1, posledni[1])
    elif svetova_strana =="z":
        nova_souradnice = (posledni[0]-1, posledni[1])
    else:
        return"Musite zadat jednu ze svetovych stran: s, j, v nebo z."
        
    if nova_souradnice in souradnice:
        raise ValueError("Game over!")
    elif nova_souradnice[0] <0 or nova_souradnice[0] >9  or nova_souradnice[1] <0 or nova_souradnice[1] >9:
        raise ValueError("Game over!")
    else:
        souradnice.append(nova_souradnice)
    
    if nova_souradnice not in ovoce:    
        del souradnice[0]
    else:
        ovoce.remove(nova_souradnice)    
        nove_ovoce(ovoce, souradnice)
    return souradnice, ovoce

tah = 0
while True:
    if tah%30 == 0:
        nove_ovoce(seznam_ovoce, zadani)
    novy_bod = input("Zadejte jednu ze svetovych stran: s, j, v nebo z:")
    pohyb(zadani,novy_bod, seznam_ovoce)
    tah +=1
    nakresli_mapu(zadani, seznam_ovoce)