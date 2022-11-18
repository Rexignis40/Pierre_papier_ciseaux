import random

def Round(action):
    jAction = int(action)
    if(jAction < 1 or jAction > 3):
        return "Mauvais input"
    iaAction = random.randint(1, 4)
    if(iaAction == jAction):
         return "Egalité"
    if((jAction > iaAction and iaAction + 1 == jAction) or (jAction < iaAction and jAction + iaAction == 4)):
        return "Gagner"
    return"Perdu"

def BO():
    scoreNeed = int(input("\nEn combien sera votre BO\n"))
    scoreJ = 0
    scoreIA = 0
    while(scoreIA < scoreNeed and scoreJ < scoreNeed):
        key = int(input("\n1: pierre, 2: papier, 3: ciseaux, 4: score\n"))
        if(key == 4):
            print("\nJ1: " + str(scoreJ) + "\nIA: " + str(scoreIA))
        else:
            result = Round(key)
            #Si result vaut "Gagner
            if(result == "Gagner"):
                scoreJ += 1
            elif(result == "Perdu"):
                scoreIA += 1
            print(result)
    if(scoreIA > scoreJ):
        print("\nVous avez perdu\n")
    else:
        print("\nVous à gagner\n")

def PVP():
    scoreJ1 = 0
    scoreJ2 = 0
    while(True):
        key = int(input("\n1: pierre, 2: papier, 3: ciseaux, 4: score, 5: exit\n"))
        if(key == 4):
            print("\nJ1: " + str(scoreJ1) + "\nJ2: " + str(scoreJ2))
        elif(key == 5):
            break
        else:
            key2 = int(input("\n1: pierre, 2: papier, 3: ciseaux\n"))
            if(key < 1 or key > 3 or key2 < 1 or key2 > 3):
                print("\nMauvais input")
            if(key2 == key):
                print("\nEgalité\n")
            elif((key > key2 and key2 + 1 == key) or (key < key2 and key + key2 == 4)):
                scoreJ1 += 1
                print("\nJ1 à gagner\n")
            else:
                scoreJ2 += 1
                print("\nJ2 à gagner\n")
    if(scoreJ1 > scoreJ2):
        print("\nJ1 à gagner le BO\n")
    else:
        print("J2 à gagner la BO")

def Game():
    scoreJ = 0
    scoreIA = 0
    while(True):
        key = int(input("\n1: pierre, 2: papier, 3: ciseaux, 4: score, 5: reset\nGame Mode\n6: BO, 7: PVP\n"))
        if(key == 4):
            print("\nJ1: " + str(scoreJ) + "\nJ2: " + str(scoreIA))
        elif(key == 5):
            scoreJ = 0
            scoreIA = 0
        elif(key == 6):
            BO()
        elif(key == 7):
            PVP()
        else:
            result = Round(key)
            if(result == "Gagner"):
                scoreJ += 1
            elif(result == "Perdu"):
                scoreIA += 1
            print(result)
    
Game()