#Importer la fonction copy depuis deepcopy

#Definir la fonction pour afficher la grille dans la console
    #Assigner "\n" à la variable result
    #Assigner 0 à i
    #Assigner 0 à rowCount
    #Boucler toute les valeurs de la grille
        #Incrementer rowCount
        #Ajouter la case à résult
        #Si rowCount vaut 3
            #Alors rowCount vaut 0
            #Ajouter à result un retour à la ligne
    #Imprimer result

#Definir la fonction pour savoir si l'on peut poser sur la case spécifier
    #Assigner à k la valeur retour de int prennant en paramtre key le tout moins 1
    #Si k est inférieur à 0 ou k est supérieur à 8
        #Alors returner 10
    #Si la valeur à l'index k dans le tableu grille vaut 'O' ou vaut 'X'
        #Alors retourner 11
    #Retourner k

#Definir la fonction qui envoie le symbole du vainqueur s'il y en a un    
    #Si la grille à l'index 0 vaut la grille à l'index 1 et que la grille à l'index 0 vaut la grille à l'index 2 et que la grille à l'index 0 vaut une case vide
        #Alors retourner la variable de la grille à l'index 0
    #Si la grille à l'index 3 vaut la grille à l'index 4 et que la grille à l'index 3 vaut la grille à l'index 5 et que la grille à l'index 3 vaut une case vide
        #Alors retourner la variable de la grille à l'index 3
    #Si la grille à l'index 6 vaut la grille à l'index 7 et que la grille à l'index 6 vaut la grille à l'index 8 et que la grille à l'index 6 vaut une case vide
        #Alors retourner la variable de la grille à l'index 6
    
    #Test des colonne
    #Si la grille à l'index 0 vaut la grille à l'index 1 et que la grille à l'index 0 vaut la grille à l'index 6 et que la grille à l'index 0 vaut une case vide
        #Alors retourner la variable de la grille à l'index 0
    #Si la grille à l'index 1 vaut la grille à l'index 4 et que la grille à l'index 1 vaut la grille à l'index 7 et que la grille à l'index 1 vaut une case vide
        #Alors retourner la variable de la grille à l'index 1
    #Si la grille à l'index 2 vaut la grille à l'index 5 et que la grille à l'index 2 vaut la grille à l'index 8 et que la grille à l'index 2 vaut une case vide
        #Alors retourner la variable de la grille à l'index 2
    
    #Test des diagonales
    #Si la grille à l'index 0 vaut la grille à l'index 4 et que la grille à l'index 0 vaut la grille à l'index 8 et que la grille à l'index 0 vaut une case vide
        #Alors retourner la variable de la grille à l'index 0
    #Si la grille à l'index 2 vaut la grille à l'index 4 et que la grille à l'index 2 vaut la grille à l'index 6 et que la grille à l'index 2 vaut une case vide
        #Alors retourner la variable de la grille à l'index 0

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