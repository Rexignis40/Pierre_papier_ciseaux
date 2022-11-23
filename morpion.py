#a joueur 1 z joueur 2

from copy import deepcopy
from time import sleep

#Fonction pour afficher dans la console
def Draw(grille):
    result = "\n"
    i = 0
    rowCount = 0
    #Boucle toute les valeurs de la grille
    for i in range(9):
        rowCount += 1
        result += "|" + str(grille[i]) + " "
        #Pour faire une nouvelle ligne
        if(rowCount == 3):
            rowCount = 0
            result += "|\n--- --- ---\n"
    print(result)

#Fonction pour savoir si l'on peut poser sur la case spécifier
def TestCase(key, grille):
    k = int(key) - 1
    if(k < 0 or k > 8):
        return 10
    if(grille[k] == 'O' or grille[k] == 'X'):
        return 11
    return k

#Renvoie le symbole du vainqueur s'il y en a un
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

#Prise de décision de l'IA
def IAMove(grille):
    #Prevoir un tour
    for i in range(9):
        testGrille = deepcopy(grille)
        if(testGrille[i] == 'X' or testGrille[i] == 'O'):
            continue
        testGrille[i] = 'X'
        #Test IA vixctoire
        if(TestWin(testGrille) == 'X'):
            return i
        testGrille[i] = 'O'
        if(TestWin(testGrille) == 'O'):
            return i
        #Prevoir deux tour
        for j in range(9):
            if(testGrille[j] == 'X' or testGrille[j] == 'O'):
                continue
            testGrille[j] = 'O'
            if(TestWin(grille) == 'O'):
                return j
            testGrille[j] = ' '
        testGrille[i] = ' '
    return GetBestPos(grille)

#Pour avoir la meilleur position pour poser
def GetBestPos(grille):
    caseFree = []
    #Boucle pour récupérer les cases libres
    for i in range(9):
        if(grille[i] != 'X' and grille[i] != 'O'):
            caseFree.append(i)
    if(4 in caseFree):
        return 4
    if(0 in caseFree):
        return 0
    if(2 in caseFree):
        return 2
    if(6 in caseFree):
        return 6
    if(8 in caseFree):
        return 8
    return caseFree[0]

#Retourne si la grille est remplie
def TestGrilleFull(grille):
    i = 0
    for i in range(9):
        if(grille[i] != 'O' and grille[i] != 'X'):
            return False
    return True

def SetAllGridWith(grid, c):
    for i in range(9):
        grid[i] = c
        Draw(grid)
        sleep(0.3)
    return grid

#Boucle du jeu
def Game():
    scoreJ1 = 0
    scoreIA = 0
    grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    whichTurn = False
    Draw(grille)
    isPlay = True
    while isPlay:
        if(whichTurn):
            grille[IAMove(grille)] = 'X'
            whichTurn = False
            Draw(grille)
        else:
            key = input("\nentrée votre numéro de case\nScore: s, Reset: r, Exit e\n")
            if(key == 's'):
                print("\nSCORE JOUEUR 1: " + str(scoreJ1) + "\nSCORE JOUEUR IA: " + str(scoreIA))
            elif (key == 'r'):
                scoreJ1 = 0
                scoreIA = 0
            elif (key == 'e'):
                isPlay = False
            elif (key == 'w'):
                grille = SetAllGridWith(grille, 'O')
            else:
                result = TestCase(key, grille)
                if(result == 11):
                    print("case déjà prise")
                elif(result == 10):
                    print("Mauvais input")
                else:
                    grille[result] = 'O'
                    whichTurn = True
                    Draw(grille)
        w = TestWin(grille)
        if(w == 'O'):
            scoreJ1 += 1
            print("Joueur 1 à gagner")
            grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            Draw(grille)
        elif(w == 'X'):
            scoreIA += 1
            print("IA à gagner")
            grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            Draw(grille)
        elif(TestGrilleFull(grille)):
            print("Egalité")
            grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            Draw(grille)

Game()
