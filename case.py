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
        return self

    def toVide(self):  # Change la case en case vide
        self.haut = 0
        self.bas = 0
        self.gauche = 0
        self.droit = 0
        self.contenu = 0
        return self

    def toDroite(self):  # change l'orientation de la case vers la droite
        changement = self.haut
        self.haut = self.droit
        self.droit = self.bas
        self.bas = self.gauche
        self.gauche = changement
        return self

    def toGauche(self):  # change l'orientation de la case vers la gauche
        changement = self.haut
        self.haut = self.gauche
        self.gauche = self.bas
        self.bas = self.droit
        self.droit = changement
        return self

#Case pour la plaque 1
caseMurDroit1 = Case(0, 0, 0, 1, Mission.vide)
caseMurGauche1 = Case(0, 0, 1, 0, Mission.vide)
caseMurHaut1 = Case(1, 0, 0, 0, Mission.vide)
caseMurBas1 = Case(0, 1, 0, 0, Mission.vide)
caseMurHautBas1 = Case(1, 1, 0, 0, Mission.vide)
caseMurHautDroit1 = Case(1, 0, 0, 1, Mission.vide)
caseLosangeBleu = Case(0, 1, 0, 1, Mission.losangeBleu)
caseCercleVert = Case(1, 0, 0, 1, Mission.cercleVert)
caseCarreJaune = Case(1, 0, 1, 0, Mission.carreJaune)
caseTriangleRouge = Case(0, 1, 1, 0, Mission.triangleRouge)

listeCasePlaque1 = [caseMurHautDroit1,caseMurHaut1,caseMurHautBas1,caseMurBas1,caseMurDroit1,caseMurGauche1,caseLosangeBleu,caseCarreJaune,caseTriangleRouge,caseCercleVert]

#Case pour la plaque 2
caseMurDroit2 = Case(0, 0, 0, 1, Mission.vide)
caseMurGauche2 = Case(0, 0, 1, 0, Mission.vide)
caseMurHaut2 = Case(1, 0, 0, 0, Mission.vide)
caseMurBas2 = Case(0, 1, 0, 0, Mission.vide)
caseMurHautBas2 = Case(1, 1, 0, 0, Mission.vide)
caseMurHautDroit2 = Case(1, 0, 0, 1, Mission.vide)
caseTriangleVert = Case(0, 1, 0, 1, Mission.triangleVert)
caseCarreBleu = Case(1, 0, 1, 0, Mission.carreBleu)
caseCercleRouge = Case(1, 0, 0, 1, Mission.cercleRouge)
caseLosangeJaune = Case(0, 1, 1, 0, Mission.losangeJaune)

listeCasePlaque2 = [caseMurHautDroit2,caseMurHaut2,caseMurHautBas2,caseMurBas2,caseMurDroit2,caseMurGauche2,caseLosangeJaune,caseCarreBleu,caseTriangleVert,caseCercleRouge]

#Case pour la plaque 3
caseMurDroit3 = Case(0, 0, 0, 1, Mission.vide)
caseMurGauche3 = Case(0, 0, 1, 0, Mission.vide)
caseMurHaut3 = Case(1, 0, 0, 0, Mission.vide)
caseMurBas3 = Case(0, 1, 0, 0, Mission.vide)
caseMurHautBas3 = Case(1, 1, 0, 0, Mission.vide)
caseMurHautDroit3 = Case(1, 0, 0, 1, Mission.vide)
caseTriangleJaune = Case(0, 1, 1, 0, Mission.triangleJaune)
caseCercleBleu = Case(1, 0, 1, 0, Mission.cercleBleu)
caseLosangeRouge = Case(1, 0, 0, 1, Mission.losangeRouge)
caseCarreVert = Case(0, 1, 0, 1, Mission.carreVert)
caseMulticouleur = Case(1, 0, 0, 1, Mission.multicolore)

listeCasePlaque3 = [caseMurHautDroit3,caseMurHaut3,caseMurHautBas3,caseMurBas3,caseMurDroit3,caseMurGauche3,caseLosangeRouge,caseCarreVert,caseTriangleJaune,caseCercleBleu,caseMulticouleur]

#Case pour la plaque 4
caseMurDroit4 = Case(0, 0, 0, 1, Mission.vide)
caseMurGauche4 = Case(0, 0, 1, 0, Mission.vide)
caseMurHaut4 = Case(1, 0, 0, 0, Mission.vide)
caseMurBas4 = Case(0, 1, 0, 0, Mission.vide)
caseMurHautBas4 = Case(1, 1, 0, 0, Mission.vide)
caseMurHautDroit4 = Case(1, 0, 0, 1, Mission.vide)
caseCercleJaune = Case(0, 1, 0, 1, Mission.cercleJaune)
caseTriangleBleu = Case(0, 1, 1, 0, Mission.triangleBleu)
caseCarreRouge = Case(1, 0, 0, 1, Mission.carreRouge)
caseLosangeVert = Case(1, 0, 1, 0, Mission.losangeVert)

listeCasePlaque4 = [caseMurHautDroit4,caseMurHaut4,caseMurHautBas4,caseMurBas4,caseMurDroit4,caseMurGauche4,caseLosangeVert,caseCarreRouge,caseTriangleBleu,caseCercleJaune]

caseVide = Case(0, 0, 0, 0, Mission.vide)
caseCentral = Case(1, 1, 1, 1, Mission.vide)
caseMurDroit = Case(0, 0, 0, 1, Mission.vide)
caseMurGauche = Case(0, 0, 1, 0, Mission.vide)
caseMurHaut = Case(1, 0, 0, 0, Mission.vide)
caseMurBas = Case(0, 1, 0, 0, Mission.vide)
caseMurHautBas = Case(1, 1, 0, 0, Mission.vide)
caseMurHautDroit = Case(1, 0, 0, 1, Mission.vide)
#listeCaseDePlaque = [listeCasePlaque1,listeCasePlaque2,listeCasePlaque3,listeCasePlaque4]






