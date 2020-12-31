import plaque
import random
import numpy as np
from case import *

class plateau():
    liste = [0, 1, 2, 3]
    listePlaque = []
    plat = np.empty((16, 16), dtype=Case)
    nbSwitchPlaque3 = 0
    """docstring for plateau"""
    def elaborationPlateau(self):
        global listeChangement
        listeChangement = [1, 1, 1, 1]
        for i in range(4):

            choix = random.choice(self.liste)
            print(choix)
            self.liste.remove(choix)
            listeChangement[i] = choix
            print(str(listeChangement[0]) + str(listeChangement[1]) + str(listeChangement[2]) + str(listeChangement[3]))

        self.liste = listeChangement

    def __init__(self, plaque1, plaque2, plaque3, plaque4):
        self.nbSwitchPlaque3 = 0
        for i in range(random.randint(0, 3)):
            plaque1.switch90(1)
        for j in range(random.randint(0, 3)):
            plaque2.switch90(2)
        for t in range(random.randint(0, 3)):
            plaque3.switch90(3)
            self.nbSwitchPlaque3 = self.nbSwitchPlaque3 + 1
        for k in range(random.randint(0, 3)):
            plaque4.switch90(4)
        self.listePlaque = [plaque1, plaque2, plaque3, plaque4]
        print(str(self.liste[0]) + str(self.liste[1]) + str(self.liste[2]) + str(self.liste[3]))

        self.elaborationPlateau()
        print(str(self.liste[0]) + str(self.liste[1]) + str(self.liste[2]) + str(self.liste[3]))

        for i in range(8):
            for j in range(8):
                self.plat[i][j] = self.listePlaque[self.liste[0]].element[i][j]
        for i in range(8, 16):
            for j in range(8):
                self.plat[i][j] = self.listePlaque[self.liste[1]].element[i-8][j]
        for i in range(8):
            for j in range(8, 16):
                self.plat[i][j] = self.listePlaque[self.liste[2]].element[i][j-8]
        for i in range(8, 16):
            for j in range(8, 16):
                self.plat[i][j] = self.listePlaque[self.liste[3]].element[i-8][j-8]
#Recherche de la case Multicouleur
        for i in range(8):
            for j in range(8):
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 3:
                    self.plat[i][j+1]= caseMurHaut
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 0:
                    self.plat[i+1][j] = caseMurGauche
        for i in range(8, 16):
            for j in range(8):
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 3:
                    self.plat[i][j+1] = caseMurHaut
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 2:
                    self.plat[i+1][j] = caseMurDroit
        for i in range(8):
            for j in range(8, 16):
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 1:
                    self.plat[i][j+1] = caseMurBas
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 0:
                    self.plat[i+1][j] = caseMurGauche
        for i in range(8, 16):
            for j in range(8, 16):
                if self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 1:
                    self.plat[i][j+1] = caseMurBas
                elif self.plat[i][j] == caseMulticouleur and self.nbSwitchPlaque3 == 2:
                    self.plat[i+1][j] = caseMurDroit
        # Défini les cases centrales au centre du plateau
        for i in range(7, 9):
            for j in range(7, 9):
                self.plat[i][j] = caseCentral
        # Défini les cases autour des cases centrales
        if self.plat[7][6] == caseMurHaut:
            self.plat[7][6] = caseMurHautBas
        else:
            self.plat[7][6] = caseMurBas
        self.plat[6][7] = caseMurDroit
        if self.plat[8][6] == caseMurHaut:
            self.plat[8][6] = caseMurHautBas
        else:
            self.plat[8][6] = caseMurBas
        self.plat[9][7] = caseMurGauche
        self.plat[6][8] = caseMurDroit
        self.plat[7][9] = caseMurHaut
        self.plat[8][9] = caseMurHaut
        self.plat[9][8] = caseMurGauche

    def coordMission(self, mission):
        for i in range(16):
            for j in range(16):
                if self.plat[i][j].mission == mission:
                    return (i,j)

plateauJeu = plateau(plaque.plaque1,plaque.plaque2,plaque.plaque3,plaque.plaque4)