import random

from .satisfy_status import SatisfyStatus

class Algorithm2Runner():
    """Class to perform a pruning-based DFS based SAT solving algorithm

    This is the second iteration of the SAT solving algorithm. In this iteration,
    The boolean formula is checked for satisfiability after each variable
    assignment. If a variable assignment causes the formula to be unsatisfiable,
    then that branch of the search tree is not further explored because all
    assignments in that subtree are also unsatisfiable.

    The satisfiability is checked by querying each clause on every assignment.
    This is not efficient because clauses do not need to be queried unless they
    have only one literal unassigned. This will be addressed in algorithm 3.

    """

    def __init__(self, clauses, atoms):
        """Initializes the runner.

        Args:
            clauses: A list of the clauses in the CNF formula.
            atoms: A list of the atoms in the formula.

        """
        self.clauses = clauses
        self.initial_atoms = atoms
        self._model = None

    def check(self):
        """Runs a DFS to find input patterns that satisfy the clauses given.

        Returns:
            bool: True if the formula is satisfiable, False otherwise

        """
        return self._run(self.initial_atoms, {})

    def model(self):
        """Get an input pattern that satisfies the CNF formula.

        Returns:
            dict: Atom assignments in the form of {atom: value}

        """
        if self._model == None:
            raise

        return self._model

    def _run(self, atoms, model):
        """The recursive DFS work function.

        This is the function that actually performs the DFS. It is called
        recursively to perform the search.

        Args:
            atoms: the remaining atoms that have not been assigned
            model: the current model of already assigned atoms

        Returns:
            bool: True if the formula is satisfiable with the given model

        """
        clause_statuses = [c.check(model) for c in self.clauses]

        if all([status == SatisfyStatus.Satisfied for status in clause_statuses]):
            self._model = model
            return True

        if any([status == SatisfyStatus.Unsatisfied for status in clause_statuses]):
            return False

        if len(atoms) > 0:
            to_explore = random.sample(atoms, 1)[0]

            new_atoms = atoms.copy()
            new_atoms.remove(to_explore)

            new_model_true = model.copy()
            new_model_false = model.copy()
            new_model_true[to_explore] = True
            new_model_false[to_explore] = False

            return (self._run(new_atoms, new_model_true) or
                    self._run(new_atoms, new_model_false))
        else:
            return False
