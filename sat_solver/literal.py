class Literal():
    """
    Class representing a literal, which is a bool that can be negated. For example, if A is an atom, then A
    or A_bar can be a literal.
    """

    def __init__(self, atom, negated = False):
        self.atom = atom
        self.negated = negated

    def value(self, atom_assignment):
        return atom_assignment ^ self.negated

    def __str__(self):
        if self.negated:
            return "{0}_bar = {1}".format(self.atom, self.value)
        else:
            return "{0} = {1}".format(self.atom, self.value)

    def __repr__(self):
        if self.negated:
            return "{0}_bar = {1}".format(self.atom, self.value)
        else:
            return "{0} = {1}".format(self.atom, self.value)

