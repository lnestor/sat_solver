class Solver():
    def __init__(self):
        self.clauses = []

    def check(self):
        # Make each run of a solver delegated to a different object
        # Runner? Then check() would just make an instance or runner
        # and runner would handle the bulk of the algorithm
        return "unsat"

    def add_clause(self, clause):
        self.clauses.append(clause)

    def add(self, disjnct):
        self._constraints.append(disjnct)
        self._atoms = self._atoms | disjnct.atoms
