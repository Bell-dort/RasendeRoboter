import numpy as np
from case import *


class plaque(object):
    """docstring for plaque"""
    element = np.empty((8, 8), dtype=Case)

    def __init__(self, element):
        self.element = element

    def switch90(self):
        tableauRemplacant = np.empty((8, 8), dtype=Case)
        for k in range(8):
            for t in range(8):
                tableauRemplacant[k][t] = self.element[k][t]
        for i in range(8):
            for j in range(8):
                self.element[i][j] = tableauRemplacant[7 - j][i]
                # Choisi entre tourner a droite ou a gauche si plus de 1 mur jsp pourquoi mais c'est comme ça
                if self.element[i][j].haut + self.element[i][j].bas + self.element[i][j].droit + self.element[i][j].gauche > 1 :
                    self.element[i][j].toDroite()
                else:
                    self.element[i][j].toGauche()
        return self
plaque1 = plaque(np.array(
    [np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas, caseMurHaut, caseMurDroit, caseVide, caseVide], dtype=Case),  # 0
     np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseMurBas, caseCarreJaune, caseVide], dtype=Case),  # 1
     np.array([caseVide, caseVide, caseVide, caseMurBas, caseCercleVert, caseVide, caseVide, caseVide], dtype=Case),  # 2
     np.array([caseMurDroit, caseVide, caseVide, caseVide, caseMurGauche, caseVide, caseVide, caseVide], dtype=Case),  # 3
     np.array([caseMurGauche, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),  # 4
     np.array([caseVide, caseVide, caseLosangeBleu, caseMurHaut, caseVide, caseVide, caseVide, caseVide], dtype=Case),  # 5
     np.array([caseVide, caseVide, caseMurGauche, caseVide, caseVide, caseMurDroit, caseVide, caseVide], dtype=Case),  # 6
     np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseTriangleRouge, caseMurHaut, caseVide], dtype=Case)], dtype=np.ndarray))  # 7
        #essaie de spécifier les types, ça évite des warning ou erreur ex : np.array([.....], dtype=<type>)


plaque2 = plaque(
    np.array([np.array([caseVide, caseVide, caseVide, caseMurDroit, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseMurDroit, caseVide, caseMurBas, caseCarreBleu, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseMurGauche, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurDroit, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseLosangeJaune, caseMurHaut], dtype=Case),
              np.array([caseVide, caseTriangleVert, caseMurHaut, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseMurGauche, caseVide, caseMurBas, caseMurHautDroit, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseMurBas, caseMurHaut, caseVide, caseMurGauche, caseVide, caseVide, caseVide], dtype=Case)], dtype=np.ndarray))

plaque3 = plaque(
    np.array([np.array([caseVide, caseVide, caseMurBas, caseMurHaut, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas, caseLosangeRouge, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseMurGauche, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseMurDroit, caseVide, caseVide, caseVide, caseVide, caseCarreVert, caseMurHaut], dtype=Case),
              np.array([caseVide, caseTriangleJaune, caseMurHaut, caseVide, caseVide, caseVide, caseMurGauche,caseMurDroit], dtype=Case),
              np.array([caseVide, caseVide, caseMurDroit, caseVide, caseVide, caseVide, caseVide, caseMurGauche], dtype=Case),
              np.array([caseVide, caseMurBas, caseCercleBleu, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseMurBas, caseMulticouleur, caseVide, caseVide, caseVide], dtype=Case)], dtype=np.ndarray))

plaque4 = plaque(
    np.array([np.array([caseVide, caseVide, caseVide, caseVide, caseMurGauche, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseCercleJaune, caseMurHaut, caseVide, caseMurDroit, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseMurGauche, caseVide, caseMurBas, caseLosangeVert, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurDroit], dtype=Case),
              np.array([caseVide, caseMurDroit, caseVide, caseVide, caseVide, caseVide, caseVide, caseMurGauche], dtype=Case),
              np.array([caseVide, caseTriangleBleu, caseMurHaut, caseVide, caseVide, caseVide, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseVide, caseMurBas, caseCarreRouge, caseVide, caseVide], dtype=Case),
              np.array([caseVide, caseVide, caseVide, caseMurBas, caseMurHaut, caseMurGauche, caseVide, caseVide], dtype=Case)], dtype=np.ndarray))
