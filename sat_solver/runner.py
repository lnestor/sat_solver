import random

class Runner():
    """
    Class to perform the SAT solving algorithm. This class will
    perform a single instance of the algorithm, while the Solver
    class will create runners each time solver.create() is called.
    """

    def __init__(self, clauses, atoms):
        self._clauses = clauses
        self._atoms = atoms
        self._atom_stack = []

    def run(self):
        while True:
            atom = self._get_atom()
            self._atom_stack.push(atom)

            assignment = random.choice([True, False])

    def _get_atom(self):
        """
        Extracts the next atom to assign a value to.
        The current implementation chooses randomly.
        """
        atom = random.sample(self._atoms, 1)[0]
        self._atoms.remove(atom)
        return atom
