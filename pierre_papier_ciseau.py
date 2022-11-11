#Debut
	#Importer le module random

	#Definir la fonction Round prennant pour paramètre action
	    #Assigner à jAction la valeur retour de l'execution int() prennant en paramètre action
	    #Si jAction est inferieur à 1 ou supérieur à 3
	        #Alors retourner "Mauvais input"
	    #Assigner iaAction une valeur aléatoire entre 1, et 3 inclu
	    #Si iaAction est égal à jAction
	        #Alors retourner "Egalité"
	    #Si jAction est supérieur à iaAction et iaAction + 1 vaut jAction ou
	    # jAction est inférieur à iaAction et jAction + iaAction vaut 2
	        #Alors retourner "Gagner"
	    #Retourner "Perdu"

	#Definir la fonction BO
	    #Assigner à entry la valeur retour de l'execution input() qui demande à l'utilisateur en combien sera le BO
	    #Assigner à scoreNeed la valeur retour de l'execution int prennant comme paramètre entry
	    #Assigner à scoreJ 0
	    #Assigner à scoreIA 0
	    #Tant que scoreIA est inférieur à scoreNeed et scoreJ est inférieur à scoreNeed
	        #Alors
	        #Assigner à key la valeur retour de l'execution input qui demande à l'utilisateur l'action qu'il veut faire
	        #Si key vaut 4
	            #Alors imprimer le score actuel
	        #Sinon
	            #Alors
	            #Assigner à result le retour de Round prennant en paramètre key
	            #Si result vaut "Gagner"
	                #Alors incrementer scoreJ
	            #Sinon si result vaut "Perdu"
	                #Alors incrementer scoreIA
	            #Imprimer le résultat
	    #Si scoreIA est supérieur à scoreJ
	        #Alors imprimer le message de défaite
	    #Sinon
	        #Alors imprimer le message de victoire

	#Definir la fonction PVP
	    #Assigner à scoreJ1 0
	    #Assigner à scoreJ2 0
	    #Tant que vrai
	        #assigner à entry la valeur retour de l'execution de input
	        #assigner à key la valeur retour de int prennant pour paramètre entry
	        #Si key est egal à 4
	            #Alors imprimer les scores
	        #Sinon si key vaut 5
	            #Alors sortir de la boucle
	        #Sinon
	            #Alors
	            #assigner à entry la valeur retour de l'execution de input
	            #assigner à key2 la valeur retour de int prennant pour paramètre entry
	            #Si key est inférieur à 1 ou key supérieur à 3
	            # ou key2 est inférieur à 1 ou key2 supérieur à 3
	                #Alors imprimer "Mauvais input"
	            #Sinon si key vaut key2
	                #Alors imprimer "Egalité"
	            #Sinon si key est supérieur à key2 et key2 + 1 vaut key ou
	            # key est inférieur à key2 et key + key2 vaut 2
	                #Alors incrementer scoreJ1
	                #Imprimer "J1 à gagner"
	            #Sinon
	                #Alors incrementer scoreJ2
	                #Imprimer "J1 à gagner"
	    #Si scoreJ1 est supérieur à scoreJ2
	        #Alors imprimer message victoire J1
	    #Sinon
	        #Alors imprimer message victoire J2

	#Definir la fonction Game
	    #Assigner à scoreJ 0
	    #Assigner à scoreIA 0
	    #Tant que vrai
	    # #Alors
	        #Assigner à key la valeur retour de l'execution input qui demande à l'utilisateur l'action qu'il veut faire
	        #Si key vaut 4
	            #Alors imprimer le score actuel
	        #Sinon si key vaut 5
	            #Alors 
	            #scoreJ = 0
	            #scoreIA = 0
	        #Sinon si key vaut 6
	            #Alors appeler la fonction BO
	        #Sinon si key vaut 7
	            #Alors appeler la fonction  PVP
	        #Sinon
	            #Alors
	            #Assigner à result le retour de l'execution Round prennant en paramètre key
	            #Si result vaut "Gagner"
	                #Alors incrementer scoreJ
	            #Sinon si result vaut "Perdu"
	                #Alors incrementer scoreIA
	            #Imprimer le résultat

	#Appeler la fonction Game
#Fin