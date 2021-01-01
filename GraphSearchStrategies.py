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
    OL=[Node(initial_state,None)]
    CL=[]
    n=0
    while OL:
        e=OL.pop(0)
        #print(getStringPath(getPathFrom(e)))
        if e.State.isFinalState() :
            print(e.State.isFinalState())
            print(getPathFrom(e), 'extending', n, 'nodes\n')
            print(getStringPath(getPathFrom(e)))
            break
        else:
            for i in range(depth):
                next_states=e.State.nextState()
                for s in next_states:
                    if not occurence_test or s not in CL:
                        n+=1
                        node=Node(s,e)
                        OL.append(node)
                        if occurence_test:
                            CL.append(s)
            OL.sort(key=lambda state : state.State.manatDist + state.State.cost*1)

def BFS(initial_state,occurence_test=True):
    OL=[Node(initial_state,None)]
    CL=[]
    n=0
    while OL:
        e=OL.pop(0)
        if e.State.isFinalState() or n>1024:
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
                    print(getStringPath(getPathFrom(node)))


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
