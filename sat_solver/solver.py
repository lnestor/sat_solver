from .runner import Runner

class Solver():
    def __init__(self):
        self.clauses = []
        self.atoms = set()

    def check(self):
        runner = Runner(self.clauses, self.atoms)

        sat = runner.run()

        if sat:
            return "sat"
        else:
            return "unsat"

    def add_clause(self, clause):
        self.clauses.append(clause)
        self.atoms = self.atoms | clause.atoms
