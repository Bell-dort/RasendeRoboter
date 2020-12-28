from plaque import *
import random


class plateau():
    liste = [0, 1, 2, 3]
    listePlaque = []
    plat = np.empty((16, 16), dtype=Case)
    nbSwitchPlaque3 = 0
    """docstring for plateau"""
    def elaborationPlateau(L):
        global listeChangement
        for i in range(4):
            listeChangement = []
            choix = random.choice(L)
            del L[choix]
            listeChangement[i] = choix
        L = listeChangement

    def __init__(self, plaque1, plaque2, plaque3, plaque4):
        self.nbSwitchPlaque3 = 0
        for i in range(np.randint(0, 3)):
            plaque1.switch90()
        for j in range(np.randint(0, 3)):
            plaque2.switch90()
        for t in range(np.randint(0, 3)):
            plaque3.switch90()
            self.nbSwitchPlaque3 = self.nbSwitchPlaque3 + 1
        for k in range(np.randint(0, 3)):
            plaque4.switch90()
        self.listePlaque = [plaque1, plaque2, plaque3, plaque4]
        self.elaborationPlateau(self.liste)
        for i in range(8):
            for j in range(8):
                self.plat[i][j] = (self.listePlaque[self.liste[0]])[i][j]
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 3:
                    self.plat[i][j+1].haut = 1
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 0:
                    self.plat[i+1][j].gauche = 1
        for i in range(8, 16):
            for j in range(8):
                self.plat[i][j] = (self.listePlaque[self.liste[1]])[i][j]
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 3:
                    self.plat[i][j+1].haut = 1
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 2:
                    self.plat[i+1][j].droit = 1
        for i in range(8):
            for j in range(8, 16):
                self.plat[i][j] = (self.listePlaque[self.liste[2]])[i][j]
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 1:
                    self.plat[i][j+1].bas = 1
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 0:
                    self.plat[i+1][j].gauche = 1
        for i in range(8, 16):
            for j in range(8, 16):
                self.plat[i][j] = (self.listePlaque[self.liste[3]])[i][j]
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 1:
                    self.plat[i][j+1].bas = 1
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 2:
                    self.plat[i+1][j].droit = 1
        # Défini les cases centrales au centre du plateau
        for i in range(7, 8):
            for j in range(7, 8):
                self.plat[i][j] = caseCentral
        # Défini les cases autour des cases centrales
        self.element[7][6] = caseMurHautBas
        self.element[6][7] = caseMurDroit
        self.element[8][6] = caseMurBas
        self.element[9][7] = caseMurGauche
        self.element[6][8] = caseMurDroit
        self.element[7][9] = caseMurHaut
        self.element[8][9] = caseMurHaut
        self.element[9][8] = caseMurGauche
