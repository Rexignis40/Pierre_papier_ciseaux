#a joueur 1 z joueur 2

def Draw(grille):
    result = "\n"
    i = 0
    rowCount = 0
    for i in range(9):
        rowCount += 1
        result += "|" + str(grille[i]) + " "
        if(rowCount == 3):
            rowCount = 0
            result += "|\n--- --- ---\n"
    print(result)

def TestCase(key, grille):
    k = int(key) - 1
    if(k < 0 or k > 8):
        return 10
    if(grille[k] == 'O' or grille[k] == 'X'):
        return 11
    return k

def TestWin(grille):
    #Test des lignes
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return grille[0]
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return grille[3]
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return grille[6]
    #Test des colonne
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return grille[0]
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return grille[1]
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return grille[2]
    #Test des diagonales
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return grille[0]
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return grille[2]

def IsPlayerGonnaWin(grille):
    #Test des lignes
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return grille[0]
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return grille[3]
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return grille[6]
    #Test des colonne
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return grille[0]
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return grille[1]
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return grille[2]
    #Test des diagonales
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return grille[0]
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return grille[2]


def TestGrilleFull(grille):
    i = 0
    for i in range(9):
        if(grille[i] != 'O' and grille[i] != 'X'):
            return False
    return True

def Game():
    scoreJ1 = 0
    scoreJ2 = 0
    grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    whichTurn = False
    Draw(grille)
    isPlay = True
    while isPlay:
        key = input("\nentrée votre numéro de case\nScore: s, Reset: r, Exit e\n")
        if(key == 's'):
            print("\nSCORE JOUEUR 1: " + str(scoreJ1) + "\nSCORE JOUEUR 2: " + str(scoreJ2))
        elif (key == 'r'):
            scoreJ1 = 0
            scoreJ2 = 0
        elif (key == 'e'):
            isPlay = False
        else:
            result = TestCase(key, grille)
            if(result == 11):
                print("case déjà prise")
            elif(result == 10):
                print("Mauvais input")
            else:
                if(whichTurn):
                    grille[result] = "X"
                    whichTurn = False
                else:
                    grille[result] = "O"
                    whichTurn = True
                Draw(grille)
                w =TestWin(grille)
                if(w == 'O'):
                    scoreJ1 += 1
                    print("Joueur 1 à gagner")
                    grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    Draw(grille)
                elif(w == 'X'):
                    scoreJ2 += 1
                    print("Joueur 2 à gagner")
                    grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    Draw(grille)
                elif(TestGrilleFull(grille)):
                    print("Egalité")
                    grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    Draw(grille)

Game()