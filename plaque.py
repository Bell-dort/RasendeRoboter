import numby as np
class plaque(object):
	element = ' '
	"""docstring for plaque"""
	def __init__(self, element):
		self.element = element


plaque1 = plaque(np.array([np.array[caseVide,caseVide,caseVide,caseVide,caseMurBas,caseMurHaut,caseMurDroit,caseVide],
						   np.array[caseVide,caseVide,caseVide,caseVide,caseVide,caseMurBas,caseCarreJaune,caseVide],
						   np.array[caseVide,caseVide,caseVide,caseMurBas,caseCercleVert,caseVide,caseVide,caseVide],
						   np.array[caseMurDroit,caseVide,caseVide,caseVide,caseMurGauche,caseVide,caseVide,caseVide],
						   np.array[caseMurGauche,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide],
						   np.array[caseVide,caseVide,caseLosangeBleu,caseVide,caseVide,caseVide,caseVide,caseVide],
						   np.array[caseVide,caseVide,caseMurGauche,caseVide,caseVide,caseMurDroit,caseVide,caseMurDroit],
						   np.array[caseVide,caseVide,caseVide,caseVide,caseVide,caseTriangleRouge,caseMurHautBas,caseCentral]]));		

plaque2 = plaque(np.array([np.array[caseVide,caseVide,caseVide,caseMurDroit,caseVide,caseMurHaut,caseMurBas,caseCentral],
						   np.array[caseMurGauche,caseVide,caseMurBas,caseCarreBleu,caseVide,caseVide,caseVide,caseMurGauche],
						   np.array[caseVide,caseVide,caseVide,caseMurBas,caseCercleVert,caseVide,caseVide,caseVide],
						   np.array[caseMurDroit,caseVide,caseVide,caseVide,caseMurGauche,caseVide,caseVide,caseVide],
						   np.array[caseMurGauche,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide,caseVide],
						   np.array[caseVide,caseVide,caseLosangeBleu,caseVide,caseVide,caseVide,caseVide,caseVide],
						   np.array[caseVide,caseVide,caseMurGauche,caseVide,caseVide,caseMurDroit,caseVide,caseVide],
						   np.array[caseVide,caseVide,caseVide,caseVide,caseVide,caseTriangleRouge,caseVide,caseVide.ToCentre()]]));	