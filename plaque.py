import numby as np
class plaque(object):
	element = ' '
	"""docstring for plaque"""
	def __init__(self, element):
		self.element = element

	switch90(self):
	tableauRemplacant = np.array([np.array([' ',' ',' ',' ',' ',' ',' ',' ']),
								  np.array([' ',' ',' ',' ',' ',' ',' ',' ']),
								  np.array([' ',' ',' ',' ',' ',' ',' ',' ']),
								  np.array([' ',' ',' ',' ',' ',' ',' ',' ']),
							      np.array([' ',' ',' ',' ',' ',' ',' ',' ']),
								  np.array([' ',' ',' ',' ',' ',' ',' ',' ']),
								  np.array([' ',' ',' ',' ',' ',' ',' ',' ']),
								  np.array([' ',' ',' ',' ',' ',' ',' ',' '])])

	for k in range(8):
		for t in range(8):
			tableauRemplacant[k][t] = self.element[k][t]
	for i in range(8):
		for j in range(8):
			self.element[i][j] = tableauRemplacant[7-j][i].toGauche


plaque1 = plaque(np.array([np.array([caseVide,caseVide,caseVide,caseVide,caseMurBas,caseMurHaut,caseMurDroit,caseVide]),              #0
						   np.array([caseVide,caseVide,caseVide,caseVide,caseVide,caseMurBas,caseCarreJaune,caseVide]),               #1
						   np.array([caseVide,caseVide,caseVide,caseMurBas,caseCercleVert,caseVide,caseVide,caseVide]),               #2
						   np.array([caseMurDroit,caseVide,caseVide,caseVide,caseMurGauche,caseVide,caseVide,caseVide]),              #3
						   np.array([caseMurGauche,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide]),                  #4
						   np.array([caseVide,caseVide,caseLosangeBleu,caseMurHaut,caseVide,caseVide,caseVide,caseVide]),             #5
						   np.array([caseVide,caseVide,caseMurGauche,caseVide,caseVide,caseMurDroit,caseVide,caseMurDroit]),          #6
						   np.array([caseVide,caseVide,caseVide,caseVide,caseVide,caseTriangleRouge,caseMurHautBas,caseVide])]))     #7		

plaque2 = plaque(np.array([np.array([caseVide,caseVide,caseVide,caseMurDroit,caseVide,caseVide,caseMurBas,caseVide]),
						   np.array([caseMurDroit,caseVide,caseMurBas,caseCarreBleu,caseVide,caseVide,caseVide,caseMurGauche]),
						   np.array([caseMurGauche,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseLosangeJaune,caseMurHaut]),
						   np.array([caseVide,caseTriangleVert,caseMurHaut,caseVide,caseVide,caseVide,caseVide,caseVide]),
						   np.array([caseVide,caseMurGauche,caseVide,caseMurBas,caseVide,caseVide,caseVide,caseVide]),
						   np.array([caseVide,caseMurBas,caseMurHaut,caseVide,caseMurGauche,caseVide,caseVide,caseVide])]))	

plaque3 = plaque(np.array([np.array([caseVide,caseVide,caseMurBas,caseMurHaut,caseVide,caseVide,caseVide,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseVide,caseMurBas,caseLosangeRouge,caseVide,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseVide,caseVide,caseMurGauche,caseVide,caseVide]),
						   np.array([caseVide,caseMurDroit,caseVide,caseVide,caseVide,caseVide,caseCarreVert,caseMurHaut]),
						   np.array([caseVide,caseTriangleJaune,caseMurHaut,caseVide,caseVide,caseVide,caseMurGauche,caseMurDroit]),
						   np.array([caseVide,caseVide,caseMurDroit,caseVide,caseVide,caseVide,caseVide,caseMurGauche]),
						   np.array([caseMurDroit,caseMurBas,caseCercleBleu,caseVide,caseVide,caseVide,caseVide,caseVide]),
						   np.array([caseVide,caseMurHaut,caseVide,caseMurBas,caseMulticouleur,caseVide,caseVide,caseVide])]))

plaque4 = plaque(np.array([np.array([caseVide,caseMurHaut,caseVide,caseVide,caseMurGauche,caseVide,caseVide,caseVide]),
						   np.array([caseMurGauche,caseVide,caseVide,caseCercleJaune,caseMurHaut,caseVide,caseMurDroit,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseMurGauche,caseVide,caseMurBas,caseLosangeVert,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseMurDroit]),
						   np.array([caseVide,caseMurDroit,caseVide,caseVide,caseVide,caseVide,caseVide,caseMurGauche]),
						   np.array([caseVide,casetriangleBleu,caseMurHaut,caseVide,caseVide,caseVide,caseVide,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseVide,caseMurBas,caseCarreRouge,caseVide,caseVide]),
						   np.array([caseVide,caseVide,caseVide,caseMurBas,caseMurHaut,caseMurGauche,caseVide,caseVide])]))