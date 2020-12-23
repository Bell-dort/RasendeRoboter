import numby as np
import plaque
import random
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

	"""docstring for plateau"""
	elaborationPlateau(L):
		for i in range(4):
			listeChangement = [' ',' ',' ',' '];
			choix = random.choice(L)
			del L[choix];
			listeChangement[i] = choix
		L = listeChangement
	def __init__(self, plaque1,plaque2,plaque3,plaque4):
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
		for i in range(8):
			for j in range(8):
				plat[i][j] = listePlaque[liste[0]].[i][j]
		for i in range(8,16):
			for j in range(8):
				plat[i][j] = listePlaque[liste[1]].[i][j]
		for i in range(8):
			for j in range(8,16):
				plat[i][j] = listePlaque[liste[2]].[i][j]
		for i in range(8,16):
			for j in range(8,16):
				plat[i][j] = listePlaque[liste[3]].[i][j]
		