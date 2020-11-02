class And():
    def __init__(self, lhs, rhs):
        self.atoms = lhs.atoms | rhs.atoms

