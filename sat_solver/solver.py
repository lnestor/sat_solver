from .naive_runner import NaiveRunner

class Solver():
    def __init__(self):
        self.clauses = []
        self.atoms = set()
        self.runner = None

    def check(self, runner_cls = NaiveRunner):
        self.runner = runner_cls(self.clauses, self.atoms)

        sat = self.runner.run()

        if sat:
            return "sat"
        else:
            return "unsat"

    def model(self):
        if self.runner is None:
            raise
        else:
            return self.runner.extract()

    def add_clause(self, clause):
        self.clauses.append(clause)
        self.atoms = self.atoms | clause.atoms
