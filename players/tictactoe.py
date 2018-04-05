class tictactoe:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
 
 
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
           print('\t%s ' % member)

    def play(self, state):
    	return "Tiki Tac "+state["player"]+" "+"/".join(state["locations"])
