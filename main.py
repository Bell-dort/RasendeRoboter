#j'ai juste créé un main même si y a rien dedans pour l'instant
import affichage
import mission
from robot import *
import etat
import GraphSearchStrategies


initialState = etat.Etat(plateau.plateauJeu, robotRouge, robotJaune, robotVert, robotBleu, mission.activeMission, 0)

GraphSearchStrategies.Astar(initialState, 1)


affichage.window.mainloop()



