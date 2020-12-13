import mission

class case(object):
	#Les différents murs
	haut = 0
	bas = 0
	gauche = 0
	droit = 0
	#Contenue de le case =0 si rien 
	contenu = 0
	"""docstring for Case"""
	def __init__(self, haut, bas, gauche, droit, contenu): #Constructeur
		self.haut = haut
		self.bas = bas
		self.gauche = gauche
		self.droit = droit
		self.contenu = contenu

	def visuel(self): #test
		return self.haut 

	def toCentre(self):#Change la case en case centrale
		self.haut = 1
		self.bas = 1
		self.gauche = 1
		self.droit = 1
		self.contenu = 0

	def toVide(self):#Change la case en case vide
		self.haut = 0
		self.bas = 0
		self.gauche = 0
		self.droit = 0
		self.contenu = 0
	def toDroite(self):#change l'orientation de la case vers la droite
		changement = ' '
		changement = self.haut
		self.haut = self.droit
		self.droit = self.bas
		self.bas = self.gauche
		self.gauche = changement

	def toGauche(self):#change l'orientation de la case vers la gauche
		changement = ' '
		changement = self.haut
		self.haut = self.gauche
		self.gauche = self.bas
		self.bas = self.droit
		self.droit = changement
caseVide = case(0,0,0,0,0)
caseCentral = case(1,1,1,1,0)
caseMurDroit = case(0,0,0,1,0)
caseMurGauche = case(0,0,1,0,0)
caseMurHaut = case(1,0,0,0,0)
caseMurBas = case(0,1,0,0,0)

caseLosangeBleu = case(0,1,0,1,losangeBleu)
caseCercleVert = case(1,0,0,1,cercleVert)
caseCarreJaune = case(1,0,1,0,carreJaune)
caseTriangleRouge = case(0,1,1,0,triangleRouge)

caseTriangleVert = case(0,1,0,1,triangleVert)
caseCarreBleu = case(1,0,1,0,carreBleu)
caseCercleRouge = case(1,0,0,1,cercleRouge)
caseLosangeJaune = case(0,1,1,0,losangeJaune)

caseTriangleJaune = case(0,1,1,0,triangleJaune)
caseCercleBleu = case(1,0,1,0,cercleBleu)
caseLosangeRouge = case(1,0,0,1,losangeRouge)
caseCarreVert = case(0,1,0,1,carreVert)
caseMulticouleur = case(1,0,0,1,multiCouleur)

caseCercleJaune = case(0,1,0,1,cercleJaune)
caseTriangleBleu = case(0,1,1,0,triangleBleu)
caseCarreRouge = case(1,0,0,1,carreRouge)
caseLosangeVert = case(1,0,1,0,losangeVert)