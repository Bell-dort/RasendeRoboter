from robot import Robot
from copy import copy
import math


class Etat():
    def __init__(self, plateau, robotRouge, robotJaune, robotVert, robotBleu, mission):
        # le plateau actuel et les robots (avec leurs positions)
        self.plateau = plateau
        self.robotRouge = robotRouge
        self.robotJaune = robotJaune
        self.robotVert = robotVert
        self.robotBleu = robotBleu
        self.mission = mission
        self.eucliDist = self.euclideanDistance()
        self.manatDist = self.manatthanDistance()

    def nextState(self):
        list = []
        # toute les position que peux prendre robotRouge
        list.append(Etat(self.plateau, copy(self.robotRouge).gauche(), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, copy(self.robotRouge).droite(), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, copy(self.robotRouge).haut(), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, copy(self.robotRouge).bas(), self.robotJaune, self.robotVert,
                         self.robotBleu, self.mission))

        # toute les position que peux prendre robotJaune
        list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).gauche(), self.robotVert,
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).droite(), self.robotVert,
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).haut(), self.robotVert,
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, self.robotRouge, copy(self.robotJaune).bas(), self.robotVert,
                         self.robotBleu, self.mission))

        # toute les position que peux prendre robotVert
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).gauche(),
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).droite(),
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).haut(),
                         self.robotBleu, self.mission))
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, copy(self.robotVert).bas(),
                         self.robotBleu, self.mission))

        # toute les position que peux prendre robotBleu
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).gauche(), self.mission))
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).droite(), self.mission))
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).haut(), self.mission))
        list.append(Etat(self.plateau, self.robotRouge, self.robotJaune, self.robotVert,
                         copy(self.robotBleu).bas(), self.mission))

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
        return "            : x  y \nRobot Rouge : {},{}\nRobot Jaune : {},{}\nRobot Vert  : {},{}\nRobot Bleu  : {},{}"\
            .format(self.robotRouge.x, self.robotRouge.y, self.robotJaune.x, self.robotJaune.y, self.robotVert.x, self.robotVert.y, self.robotBleu.x, self.robotBleu.y)