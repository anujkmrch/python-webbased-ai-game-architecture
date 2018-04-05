class nim:
    def __init__(self):
        ''' Constructor for this class. '''
        self.max_depth = 4
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)

    def play(self, state):
        s = self.successor(state,4,"")
        return s
    	# return self.MinMax(state,self.max_depth);
    def successor(self, state,depth,level):

        ## terminal statement for the recursion
        ## if depth reached or there is not stick then simply
        ## end the tree
        if depth <= 0:
            return None

        if state["sticks"] < 1:
            return None

        ## initialize the successors list for the current state
        s = []

        # current player
        p = state["player"]

        # loop through possible states
        for pick in range(1,3+1):
            ## go recursive
            self.successor({"player":p*-1,"sticks":state["sticks"]-pick},depth-1,level+"  ")

        ## the possible successor tree
        return s

    #
    # def successor(self,state,depth,level):
    #
    #     # Terminal statement
    #     if depth <=0 or state["sticks"] < 1:
    #         print "return the depth " + str(depth), "Sticks "+str(state["sticks"])
    #         return None;
    #
    #     s = []
    #     p = state["player"]
    #     for i in range(1,4):
    #         print level, i, depth, state["sticks"]
    #         if state["sticks"] - i > 0:
    #             # print "Player " + str(p), "Sticks "+str(state["sticks"])
    #             t = self.successor({"player":p*-1,"sticks":state["sticks"]-i},depth-1,level+"->")
    #             # if t:
    #                 # print level,"Temp "+str(t),"Player "+str(p), "Sticks "+ str(state["sticks"]),"Depth "+str(depth), "Picks "+str(i) , "Left "+str(state["sticks"]-i)
    #             # s.append((p*-1,state["sticks"]-i))
    #
    #     return s if len(s) else None

    def MinMax(self,state,depth):
    	##terminal statement
    	if depth == 0 or state["sticks"] < 1:
    		return state

    	state["player"]=state["player"] * -1
    	state["sticks"] = state["sticks"] -1
    	state = self.MinMax(state,depth-1)

    	return state
