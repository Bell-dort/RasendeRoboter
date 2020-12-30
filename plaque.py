import numpy as np
from case import *


class plaque(object):
    """docstring for plaque"""
    element = np.empty((8, 8), dtype=Case)

    def __init__(self, element):
        self.element = element

    def switch90(self,t):


        if t == 1:
            for i in range(len(listeCasePlaque1)):
                    listeCasePlaque1[i].toDroite()
        if t == 2:
            for i in range(len(listeCasePlaque2)):
                    listeCasePlaque2[i].toDroite()
        if t == 3:
            for i in range(len(listeCasePlaque3)):
                listeCasePlaque3[i].toDroite()
        if t == 4:
            for i in range(len(listeCasePlaque4)):
                    listeCasePlaque4[i].toDroite()
        tableauRemplacant = np.empty((8, 8), dtype=Case)
        for k in range(8):
            for t in range(8):
                tableauRemplacant[k][t] = self.element[k][t]
        for i in range(8):
            for j in range(8):
                self.element[i][j] = tableauRemplacant[7 - j][i]
        return self
plaque1 = plaque(np.array(
    [np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas1, caseMurHaut1,caseMurDroit1, caseVide, caseVide], dtype=Case),  # 0
     np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseMurBas1, caseCarreJaune, caseVide], dtype=Case),  # 1
     np.array([caseVide, caseVide, caseVide, caseMurBas1, caseCercleVert, caseVide, caseVide, caseVide], dtype=Case),  # 2
     np.array([caseMurDroit1, caseVide, caseVide, caseVide, caseMurGauche1, caseVide, caseVide, caseVide], dtype=Case),  # 3
     np.array([caseMurGauche1, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),  # 4
     np.array([caseVide, caseVide, caseLosangeBleu, caseMurHaut1, caseVide, caseVide, caseVide, caseVide], dtype=Case),  # 5
     np.array([caseVide, caseVide, caseMurGauche1, caseVide, caseVide, caseMurDroit1, caseVide, caseVide], dtype=Case),  # 6
     np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseTriangleRouge, caseMurHaut1, caseVide], dtype=Case)], dtype=np.ndarray))  # 7
        #essaie de spécifier les types, ça évite des warning ou erreur ex : np.array([.....], dtype=<type>)

plaque2 = plaque(
    np.array([np.array([caseVide, caseVide, caseVide, caseMurDroit2, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseMurDroit2, caseVide, caseMurBas2, caseCarreBleu, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseMurGauche2, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurDroit2, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseLosangeJaune, caseMurHaut2], dtype=Case),
              np.array([caseVide, caseTriangleVert, caseMurHaut2, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseMurGauche2, caseVide, caseMurBas2, caseMurHautDroit2, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseMurBas2, caseMurHaut2, caseVide, caseMurGauche2, caseVide, caseVide, caseVide], dtype=Case)], dtype=np.ndarray))

plaque3 = plaque(
    np.array([np.array([caseVide, caseVide, caseMurBas3, caseMurHaut3, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas3, caseLosangeRouge, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseMurGauche3, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseMurDroit3, caseVide, caseVide, caseVide, caseVide, caseCarreVert, caseMurHaut3], dtype=Case),
              np.array([caseVide, caseTriangleJaune, caseMurHaut3, caseVide, caseVide, caseVide, caseMurGauche3, caseMurDroit3], dtype=Case),
              np.array([caseVide, caseVide, caseMurDroit3, caseVide, caseVide, caseVide, caseVide, caseMurGauche3], dtype=Case),
              np.array([caseVide, caseMurBas3, caseCercleBleu, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseMurBas3, caseMulticouleur, caseVide, caseVide, caseVide], dtype=Case)], dtype=np.ndarray))

plaque4 = plaque(
    np.array([np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseCercleJaune, caseMurHaut4, caseVide, caseMurDroit4, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseMurGauche4, caseVide, caseMurBas4, caseLosangeVert, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurDroit4], dtype=Case),
              np.array([caseVide, caseMurDroit4, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurGauche4], dtype=Case),
              np.array([caseVide, caseTriangleBleu, caseMurHaut4, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas4, caseCarreRouge, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseMurBas4, caseMurHaut4, caseMurGauche4, caseVide, caseVide], dtype=Case)], dtype=np.ndarray))
