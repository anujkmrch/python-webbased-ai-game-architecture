class Node(object):
    """docstring for Node."""
    def __init__(self, weight,name,parent=None):
        super(Node, self).__init__()
        self.weight = weight
        self.name = name
        self.parent = parent
        self.children = []

    # method to add children to current node
    # returns added child node
    def addChild(self, node):
        self.children.append(node)
        return self

    # method to get parent of the current node
    def getParent(self):
        return self.parent
