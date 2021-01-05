# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:10:40 2020

@author: LAURI
"""


class Node:
    
    def __init__(self,state,father):
        self.State=state
        self.Father=father
        
    def __repr__(self):
        return str(self.State)


def getPathFrom(e):
    l=[e.State]
    while e.Father:
        e=e.Father
        l.insert(0,e.State)
    return l

def getStringPath(l):
    for e in l:
        print(e.toString(), "\n\n")

def Astar(initial_state,depth,occurence_test=True):
    OL=[Node(initial_state,None)]   #on ajoute l'état initial à l'OpenList
    CL=[]                           #on créé la CloseList
    n=0
    while OL:           #tant que la liste n'est pas vide
        e=OL.pop(0)     #on récupère la tete de liste
        #print(getStringPath(getPathFrom(e)))   permet d'afficher chaque noeud cherché
        if e.State.isFinalState():  #Si l'état est final
            print(getPathFrom(e), 'extending', n, 'nodes\n')    #on affiche le chemin
            print(getStringPath(getPathFrom(e)))        #on le traduit pour l'utilisateur
            return e.State
            #break       #on sort de la boucle
        else:
            for i in range(depth):  #on effectue le nombre de fois de depth (profondeur)
                next_states=e.State.nextState()     #on récupère les états suivants
                for s in next_states:   #pour chaque état
                    if not occurence_test or s not in CL:   #si l'état n'est pas dans la CloseList
                        n+=1
                        node=Node(s,e)      #on créé un nouveau noeud
                        OL.append(node)     #On ajoute le noeud à l'OpenList
                        if occurence_test:
                            CL.append(s)    #on ajoute le Noeud à la Close List
            # on trie l'OpenList en fonction de l'Heuristique (ici la distance de Manhattan
            OL.sort(key=lambda state : state.State.manatDist + state.State.cost*1)

def BFS(initial_state,occurence_test=True):
    OL=[Node(initial_state,None)]
    CL=[]
    n=0
    while OL:
        e=OL.pop(0)
        if e.State.isFinalState() or n == 4096 :
            print(e.State.isFinalState)
            print(getPathFrom(e), 'extending', n, 'nodes')
            print(getStringPath(getPathFrom(e)))
            break
        else:
            next_states=e.State.nextState()
            for s in next_states:
                if not occurence_test or s not in CL:
                    n+=1
                    node=Node(s,e)
                    OL.append(node)
                    if occurence_test:
                        CL.append(s)


def DFS(initial_state,mission,occurence_test=True):
    OL=[Node(initial_state,None)]
    CL=[]
    n=0
    while OL:
        e=OL.pop(0)
        if e.State.isFinalState():
            print(getPathFrom(e), 'extending', n, 'nodes')
            break
        else:
            next_states=e.State.nextState()
            for s in next_states:
                if not occurence_test or s not in CL:
                    n+=1
#                    if (n % 100)==0:
#                        print(n)
                    node=Node(s,e)
                    OL.insert(0,node)
                    if occurence_test:
                        CL.append(s)
