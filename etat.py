from robot import Robot
from copy import copy
import math


class Etat():
    def __init__(self, plateau, robotRouge, robotJaune, robotVert, robotBleu, mission, cost):
        # le plateau actuel et les robots (avec leurs positions)
        self.plateau = plateau
        self.robotRouge = robotRouge
        self.robotJaune = robotJaune
        self.robotVert = robotVert
        self.robotBleu = robotBleu
        self.mission = mission
        self.eucliDist = self.euclideanDistance()
        self.manatDist = self.manatthanDistance()
        self.cost = cost

    def isRobotHere(self, x, y):
        return (self.robotRouge.x == x and self.robotRouge.y == y) or (self.robotJaune.x == x and self.robotJaune.y == y) or \
               (self.robotVert.x == x and self.robotVert.y == y) or (self.robotBleu.x == x and self.robotBleu.y == y)

    def nextState(self):
        list = []
        # toute les position que peux prendre robotRouge
        if not self.plateau.plat[self.robotRouge.x][self.robotRouge.y].gauche and self.robotRouge.x > 0 and not self.isRobotHere(
                self.robotRouge.x-1, self.robotRouge.y):
            list.append(Etat(self.plateau, copy(self.robotRouge).gauche(self), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotRouge.x][self.robotRouge.y].droit and self.robotRouge.x < 15 and not self.isRobotHere(
                self.robotRouge.x+1, self.robotRouge.y):
            list.append(Etat(self.plateau, copy(self.robotRouge).droite(self), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotRouge.x][self.robotRouge.y].haut and self.robotRouge.y > 0 and not self.isRobotHere(
                self.robotRouge.x, self.robotRouge.y-1):
            list.append(Etat(self.plateau, copy(self.robotRouge).haut(self), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotRouge.x][self.robotRouge.y].bas and self.robotRouge.y < 15 and not self.isRobotHere(
                self.robotRouge.x, self.robotRouge.y+1):
            list.append(Etat(self.plateau, copy(self.robotRouge).bas(self), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))

        # toute les position que peux prendre robotJaune
        if not self.plateau.plat[self.robotJaune.x][self.robotJaune.y].gauche and self.robotJaune.x > 0 and not self.isRobotHere(
                self.robotJaune.x - 1, self.robotJaune.y):
            list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).gauche(self), self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))
        if not  self.plateau.plat[self.robotJaune.x][self.robotJaune.y].droit and self.robotJaune.x < 15 and not self.isRobotHere(
                self.robotJaune.x + 1, self.robotJaune.y):
            list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).droite(self), self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotJaune.x][self.robotJaune.y].haut and self.robotJaune.y > 0 and not self.isRobotHere(
                self.robotJaune.x, self.robotJaune.y - 1):
            list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).haut(self), self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotJaune.x][self.robotJaune.y].bas and self.robotJaune.y < 15 and not self.isRobotHere(
                self.robotJaune.x, self.robotJaune.y + 1):
            list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).bas(self), self.robotVert,
                         self.robotBleu, self.mission, self.cost + 1))

        # toute les position que peux prendre robotVert
        if not self.plateau.plat[self.robotVert.x][self.robotVert.y].gauche and self.robotVert.x > 0 and not self.isRobotHere(
                self.robotVert.x - 1, self.robotVert.y):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).gauche(self),
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotVert.x][self.robotVert.y].droit and self.robotVert.x < 15 and not self.isRobotHere(
                self.robotVert.x + 1, self.robotVert.y):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).droite(self),
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotVert.x][self.robotVert.y].haut and self.robotVert.y > 0 and not self.isRobotHere(
                self.robotVert.x, self.robotVert.y - 1):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).haut(self),
                         self.robotBleu, self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotVert.x][self.robotVert.y].bas and self.robotVert.y < 15 and not self.isRobotHere(
                self.robotVert.x, self.robotVert.y + 1):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).bas(self),
                         self.robotBleu, self.mission, self.cost + 1))

        # toute les position que peux prendre robotBleu
        if not self.plateau.plat[self.robotBleu.x][self.robotBleu.y].gauche and self.robotBleu.x > 0 and not self.isRobotHere(
                self.robotBleu.x - 1, self.robotBleu.y):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).gauche(self), self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotBleu.x][self.robotBleu.y].droit and self.robotBleu.x < 15 and not self.isRobotHere(
                self.robotBleu.x + 1, self.robotBleu.y):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).droite(self), self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotBleu.x][self.robotBleu.y].haut and self.robotBleu.y > 0 and not self.isRobotHere(
                self.robotBleu.x, self.robotBleu.y - 1):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).haut(self), self.mission, self.cost + 1))
        if not self.plateau.plat[self.robotBleu.x][self.robotBleu.y].bas and self.robotBleu.y < 15 and not self.isRobotHere(
                self.robotBleu.x, self.robotBleu.y + 1):
            list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).bas(self), self.mission, self.cost + 1))

        return list

    def isFinalState(self):
        coord = self.plateau.coordMission(self.mission)
        if self.mission.couleur == "red":
            return (self.robotRouge.x, self.robotRouge.y) == coord
        elif self.mission.couleur == "yellow":
            return (self.robotJaune.x, self.robotJaune.y) == coord
        elif self.mission.couleur == "green":
            return (self.robotVert.x, self.robotVert.y) == coord
        elif self.mission.couleur == "blue":
            return (self.robotBleu.x, self.robotBleu.y) == coord
        elif self.mission.couleur == "multicolore":
            return (self.robotRouge.x, self.robotRouge.y) == coord or (self.robotBleu.x, self.robotBleu.y) == coord or \
                   (self.robotJaune.x, self.robotJaune.y) == coord or (self.robotVert.x, self.robotVert.y) == coord

    def euclideanDistance(self):
        coord = self.plateau.coordMission(self.mission)
        if self.mission.couleur == "red":
            return math.sqrt(math.pow(coord[0] - self.robotRouge.x, 2) + math.pow(coord[1] - self.robotRouge.y, 2))
        elif self.mission.couleur == "yellow":
            return math.sqrt(math.pow(coord[0] - self.robotJaune.x, 2) + math.pow(coord[1] - self.robotJaune.y, 2))
        elif self.mission.couleur == "green":
            return math.sqrt(math.pow(coord[0] - self.robotVert.x, 2) + math.pow(coord[1] - self.robotVert.y, 2))
        elif self.mission.couleur == "blue":
            return math.sqrt(math.pow(coord[0] - self.robotBleu.x, 2) + math.pow(coord[1] - self.robotBleu.y, 2))
        elif self.mission.couleur == "multicolore":
            return min(math.sqrt(math.pow(coord[0] - self.robotRouge.x, 2) + math.pow(coord[1] - self.robotRouge.y, 2)),
                       math.sqrt(math.pow(coord[0] - self.robotJaune.x, 2) + math.pow(coord[1] - self.robotJaune.y, 2)),
                       math.sqrt(math.pow(coord[0] - self.robotVert.x, 2) + math.pow(coord[1] - self.robotVert.y, 2)),
                       math.sqrt(math.pow(coord[0] - self.robotBleu.x, 2) + math.pow(coord[1] - self.robotBleu.y, 2)))

    def manatthanDistance(self):
        coord = self.plateau.coordMission(self.mission)
        if self.mission.couleur == "red":
            return abs(coord[0] - self.robotRouge.x) + abs(coord[1] - self.robotRouge.y)
        elif self.mission.couleur == "yellow":
            return abs(coord[0] - self.robotJaune.x) + abs(coord[1] - self.robotJaune.y)
        elif self.mission.couleur == "green":
            return abs(coord[0] - self.robotVert.x) + abs(coord[1] - self.robotVert.y)
        elif self.mission.couleur == "blue":
            return abs(coord[0] - self.robotBleu.x) + abs(coord[1] - self.robotBleu.y)
        elif self.mission.couleur == "multicolore":
            return min(abs(coord[0] - self.robotRouge.x) + abs(coord[1] - self.robotRouge.y),
                       abs(coord[0] - self.robotJaune.x) + abs(coord[1] - self.robotJaune.y),
                       abs(coord[0] - self.robotVert.x) + abs(coord[1] - self.robotVert.y),
                       abs(coord[0] - self.robotBleu.x) + abs(coord[1] - self.robotBleu.y))


    def toString(self):
        return "cout : {}  heuristique : {}\n            : x  y \nRobot Rouge : {},{}\nRobot Jaune : {},{}\nRobot Vert  : {},{}\nRobot Bleu  : {},{}"\
            .format(self.cost, self.manatDist, self.robotRouge.x, self.robotRouge.y, self.robotJaune.x, self.robotJaune.y, self.robotVert.x, self.robotVert.y, self.robotBleu.x, self.robotBleu.y)