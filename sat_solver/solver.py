class Solver():
    def __init__(self):
        self._constraints = []
        self._atoms = set()

    def check(self):
        return "unsat"

    def add(self, disjnct):
        self._constraints.append(disjnct)
        self._atoms = self._atoms | disjnct.atoms
