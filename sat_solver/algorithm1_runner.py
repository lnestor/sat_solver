import random
from .stack_frame import StackFrame

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
        self.unassigned_atoms = atoms
        self.assigned_atoms = []
        self.stack = []
        self.model = None

    def run(self):
        """Runs a DFS to find input patterns that satisfy the clauses given.

        Returns:
            bool: True if the formula is satisfiable, False otherwise

        """
        first_atom = self._get_next_atom(0)
        self.stack.append(StackFrame(first_atom, {}, 0))

        while len(self.stack) > 0:
            frame = self.stack.pop()
            next_atom = self._get_next_atom(frame.depth + 1)

            if frame.atom is not None:
                next_assignments = [True, False]
                random.shuffle(next_assignments)

                for assignment in next_assignments:
                    new_assignments = frame.assignments.copy()
                    new_assignments[frame.atom] = assignment

                    next_frame = StackFrame(next_atom, new_assignments, frame.depth + 1)
                    self.stack.append(next_frame)
            else:
                # No more atoms to assign, check if it works
                assignments = frame.assignments
                satisfied = self._check_satisfiability(assignments)

                if satisfied:
                    self.model = assignments
                    return True

        # No satisfiable pattern was found
        return False

    def extract(self):
        """Get an input pattern that satisfies the CNF formula.

        Returns:
            dict: Atom assignments in the form of {atom: value}

        """
        if self.model is not None:
            return self.model
        else:
            raise

    def _get_next_atom(self, frame_depth):
        """Chooses the next atom to assign a value to.

        The current implementation chooses randomly. Other implementations are possible.

        Args:
            frame_depth: the depth of the current frame in the search tree

        Returns:
            atom: The next atom to be explored.

        """
        if len(self.assigned_atoms) > frame_depth:
            return self.assigned_atoms[frame_depth]
        elif len(self.unassigned_atoms) == 0:
            return None
        else:
            atom = random.sample(self.unassigned_atoms, 1)[0]
            self.unassigned_atoms.remove(atom)
            self.assigned_atoms.append(atom)
            return atom

    def _check_satisfiability(self, assignments):
        """Checks if the assignments passed in satisfy the clauses.

        Args:
            assignments: dict of boolean assignments in the form of {atom: value}

        Returns:
            bool: True if the formula is satisfied, False otherwise

        """
        clause_satisfies = [c.check(assignments) for c in self.clauses]
        return not (False in clause_satisfies)
