import random
def gubitak(igra, igrac):
    for i in range(3):
        if all(igra[i][j] == igrac for j in range(3)):
            return True
        if all(igra[j][i] == igrac for j in range(3)):
            return True
    if all(igra[i][i] == igrac for i in range(3)) or all(igra[i][2-i] == igrac for i in range(3)):
        return True
    return False

def nerjeseno(igra):
    return all(igra[i][j] != ' ' for i in range(3) for j in range(3))

def ispis(igra):
    print("-" * 9)
    for row in igra:
        print(" | ".join(row))
        print("-" * 9)

def prazna_polja(igra):
    return [igra[i][j] for i in range(3) for j in range(3) if igra[i][j] == ' ']

def ai_potez(igra, x, y):
    
    if gubitak(igra, 'O'):
        return -2
    if gubitak(igra, 'X'):
        return 1
    if nerjeseno(igra):
        return 0
    igra[x][y]='X'
    if gubitak(igra, 'X'):
        return -1
    else:
        igra[x][y]='O'

    najbolje = -float('inf')
    for i in range(3):
        for j in range(3):
            if igra[i][j] == ' ':
                igra[i][j] = 'X' 
                ocjena = ai_potez(igra, i, j)
                igra[i][j] = ' '
                najbolje = max(najbolje, ocjena)
    return najbolje

def najbolji_potez(igra):
    najbolje = -float('inf')
    najbolji_potez = None
    for i in range(3):
        for j in range(3):
            if igra[i][j] == ' ':
                igra[i][j] = 'O'
                potez = ai_potez(igra, i, j)
                igra[i][j] = ' '
                if potez >= najbolje:
                    najbolje = potez
                    najbolji_potez = (i, j)
    return najbolji_potez

def main():
    igra = [[' ' for _ in range(3)] for _ in range(3)]
    print("Autor: Matija Žnidarić \nDobrodošli u Misere varijantu igre Tic Tac Toe! \nU ovoj varijanti igre pobjeđuje igrač koji nema 3 jednaka znaka u nizu. \n")
    ispis(igra)
    print(" ")
    
    print("Mogući potezi su:")
    print(" ")
    for i in range(3):
        for j in range(3):
            if igra[i][j] == ' ':
                print(3 * i + j + 1, end=' ')
            else:
                print("_", end=' ')
        print()
    print(" ")
    
    try:
        igrac_potez = int(input("Unesite broj polja za svoj potez (1-9): "))
        igrac_potez -= 1
        if igrac_potez < 0 or igrac_potez > 8 or igra[igrac_potez // 3][igrac_potez % 3] != ' ':
            print("Neispravan potez. Pokušajte ponovno.")

        igra[igrac_potez // 3][igrac_potez % 3] = 'X'

    except ValueError:
        print("Niste unijeli ispravan broj. Pokušajte ponovno.")
    
  
    ispis(igra)
    
    randx = random.randint(0,2)
    randy = random.randint(0,2)
    print(randx)
    while igra[randx][randy] != ' ':
        randx = random.randint(0,2)
        randy = random.randint(0,2)
    igra[randx][randy]='O' 
    print("AI igra : {}".format(randx*3+randy+1))
    ispis(igra)
    while True:
        print("Mogući potezi su:")
        print(" ")
        for i in range(3):
            for j in range(3):
                if igra[i][j] == ' ':
                    print(3 * i + j + 1, end=' ')
                else:
                    print("_", end=' ')
            print()
        print(" ")
        
        try:
            igrac_potez = int(input("Unesite broj polja za svoj potez (1-9): "))
            igrac_potez -= 1
            if igrac_potez < 0 or igrac_potez > 8 or igra[igrac_potez // 3][igrac_potez % 3] != ' ':
                print("Neispravan potez. Pokušajte ponovno.")
                continue

            igra[igrac_potez // 3][igrac_potez % 3] = 'X'

        except ValueError:
            print("Niste unijeli ispravan broj. Pokušajte ponovno.")
            continue

        if gubitak(igra, 'X'):
            print("AI je pobjedio!")
            ispis(igra)
            break

        if nerjeseno(igra):
            print("Igra je završila neriješeno.")
            ispis(igra)
            break

        ispis(igra)

        ai_i, ai_j = najbolji_potez(igra)
        igra[ai_i][ai_j] = 'O'
        print("AI igra : {}".format(ai_i*3+ai_j+1))
        ispis(igra)
        
        if gubitak(igra, 'O'):
            print("Pobjedili ste! Cestitam.")
            ispis(igra)
            break

        if nerjeseno(igra):
            print("Igra je završila neriješeno.")
            ispis(igra)
            break


main()