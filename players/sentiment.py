class sentiment:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Angry', 'Sad', 'Love','Horny']

    def printMembers(self):
        print('Printing members of the Mammals class')
        return "".join(self.members)

    def play(self, state):
    	return "Bit sentimental "+state["message"]