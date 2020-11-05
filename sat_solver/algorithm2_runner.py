import random
from .stack_frame import StackFrame

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
        self.clauses = clauses.copy()
        self.unassigned_atoms = atoms.copy()
        self.assigned_atoms = []
        self.stack = []
        self.model = None

    def run(self):
        """Runs a modified DFS to find input patterns that satisfy the clauses given.

        Returns:
            bool: True if the formula is satisfiable, False otherwise

        """
        first_atom = self._get_next_atom(0)
        self.stack.append(StackFrame(first_atom, {}, 0))

        while len(self.stack) > 0:
            frame = self.stack.pop()
            assignments = frame.assignments

            # Check if this is still satisfiable
            # If it is not, this path cannot exist
            satisfiable = self._check_satisfiability(assignments)

            if satisfiable:
                if frame.atom is not None:
                    next_atom = self._get_next_atom(frame.depth + 1)
                    self._switch_on_atom(next_atom, frame)
                else:
                    # Assignments all work, return
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

    def _switch_on_atom(self, next_atom, old_frame):
        """Branch on an atom being assigned true or false.

        Args:
            next_atom: The next atom to be assigned. Note that this
                is not the same as the current atom being branched.
            old_frame: The previous stack frame of the DFS algorithm.

        """
        next_assignments = [True, False]
        random.shuffle(next_assignments)

        for assignment in next_assignments:
            new_assignments = old_frame.assignments.copy()
            new_assignments[old_frame.atom] = assignment

            next_frame = StackFrame(next_atom, new_assignments, old_frame.depth + 1)
            self.stack.append(next_frame)

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
        """Checks if the formula is still satisfiable.

        Note that this does not check if the formula is satisfied, only
        if it can be satisfied in the future.

        Args:
            assignments: dict of boolean assignments in the form of {atom: value}

        Returns:
            bool: True if the formula is still satsifiable, False otherwise

        """
        clause_satisfies = [c.check(assignments) for c in self.clauses]
        return not (False in clause_satisfies)
