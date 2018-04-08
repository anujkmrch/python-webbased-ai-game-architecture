class sentiment:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Angry', 'Sad', 'Love','Horny']

    def setMaxDepth(self,max_depth=4):
        self.max_depth = max_depth

    def printMembers(self):
        print('Printing members of the Mammals class')
        return "".join(self.members)

    def generate(self, state):
    	return "Bit sentimental "+state["message"]

    def move(self, state,level=""):
        print state
