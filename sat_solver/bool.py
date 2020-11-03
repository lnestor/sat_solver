class Bool():
    """
    Class representing a single atom.
    """

    def __init__(self, name):
        self.name = name
        self.atoms = {self}

    def __str__(self):
        return self.name
