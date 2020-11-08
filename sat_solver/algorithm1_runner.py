import random

class Algorithm1Runner():
    """Class to perform a DFS based SAT solving algorithm.

    This is the first iteration of the SAT solving algorithm. It uses a simple
    depth-first search to find input patterns that satisfy a CNF formula. The
    search is performed on a tree where each node represents a single atom in
    the formula. The left branch of each node represents that node assigned as
    true, and the right branch represents that node assigned as false.

    This search incrementally chooses variables to assign values to. When all
    variables are assigned, it checks if the assignments satisfy the formula.
    If so, it returns. If not, it steps up one node in the tree and explores
    the other branches.

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
        satisfied = [c.is_satisfied(model) for c in self.clauses]
        if not (False in satisfied):
            self._model = model
            return True

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
