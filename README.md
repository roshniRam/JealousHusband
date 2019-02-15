# JealousHusband
To model the Jealous Husband problem in terms of state space search problem and solve it using BFS/DFS approach.

## Problem statement
Three jealous husbands and their wives need to cross a river using a single boat. At no time should any of the women be left in company with any of the men, unless her husband is present. The boat can carry up to two passengers and can not move by itself.

## Approach
To model the problem as a state space search problem, we considered the shores of the river as the edges where the couples are standing. Initially, we assumed them to be standing on the left edge in the sequence as wife1, wife2, wife3, husband1, husband2, husband3. We describe the position of each person through numbers, 0 for left shore and 1 for right, same conventions are used for the position of the boat.
At each current state, we search for the possible next moves and check if the conditions are fulfilled or not, we are also required to check the goal state condition.

### Using BFS
The optimal solution is the one with the fewest number of steps. The program should print out the solution by listing a sequence of steps and operators needed to reach the goal state from the initial state.

<img src="https://user-images.githubusercontent.com/30633549/52881615-06742180-318b-11e9-820c-9c7279864bba.png" height="125" >

### Using DFS
The optimal solution is the one with the fewest number of steps. The program should print out the solution by listing a sequence of steps and operators needed to reach the goal state from the initial state.

<img src="https://user-images.githubusercontent.com/30633549/52881763-87331d80-318b-11e9-9145-0591a5e83056.png" height="125">
