import random

class mission():
    """docstring for mission"""

    def __init__(self, couleur, symbole):  # constructeur mission
        self.couleur = couleur
        self.symbole = symbole

# def accessContenu(self):
# 	return self.symbole + " " + self.couleur


triangleRouge = mission("red", "triangle")
triangleBleu = mission("blue", "triangle")
triangleVert = mission("green", "triangle")
triangleJaune = mission("yellow", "triangle")

cercleRouge = mission("red", "cercle")
cercleBleu = mission("blue", "cercle")
cercleVert = mission("green", "cercle")
cercleJaune = mission("yellow", "cercle")

carreRouge = mission("red", "carre")
carreBleu = mission("blue", "carre")
carreVert = mission("green", "carre")
carreJaune = mission("yellow", "carre")

losangeRouge = mission("red", "losange")
losangeBleu = mission("blue", "losange")
losangeVert = mission("green", "losange")
losangeJaune = mission("yellow", "losange")

multicolore = mission("multicolore", "")
vide = mission("", "")

activeMission = multicolore
# activeMission = random.choice([triangleJaune,triangleRouge,triangleBleu,triangleVert,carreJaune,carreVert,carreRouge,
# 							   carreBleu,losangeJaune,losangeVert,losangeRouge,losangeBleu,cercleJaune,cercleVert,cercleBleu,cercleRouge])

