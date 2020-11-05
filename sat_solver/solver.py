from .algorithm1_runner import Algorithm1Runner

class Solver():
    """Class to handle solving a SAT formula."""

    def __init__(self):
        self.clauses = []
        self.atoms = set()
        self.runner = None

    def check(self, runner_cls = Algorithm1Runner):
        """Check if the current SAT formula is satisfiable.

        A formula is satisfiable if there exists input patterns
        that cause the formula to evaluate to true.

        Args:
            runner_cls: The class for the desired algorithm implementation.
                See all runner classes for details on specific algorithms.

        Returns:
            bool: "sat" if the SAT formula is satisfiable, "unsat" otherwise

        """
        self.runner = runner_cls(self.clauses, self.atoms)

        sat = self.runner.run()

        if sat:
            return "sat"
        else:
            return "unsat"

    def model(self):
        """Find valid inputs that satisfy the current SAT formula.

        This function *must* come after a call to check(), as check() does
        the actual searching for a valid input pattern.

        If the current SAT formula is not satisfiable, this function will
        raise an exception.

        Args:
            dict: Atom assignments in the form {atom: truth value}

        """
        if self.runner is None:
            raise
        else:
            return self.runner.extract()

    def add_clause(self, clause):
        """Add a clause to the current SAT formula.

        Since the SAT formula is represented by a conjunction of clauses
        (which themselves are disjunctions), this method adds another
        disjunction. Basically it ANDs a clause with the other clauses
        that already are in the SAT formula.

        Args:
            clause: the clause to add to the SAT formula

        """
        self.clauses.append(clause)
        self.atoms = self.atoms | clause.atoms
