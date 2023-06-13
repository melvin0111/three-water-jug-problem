# Melvin Cabrera - CS 331
# Water Jar Project 

##############################
from collections import deque

class Graph:
    class GraphNode:
        def __init__(self, jar1=0, jar2=0, jar3=0):
            self.jar1 = jar1
            self.jar2 = jar2
            self.jar3 = jar3

        def __str__(self):
            return f"({self.jar1}, {self.jar2}, {self.jar3})"

    def __init__(self, jl1=0, jl2=0, jl3=0, target=0):
        self.jl1 = jl1
        self.jl2 = jl2
        self.jl3 = jl3
        self.target = target

    def is_found(self, node):
        return self.target in (node.jar1, node.jar2, node.jar3)

    def getTransitions(self, node): 
        a, b, c = node.jar1, node.jar2, node.jar3
        transitions = [ # create all potential states from the current state
            (self.jl1, b, c),  #fill jar 1
            (a, self.jl2, c),  # fill jar 2
            (a, b, self.jl3),  #fill jar 3
            (0, b, c),  # empty jar 1
            (a, 0, c),  # empty jar 2
            (a, b, 0),  # empty jar 3
            (a - min(a, self.jl2 - b), b + min(a, self.jl2 - b), c),  # pour jar1 into jar 2
            (a - min(a, self.jl3 - c), b, c + min(a, self.jl3 - c)),  # pour jar1 into jar 3
            (a + min(b, self.jl1 - a), b - min(b, self.jl1 - a), c),  # pour jar2 into jar 1
            (a, b - min(b, self.jl3 - c), c + min(b, self.jl3 - c)),  # pour jar2 into jar 3
            (a + min(c, self.jl1 - a), b, c - min(c, self.jl1 - a)),  # jar3 into jar 1
            (a, b + min(c, self.jl2 -b), c - min(c, self.jl2 -b))  # jar 3 into jar 2
        ]
        return [self.GraphNode(*t) for t in transitions] # rerturn the transitions as a list of graphnode objects

    def bfs(self):
        visited = set() #initialize the set 'visiited' to keep track of all the visited states


        queue = deque([(self.GraphNode(0, 0, self.jl3), [])]) # we initialize the queue  with the initial state 0,0,jl3
                                                            # the empty list is to store the solution to the problem
        while queue: #loop while queue is not 
            node, path = queue.popleft() # pop left ele from queue

            if str(node) in visited: #check if string repr of the node is in the visited set
                continue
            visited.add(str(node)) # mark the node once visited 

            if self.is_found(node): # checks if the nodes correspond to the target
                return path + [node] # if true then return the path to the solution

            for nextNode in self.getTransitions(node): # possible transition from the curr node
                if str(nextNode) not in visited:
                    queue.append((nextNode, path + [node])) # add the nextNode and the new path

        return None # if nothing can be find, then return nothing
    
#########################################################################################################################
def main():
    jar1 = int(input("size of jar1: "))
    jar2 = int(input("size of jar 2: "))
    jar3 = int(input("size of jar 3: "))
    target = int(input("enter target volume: "))

    graph = Graph(jar1, jar2, jar3, target)
    solution = graph.bfs()

    if solution:
        print("shortest sequence of operations for solution:")
        for s in solution:
            print(s)
    else:
        print("no solution were found")

if __name__ == "__main__":
    main()
