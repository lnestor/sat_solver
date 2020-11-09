import random

from .satisfy_status import SatisfyStatus

class Algorithm3Runner():
    """Class to perform a unit-propagation DFS based SAT solving algorithm

    This is the third iteration of the SAT solving algorithm. A "unit clause"
    is one where all but one literal are assigned false. Therefore, the
    remaining literal MUST be true. This conclusion is "propagated" throughout
    the other clauses of the formula.

    Checking every clause when a literal is assigned can be expensive. We can
    make things better by assigning two "watched literals" to each clause. When
    one of these literals is assigned false, then we inspect the clause and
    potentially propagate if it is a unity clause. If the clause is not a unit
    clause, then we choose a new watched literal. If the watched literal is
    assigned True, there is no need to inspect the clause.

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

        # Perhaps have a "watched clause" class that holds a clause and also
        # The watched literals. Then we can only pass down the clauses we need to
        # and add the list of clauses as an argument to the function. Maybe make
        # the same change to algorithms 1 & 2
        # If there exists a unit clause {p}
            # recursively call

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
