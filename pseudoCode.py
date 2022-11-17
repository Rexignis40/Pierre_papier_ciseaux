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
#Définir la fonction IAMove ayant comme paramètre grille
    #Prevoir un tour
    #Tant que i est inférieur à 9
        #Assigner à testGrille, deepcopy(grille)
        #Si le tableau testGrille ayant comme paramètre i est strictement égal à 'X' ou 'O'
            #Continuer
        #Assigner à testGrille ayant comme paramètre i, 'X'
        #Test IA vixctoire
        #Si TestWin ayant comme paramètre testGrille est égal à 'X'
            #Retourner i
        #Assigner à testGrille ayant comme paramètre i, 'O' 
        #Si TestWin ayant comme paramètre testGrille est égal à 'O'
            #Retourner i
        #Prevoir deux tour
        #Tant que j est inférieur à 9
            #Si le tableau testGrille ayant comme paramètre j est égal à 'X' ou 'O'
                #Continuer
            #Assigner à testGrille ayant comme paramètre j, 'O'
            #Si TestWin ayant comme paramètre grille est égal à 'O'
                #Retourner j
            #Assigner à testGrille ayant comme paramètre j, ' '
        #Assigner à testGrille ayant comme paramètre i, ' '
    #Retourner GetBestPos ayant comme paramètre grille

#Pour avoir la meilleur position pour poser
#Définir la fonction GetBestPos ayant comme paramètre grille
    #Assigner à caseFree, [], un tableau vide 
    #Boucle pour récupérer les cases libres
    #Tant que i est inférieur à 9
        #Si le tableau grille ayant comme paramètre i n'est pas égal à 'X' et 'O'
            #Donner à caseFree.append le paramètre i
    #Si on trouve 4 dans caseFree
        #Retourner 4
    #Si on trouve 0 dans caseFree
        #Retourner 0
    #Si on trouve 2 dans caseFree
        #Retourner 2
    #Si on trouve 6 dans caseFree
        #Retourner 6
    #Si on trouve 8 dans caseFree
        #Retourner 8
    #Retourner caseFree ayant comme paramètre 0

#Retourne si la grille est remplie

#Definir la fonction de la boucle du jeu
    #Assignier 0 à scoreJ1
    #Assignier 0 à scoreIA
    #Assignier numéros de chaque cases à grille
    #Assigner false à whichTurn
    #Appeler la fonction Draw et lui passert comme paramètre grille
    #Assigner True à isPlay
    #Tant que isPlay
        #Alors
        #Si whichTurn
            #Alors 
            #Assigner le resultat de IAMove prennant comme paramètre grille à nextMove
            #Assigner à l'index nextMove de grille la valeur 'X'
            #Assigner False à whichTurn
            #Appeler la fonction Draw en lui passant pour paramètre grille
        #Sinon
            #Alors
            #Assigner à key le résultat de la fonction input demander à l'utilisateurs qu'elle action veut-il faire
            #Si key vaut 'S'
                #Alors imprimer les scores globaux
            #Sinon si key vaut 'r'
                #Alors 
                #Assignier 0 à scoreJ1
                #Assignier 0 à scoreIA
            #Sinon si key vaut e
                #Alors assigner False à isPlay
            #Sinon
                #Alors
                #Assigner la valeur retour de TestCase prennat en paramètre key et grille
                #Si result vaut 11
                    #Alors imprimer "case déjà prise"
                #Sinon si result vaut 10
                    #Alors imprimer "Mauvais input"
                #Sinon
                    #Alors
                    #Assigner 'O' dans le tableau grille à l'index result
                    #Aassigner True à isPlay
                    #Appeller la fonctoni Draw prennant comme paramètre grille
        #Assigner le résultat de TestWin à w
        #Si w vaut 'O'
            #Alors
            #Incrementer scoreJ1
            #Imprimer message de victoire
            #Assigner les valeurs de bases à grille
            #Appeler la fonction Draw prennant comme paramètre grille
        #Sinon si w == 'X'
            #Alors
            #Incrementer scoreIA
            #Imprimer message de défaite
            #Assigner les valeurs de bases à grille
            #Appeler la fonction Draw prennant comme paramètre grille
        #Sinon si le resultatde TestGrilleFull prennant comme paramètres grille
            #Alors
            #Imprimer message d'égalité
            #Assigner les valeurs de bases à grille
            #Appeler la fonction Draw prennant comme paramètre grille

#Appeler la Game