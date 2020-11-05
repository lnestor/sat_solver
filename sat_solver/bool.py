class Bool():
    """Class representing a single atom, which is a boolean variable."""

    def __init__(self, name):
        """Initializes the atom.

        Args:
            name: the name of the boolean variable

        """
        self.name = name

    def __str__(self):
        return self.name
