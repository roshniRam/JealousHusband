'''
Lab 4
Jealous Husband code in Python

'''

import sys
import time
from copy import deepcopy

class State:
    #edge is an array with positions like w1,w2,w3,h1,h2.h3
    #holds 0 if at left edge and 1 if at right edge
    edge = None                  
    #position of the boat, 0 for left & 1 for right
    boatPosition = 0                
    depth = 0   
    #path is an array of states to reach the goal state                       
    path = None                   
    
    def __init__(self, s=[], b=0):
        self.edge = s
        self.boatPosition = b
        self.depth = 0
        self.path = []
        
    def f(self):                        # evaluation function
        return self.depth + h(self)     
          

def checkCondition(current):
    for i in range(0,noOfCouples):
        if current.edge[i] != current.edge[noOfCouples+i]:          # husband is not with his wife
            for j in range(noOfCouples, noOfCouples*2): 
                    if(current.edge[j] == current.edge[i]):       # another man is with the wife
                        return 1
    return 0

def alterbit(bit):                                                  # used to change position of people or the boat
    return abs(bit - 1)

def isSame(state):                                                  # people on the same side as the boat are "good"
    good_people = deepcopy(state.edge)
    for i in range(0, len(state.edge)):
        if state.edge[i] == state.boatPosition:
            good_people[i] = 1
    return good_people

def GoalTest(state):                     
    result = len(state.edge)
    for i in state.edge:
        result = result - i
    return result      #if 0 then goal matched

def visited(state, searched):                                       # determines whether a State has already been visited
    for k in range(0, len(searched)):
        if state.edge == searched[k].edge and state.boatPosition == searched[k].boatPosition:
            return True
    return False

def moveGen(cap, state, movement, result, start):                      # computes all possible moves from a current State with a certain boat capacity
    for i in range(start, len(state.edge)):
        if isSame(state)[i] == 1:                                   # if the person is on the same side as the boat
            movement.append(i)                                      # add the person to the list of possible moves
            if cap > 1:                                             # if there is more space in the boat
                moveGen(cap-1, state, movement, result,i)              # iterate; start for-loop with i to prevent duplicates (permutations)
            if cap == 1:                                            # if the boat is full
                result.append(deepcopy(movement))                   # add move to the result array
            movement.pop()                                          # when returning to the outer iteration, pop the last item
    #print("result:", result)
    return result                                                   # return an array of possible moves

def expand(state): 
    stateCopy = deepcopy(state)          # create copy of the state
    result = [] 
    possible_moves = moveGen(capacity, state, [], result,0)       # get all possible moves for the current State and capacity
    for i in possible_moves:                                        # iterate through all possible state changes
        stateCopy = deepcopy(state)
        for j in i:
            stateCopy.edge[j]  = alterbit(state.edge[j])          # move persons
        stateCopy.boatPosition = alterbit(state.boatPosition)                       # move boat
        if visited(stateCopy, searched):                            # check if state was already visited
            True
        elif checkCondition(stateCopy):                                   # check if there is jealousy
            searched.append(stateCopy)
        elif True:
            stateCopy.depth = stateCopy.depth + 1                   # increase depth
            stateCopy.path.append(state)                            # add the parent node to the path
            frontier.append(stateCopy)                              # add the node to the frontier
            


def DFS(noOfStates):
    while True:
        noOfStates = noOfStates + 1
        
        current = frontier.pop()               # examine last item from frontier (LIFO)
        
        if GoalTest(current) == 0:                    # check for goal state
            print("Total Number of States Visited: ", noOfStates)   
            return current                                     
        
        expand(current)                                         # expand and add new states to frontier
        searched.append(current)                                # add the current node to the closed list
 

noOfCouples = int(input("Enter the number of couples: "))
capacity = 2
    
couple = [0,0]
initial = State([], 0)
goal = State([], 0)
frontier = []                        # open list (frontier)
searched = []                        # closed list
noOfStates = 0
path=[]
    
for i in range(0,noOfCouples):                        # add couples on left side of the river
    initial.edge.extend(couple)                    # the state will be treated as w1,w2,w3,h1,h2.h3

frontier.append(initial)                            # add initial node to frontier
    
print("Depth First Search")
goal=DFS(noOfStates)
    
print("\nReached the goal: ", goal.edge)
print("Depth: ", goal.depth)

for i in goal.path:
        path.append(i.edge)
print("Path: ", path)


