import copy

class nim:
    def __init__(self):
        ''' Constructor for this class. '''
        self.max_depth = 4

    def play(self, state):
        s = self.successor(state,5,"")
        return s

    def successor(self, state,depth,level):
        ## terminal statement for the recursion
        ## if depth reached or there is not stick then simply
        ## end the tree
        if depth <= 0:
            # print "Depth "+ str(depth)+ "Stick Reached "+str(state["sticks"])
            return state

        if state["sticks"] < 1:
            return state

        ## initialize the successors list for the current state
        s = []

        # current player
        p = state["player"]

        # loop through possible states
        for pick in range(1,3+1):
            print str(level) ,str(state["sticks"])+" sticks passed and on","picking "+ str(pick),"on depth "+ str(depth), "only "+str(state["sticks"] -pick) + " left", "by player",("max" if p==1 else "min")
            ## go recursive
            t = self.successor({"player":p*-1,"sticks":state["sticks"]-pick},depth-1,level+"  ")
            s.append(t)

        ## return current successor tree
        return s
