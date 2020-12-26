import mission
from enum import Enum, auto


# je vais surement modifier l'enumération pour en avoir une pour les forme et une pour les couleur
# j'ai mis comme ça pour que ce soit fonctionel, j'optimiserais plus tard
class Mission(Enum):
    vide = auto()
    losangeVert = auto()
    losangeJaune = auto()
    losangeRouge = auto()
    losangeBleu = auto()
    cercleVert = auto()
    cercleJaune = auto()
    cercleRouge = auto()
    cercleBleu = auto()
    carreVert = auto()
    carreJaune = auto()
    carreRouge = auto()
    carreBleu = auto()
    triangleVert = auto()
    triangleJaune = auto()
    triangleRouge = auto()
    triangleBleu = auto()
    multicolore = auto()


class Case(object):
    # Les différents murs
    haut = 0
    bas = 0
    gauche = 0
    droit = 0
    # Contenue de le case =0 si rien
    contenu = 0
    """docstring for Case"""

    def __init__(self, haut, bas, gauche, droit, contenu):  # Constructeur
        self.haut = haut
        self.bas = bas
        self.gauche = gauche
        self.droit = droit
        self.contenu = contenu

    def visuel(self):  # test
        return self.haut

    def toCentre(self):  # Change la case en case centrale
        self.haut = 1
        self.bas = 1
        self.gauche = 1
        self.droit = 1
        self.contenu = 0

    def toVide(self):  # Change la case en case vide
        self.haut = 0
        self.bas = 0
        self.gauche = 0
        self.droit = 0
        self.contenu = 0

    def toDroite(self):  # change l'orientation de la case vers la droite
        changement = self.haut
        self.haut = self.droit
        self.droit = self.bas
        self.bas = self.gauche
        self.gauche = changement

    def toGauche(self):  # change l'orientation de la case vers la gauche
        changement = self.haut
        self.haut = self.gauche
        self.gauche = self.bas
        self.bas = self.droit
        self.droit = changement


caseVide = Case(0, 0, 0, 0, Mission.vide)
caseCentral = Case(1, 1, 1, 1, Mission.vide)
caseMurDroit = Case(0, 0, 0, 1, Mission.vide)
caseMurGauche = Case(0, 0, 1, 0, Mission.vide)
caseMurHaut = Case(1, 0, 0, 0, Mission.vide)
caseMurBas = Case(0, 1, 0, 0, Mission.vide)
caseMurHautBas = Case(1, 1, 0, 0, Mission.vide)
caseMurHautDroit = Case(1, 0, 0, 1, Mission.vide)

caseLosangeBleu = Case(0, 1, 0, 1, Mission.losangeBleu)
caseCercleVert = Case(1, 0, 0, 1, Mission.cercleVert)
caseCarreJaune = Case(1, 0, 1, 0, Mission.carreJaune)
caseTriangleRouge = Case(0, 1, 1, 0, Mission.triangleRouge)

caseTriangleVert = Case(0, 1, 0, 1, Mission.triangleVert)
caseCarreBleu = Case(1, 0, 1, 0, Mission.carreBleu)
caseCercleRouge = Case(1, 0, 0, 1, Mission.cercleRouge)
caseLosangeJaune = Case(0, 1, 1, 0, Mission.losangeJaune)

caseTriangleJaune = Case(0, 1, 1, 0, Mission.triangleJaune)
caseCercleBleu = Case(1, 0, 1, 0, Mission.cercleBleu)
caseLosangeRouge = Case(1, 0, 0, 1, Mission.losangeRouge)
caseCarreVert = Case(0, 1, 0, 1, Mission.carreVert)
caseMulticouleur = Case(1, 0, 0, 1, Mission.multicolore)

caseCercleJaune = Case(0, 1, 0, 1, Mission.cercleJaune)
caseTriangleBleu = Case(0, 1, 1, 0, Mission.triangleBleu)
caseCarreRouge = Case(1, 0, 0, 1, Mission.carreRouge)
caseLosangeVert = Case(1, 0, 1, 0, Mission.losangeVert)
