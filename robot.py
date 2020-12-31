import plateau
class Robot() :

    def __init__(self, x, y, couleur, plateau): #un robot est defini par sa couleur et sa position
        self.x = x
        self.y = y
        self.couleur = couleur
        self.plateau = plateau

    #tout les déplacement possible du robot
    #il s'arrete s'il trouve un mur ou le bord du terrain
    def gauche(self):
        while not self.plateau.plat[self.x][self.y].gauche and self.x > 0 and not isRobotHere(self.x-1, self.y):
            self.x -= 1
        return self

    def droite(self):
        while not self.plateau.plat[self.x][self.y].droit and self.x < 15 and not isRobotHere(self.x+1,self.y):
            self.x += 1
        return self

    def haut(self):

        while not self.plateau.plat[self.x][self.y].haut and self.y > 0 and not isRobotHere(self.x, self.y-1):
            self.y -= 1
        return self

    def bas(self):
        while not self.plateau.plat[self.x][self.y].bas and self.y < 15 and not isRobotHere(self.x, self.y+1):
            self.y += 1
        return self

def isRobotHere(x, y):
    return (robotRouge.x == x and robotRouge.y == y) or (robotJaune.x == x and robotJaune.y == y) or \
           (robotVert.x == x and robotVert.y == y) or (robotBleu.x == x and robotBleu.y == y)

#on créé les 4 robots et on les positionne à des endroit alléatoire
#(pour l'instant ils sont définis mais c'est pour les test)
robotRouge = Robot(1, 10, "red", plateau.plateauJeu)
robotBleu = Robot(15, 15, "blue", plateau.plateauJeu)
robotVert = Robot(1, 5, "green", plateau.plateauJeu)
robotJaune = Robot(15, 1, "yellow", plateau.plateauJeu)

