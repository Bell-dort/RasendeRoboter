#j'ai juste créé un main même si y a rien dedans pour l'instant
import affichage
import mission
import plateau
from robot import *
import etat
import GraphSearchStrategies
activeMission = mission.multicolore
initialState = etat.Etat(plateau.plateauJeu, robotRouge, robotJaune, robotVert, robotBleu, activeMission, 0)

GraphSearchStrategies.Astar(initialState, 1)


affichage.window.mainloop()



