class Literal():
    """Class representing a literal, which is an atom or its negation.

    For example, if A is an atom, then A or A_bar can be a literal.
    """

    def __init__(self, atom, negated = False):
        """Initializes a literal.

        Args:
            atom: the atom of the literal
            negated: whether or not the atom should be negated

        """
        self.atom = atom
        self.negated = negated

    def value(self, atom_assignment):
        """Finds the value of the literal given an assignment of its atom

        Args:
            atom_assignment: the value of the atom for this literal

        Returns:
            bool: True if the literal evaluates to true, False otherwise

        """
        return atom_assignment ^ self.negated

    def __str__(self):
        if self.negated:
            return "%s_bar" % (self.atom)
        else:
            return "%s" % (self.atom)

    def __repr__(self):
        if self.negated:
            return "%s_bar" % (self.atom)
        else:
            return "%s" % (self.atom)
