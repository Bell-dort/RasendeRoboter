import tkinter
import numpy as np
import mission
import plaque
import plateau
from robot import *
# Fenetre principale
window = tkinter.Tk()
window.wm_minsize(500, 500)

fenetre = tkinter.Frame(window)  # crée une sous-fenetre dans la fentre


class DrawCase(tkinter.Canvas):  # classe DrawCase dérivée de Canvas (permet de créer l'affichage des case)
    # parametres des cases
    wallColor = "grey"
    wallSize = 5
    caseColor = "#CFC1B0"
    caseSize = 40

    def __init__(self, master, case):
        super(DrawCase, self).__init__(master, bd=-2, width=self.caseSize,
                                       height=self.caseSize)  # créé un canvas (élément de dessin)
        self.create_rectangle(0, 0, self.caseSize - 1, self.caseSize - 1,
                              fill=self.caseColor)  # créé un rectangle qui rempli le canvas*
        self.case = case
        # ajoute les murs en fonction des cases
        if case.haut:
            self.create_rectangle(0, 0, self.caseSize - 1, self.wallSize, fill=self.wallColor)
        if case.bas:
            self.create_rectangle(0, self.caseSize - 1 - self.wallSize, self.caseSize - 1, self.caseSize - 1,
                                  fill=self.wallColor)
        if case.droit:
            self.create_rectangle(self.caseSize - 1 - self.wallSize, 0, self.caseSize - 1, self.caseSize - 1,
                                  fill=self.wallColor)
        if case.gauche:
            self.create_rectangle(0, 0, self.wallSize, self.caseSize - 1, fill=self.wallColor)



    def drawRobot(self, robot):
        self.create_oval(self.caseSize/3, self.caseSize/5, 2*self.caseSize/3, self.caseSize/2, fill=robot.couleur)
        self.create_oval(self.caseSize / 4, self.caseSize / 3, 3*self.caseSize / 4, 3*self.caseSize / 4,
                         fill=robot.couleur, outline="")
    def draw(self):
        missionCase = self.case.mission
        if missionCase != mission.vide:
            if missionCase.symbole == "triangle":
                self.create_polygon(self.caseSize / 4, 3 * self.caseSize / 4, self.caseSize / 2, self.caseSize / 4,
                                    3 * self.caseSize / 4, 3 * self.caseSize / 4, fill=missionCase.couleur)
            elif missionCase.symbole == "carre":
                self.create_rectangle(self.caseSize / 4, self.caseSize / 4, 3 * self.caseSize / 4,
                                      3 * self.caseSize / 4, fill=missionCase.couleur, outline="")
            elif missionCase.symbole == "losange":
                self.create_polygon(self.caseSize / 2, self.caseSize / 4, 3 * self.caseSize / 4, self.caseSize / 2,
                                    self.caseSize / 2, 3 * self.caseSize / 4, self.caseSize / 4, self.caseSize / 2,
                                    fill=missionCase.couleur)
            elif missionCase.symbole == "cercle":
                self.create_oval(self.caseSize / 4, self.caseSize / 4, 3 * self.caseSize / 4,
                                 3 * self.caseSize / 4, fill=missionCase.couleur, outline="")
            else :
                self.create_rectangle(self.wallSize+1, self.wallSize+1, self.caseSize/2, self.caseSize/2, fill="red", outline="")
                self.create_rectangle(self.caseSize / 2, self.wallSize+1, self.caseSize - (self.wallSize+1), self.caseSize / 2, fill="yellow",
                                      outline="")
                self.create_rectangle(self.caseSize/2, self.caseSize/2, self.caseSize - (self.wallSize + 1), self.caseSize - (self.wallSize+1), fill="green",
                                      outline="")
                self.create_rectangle(self.wallSize+1, self.caseSize/2, self.caseSize / 2, self.caseSize - (self.wallSize+1), fill="blue",
                                      outline="")


# -----------------affichage de chaque case---------------------------
drawnCase = np.empty((16, 16), dtype=DrawCase)

# for i in range(0, 8):
#     for j in range(0, 8):
#         DrawCase(fenetre, plaque.plaque4.element[j][i]).grid(row=i, column=j)


for i in range(0, 16):
    for j in range(0, 16):
        drawnCase[j][i] = DrawCase(fenetre, plateau.plateauJeu.plat[j][i])
        drawnCase[j][i].draw()
        drawnCase[j][i].grid(row=i, column=j)

#-------------------affichage des robots---------------------
drawnCase[robotRouge.x][robotRouge.y].drawRobot(robotRouge)
drawnCase[robotJaune.x][robotJaune.y].drawRobot(robotJaune)
drawnCase[robotVert.x][robotVert.y].drawRobot(robotVert)
drawnCase[robotBleu.x][robotBleu.y].drawRobot(robotBleu)


fenetre.pack(expand=True)