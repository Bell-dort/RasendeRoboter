import numpy as np
from case import *


class plaque(object):
    """docstring for plaque"""

    def __init__(self, element):
        self.element = element

    def switch90(self):
        #---------------non nécessaire vu que tu change directement les attributs avec toGauche()----------
        # tableauRemplacant = np.empty((8, 8), dtype=Case)      #comment créer un tableau numpy vide
        #
        # for k in range(8):
        #     for t in range(8):
        #         tableauRemplacant[k][t] = self.element[k][t]
        for i in range(8):
            for j in range(8):
                self.element[i][j].toGauche()


plaque1 = plaque(np.array(
    [np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas, caseMurHaut, caseMurDroit, caseVide, caseVide], dtype=Case),  # 0
     np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseMurBas, caseCarreJaune, caseVide], dtype=Case),  # 1
     np.array([caseVide, caseVide, caseVide, caseMurBas, caseCercleVert, caseVide, caseVide, caseVide], dtype=Case),  # 2
     np.array([caseMurDroit, caseVide, caseVide, caseVide, caseMurGauche, caseVide, caseVide, caseVide], dtype=Case),  # 3
     np.array([caseMurGauche, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),  # 4
     np.array([caseVide, caseVide, caseLosangeBleu, caseMurHaut, caseVide, caseVide, caseVide, caseVide], dtype=Case),  # 5
     np.array([caseVide, caseVide, caseMurGauche, caseVide, caseVide, caseMurDroit, caseVide, caseMurDroit], dtype=Case),  # 6
     np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseTriangleRouge, caseMurHautBas, caseVide], dtype=Case)], dtype=np.ndarray))  # 7
        #essaie de spécifier les types, ça évite des warning ou erreur ex : np.array([.....], dtype=<type>)


plaque2 = plaque(
    np.array([np.array([caseVide, caseVide, caseVide, caseMurDroit, caseVide, caseVide, caseMurBas, caseVide]),
              np.array(
                  [caseMurDroit, caseVide, caseMurBas, caseCarreBleu, caseVide, caseVide, caseVide, caseMurGauche]),
              np.array([caseMurGauche, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurDroit, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseLosangeJaune, caseMurHaut]),
              np.array([caseVide, caseTriangleVert, caseMurHaut, caseVide, caseVide, caseVide, caseVide, caseVide]),
              np.array([caseVide, caseMurGauche, caseVide, caseMurBas, caseMurHautDroit, caseVide, caseVide, caseVide]),
              np.array([caseVide, caseMurBas, caseMurHaut, caseVide, caseMurGauche, caseVide, caseVide, caseVide])]))

plaque3 = plaque(
    np.array([np.array([caseVide, caseVide, caseMurBas, caseMurHaut, caseVide, caseVide, caseVide, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas, caseLosangeRouge, caseVide, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseMurGauche, caseVide, caseVide]),
              np.array([caseVide, caseMurDroit, caseVide, caseVide, caseVide, caseVide, caseCarreVert, caseMurHaut]),
              np.array([caseVide, caseTriangleJaune, caseMurHaut, caseVide, caseVide, caseVide, caseMurGauche,
                        caseMurDroit]),
              np.array([caseVide, caseVide, caseMurDroit, caseVide, caseVide, caseVide, caseVide, caseMurGauche]),
              np.array([caseMurDroit, caseMurBas, caseCercleBleu, caseVide, caseVide, caseVide, caseVide, caseVide]),
              np.array([caseVide, caseMurHaut, caseVide, caseMurBas, caseMulticouleur, caseVide, caseVide, caseVide])]))

plaque4 = plaque(
    np.array([np.array([caseVide, caseMurHaut, caseVide, caseVide, caseMurGauche, caseVide, caseVide, caseVide]),
              np.array(
                  [caseMurGauche, caseVide, caseVide, caseCercleJaune, caseMurHaut, caseVide, caseMurDroit, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseMurGauche, caseVide, caseMurBas, caseLosangeVert, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurDroit]),
              np.array([caseVide, caseMurDroit, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurGauche]),
              np.array([caseVide, caseTriangleBleu, caseMurHaut, caseVide, caseVide, caseVide, caseVide, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas, caseCarreRouge, caseVide, caseVide]),
              np.array([caseVide, caseVide, caseVide, caseMurBas, caseMurHaut, caseMurGauche, caseVide, caseVide])]))
