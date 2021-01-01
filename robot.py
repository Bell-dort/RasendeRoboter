import plateau
import random

class Robot() :

    def __init__(self, x, y, couleur, plateau): #un robot est defini par sa couleur et sa position
        self.x = x
        self.y = y
        self.couleur = couleur
        self.plateau = plateau

    #tout les déplacement possible du robot
    #il s'arrete s'il trouve un mur ou le bord du terrain
    def gauche(self, state):
        while not self.plateau.plat[self.x][self.y].gauche and self.x > 0 and not state.isRobotHere(self.x-1, self.y):
            self.x -= 1
        return self

    def droite(self, state):
        while not self.plateau.plat[self.x][self.y].droit and self.x < 15 and not state.isRobotHere(self.x+1,self.y):
            self.x += 1
        return self

    def haut(self, state):

        while not self.plateau.plat[self.x][self.y].haut and self.y > 0 and not state.isRobotHere(self.x, self.y-1):
            self.y -= 1
        return self

    def bas(self, state):
        while not self.plateau.plat[self.x][self.y].bas and self.y < 15 and not state.isRobotHere(self.x, self.y+1):
            self.y += 1
        return self




#on créé les 4 robots et on les positionne à des endroit alléatoire

xR = random.randint(0, 15)
yR = random.randint(0, 15)
robotRouge = Robot(xR, yR, "red", plateau.plateauJeu)

xB = random.randint(0, 15)
yB = random.randint(0, 15)
while(xB==xR and yB==yR):
    xB = random.randint(0, 15)
    yB = random.randint(0, 15)
robotBleu = Robot(xB, yB, "blue", plateau.plateauJeu)

xV = random.randint(0, 15)
yV = random.randint(0, 15)
while(xV==xR and yV==yR or xV==xB and yV==yB):
    xV = random.randint(0, 15)
    yV = random.randint(0, 15)

robotVert = Robot(xV, yV, "green", plateau.plateauJeu)

xJ = random.randint(0, 15)
yJ = random.randint(0, 15)
while(xJ==xR and yJ==yR or xJ==xB and yJ==yB or xJ==xV and yJ==yV):
    xJ = random.randint(0, 15)
    yJ = random.randint(0, 15)

robotJaune = Robot(xJ, yJ, "yellow", plateau.plateauJeu)

#----------------------pour les test------------------------
# robotRouge = Robot(10, 10, "red", plateau.plateauJeu)
# robotBleu = Robot(12, 10, "blue", plateau.plateauJeu)
# robotVert = Robot(8, 10, "green", plateau.plateauJeu)
# robotJaune = Robot(0, 0, "yellow", plateau.plateauJeu)