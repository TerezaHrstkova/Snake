zadani = [(0, 0), (1, 0), (2, 0)]
cislo = len(zadani)

def nakresli_mapu(seznam):
    tabulka = []
    for radek in range (10):
        radek = []
        for sloupec in range(10):
            radek.append(".")
        tabulka.append(radek) 
       
    for radek, sloupec in seznam:
        tabulka[sloupec][radek] = 'X'

    for radek in tabulka:
        for prvek in radek:
            print (prvek, end = " ")
        print()

def pohyb(souradnice, svetova_strana):
    "Dostane seznam souřadnic a světovou stranu a přidá k seznamu poslední bod „posunutý“ v daném směru."
    posledni = souradnice[-1]
    if svetova_strana =="s":
        nova_souradnice = (posledni[0], posledni[1]-1)
    elif svetova_strana =="j":
        nova_souradnice = (posledni[0], posledni[1]+1)
    elif svetova_strana =="v":
        nova_souradnice = (posledni[0]+1, posledni[1])
    elif svetova_strana =="z":
        nova_souradnice = (posledni[0]-1, posledni[1]+1)
    else:
        return"Musite zadat jednu ze svetovych stran: s, j, v nebo z."
        
    if nova_souradnice in souradnice:
        raise ValueError("Game over!")
    elif nova_souradnice[0] <0 or nova_souradnice[0] >9  or nova_souradnice[1] <0 or nova_souradnice[1] >9:
        raise ValueError("Game over!")
    else:
        souradnice.append(nova_souradnice)
    del souradnice[0]
    return souradnice
  
while True:
    novy_bod = input("Zadejte jednu ze svetovych stran: s, j, v nebo z:")
    nove_zadani = pohyb(zadani,novy_bod)
    print(nove_zadani)
    nakresli_mapu(nove_zadani)