import copy
from node import Node
class tictactoe:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']

    def setMaxDepth(self,max_depth=4):
        self.max_depth = max_depth


    def generate(self, state):
        s = self.successor(state,self.max_depth,"")
        return s

    def successor(self, state,depth,level):
        ## terminal statement for the recursion
        ## if depth reached or there is not stick then simply
        ## end the tree
        if depth <= 0:
            return None

        if state["sticks"] < 0:
            return None

        # current player
        player = state["player"]

        #intialize the current state node
        current = Node(player,state["sticks"])

        # loop through possible states
        for pick in range(1,2+1):

            ## go recursive to generate the successors for each state
            child = self.successor({"player":player*-1,"sticks":state["sticks"]-pick},depth-1,level+"  ")

            #check if there is possible successor state generated
            if child:
                #add child to the current node and make it a tree
                current.addChild(child)

        ## return current successor tree
        return current

    def move(self, node,level=""):
        if node:
            print level,node.weight,node.name
            for child in node.children:
                self.move(child,level+"+>")
