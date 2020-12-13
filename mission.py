class mission(object):
	couleur = ' '
	symbole = ' '
	"""docstring for mission"""
	def __init__(self, couleur, symbole): #constructeur mission
		self.couleur = couleur
		self.symbole = symbole

	def accessContenu(self):
		return self.symbole + " " + self.couleur

triangleRouge = mission("rouge", "triangle")
triangleBleu = mission("bleu", "triangle")
triangleVert = mission("vert", "triangle")
triangleJaune = mission("jaune", "triangle")

cercleRouge = mission("rouge", "cercle")
cercleBleu = mission("bleu", "cercle")
cercleVert = mission("vert", "cercle")
cercleJaune = mission("jaune", "cercle")

carreRouge = mission("rouge", "carre")
carreBleu = mission("bleu", "carre")
carreVert = mission("vert", "carre")
carreJaune = mission("jaune", "carre")

losangeRouge = mission("rouge", "losange")
losangeBleu = mission("bleu", "losange")
losangeVert = mission("vert", "losange")
losangeJaune = mission("jaune", "losange")

multiCouleur = mission("multicouleur", " ")