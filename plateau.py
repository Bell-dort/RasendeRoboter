import numby as np
import plaque
import random
import case
class plateau(object):
	liste = [0,1,2,3];
	plat = np.array([np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']),
					 np.array([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])])

	#Défini quelle plaque aura quelle position aléatoirement
	elaborationPlateau(L):
		for i in range(4):
			listeChangement = [' ',' ',' ',' '];
			choix = random.choice(L)
			del L[choix];
			listeChangement[i] = choix
		L = listeChangement

	def __init__(self, plaque1,plaque2,plaque3,plaque4):
		#Change l'orientation des plaques aléatoirement entre 0 et 3 fois
		for i in range(randint(0,3)):
			plaque1.switch90()
		for j in range(randint(0,3)):
			plaque2.switch90()
		for t in range(randint(0,3)):
			plaque3.switch90()
		for k in range(randint(0,3)):
			plaque4.switch90()

		listePlaque = [plaque1,plaque2,plaque3,plaque4]
		elaborationPlateau(liste)
		#Défini le plateau avec chaque plaque aléatoire
		for i in range(8):
			for j in range(8):
				self.plat[i][j] = listePlaque[liste[0]].[i][j]
		for i in range(8,16):
			for j in range(8):
				self.plat[i][j] = listePlaque[liste[1]].[i][j]
		for i in range(8):
			for j in range(8,16):
				self.plat[i][j] = listePlaque[liste[2]].[i][j]
		for i in range(8,16):
			for j in range(8,16):
				self.plat[i][j] = listePlaque[liste[3]].[i][j]
		#Défini les cases central au centre du plateau
		for i in range(7,8):
			for j in range(7,8):
				self.plat[i][j] = caseCentral