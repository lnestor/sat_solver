import random
from .atom_chooser import AtomChooser
from .stack_frame import StackFrame

class Algorithm3Runner():
    """Class to perform a watched-clause DFS based SAT solving algorithm.

    This is the third iteration of the SAT solving algorithm. Like the last
    iteration, the boolean formula is checked for satisfiability after each
    variable assignment. However, in this iteration, clauses have "watched
    literals" and are only inspected once one of those watched literals is
    assigned false.

    Each clause will have two watched literals. These literals are chosen
    randomly from the literals in the clause. When one of those literals is
    assigned true, then the clause does not need to be watched anymore. If
    one of the literals is assigned false, then the clause must be inspected.

    If the clause only has one remaining variable and the rest are false, then
    that variable must be set to true. If it has more remaining variables,
    then the watched literal is assigned false and a new, unassigned literal
    is chosen as the next watched literal.

    """

    def __init__(self, clauses, atoms):
        """Initializes the runner.

        Args:
            clauses: A list of the clauses in the CNF formula.
            atoms: A list of the atoms in the formula.

        """
        self.clauses = clauses.copy()
        self.chooser = AtomChooser(atoms)
        self.stack = []
        self.model = None

    def run(self):
        """Runs a modified DFS to find input patterns that satisfy the clauses given.

        Returns:
            bool: True if the formula is satisfiable, False otherwise

        """
        first_atom = self.chooser.choose(0)
        self.stack.append(StackFrame(first_atom, {}, 0))

        while len(self.stack) > 0:
            frame = self.stack.pop()
            assignments = frame.assignments
            latest_assignment = frame.latest_assignment

            propgations, conflicts = self.watched_literals.inspect(latest_assignment)

            if len(conflicts) > 0:
                # Conflicts exist, this path cannot be satisfied

            for propagation in propagations:
                # create new assignments dict with propagated assignments

            # Detect somehow if everything has been assigned
            if satisfiable:
                if frame.atom is not None:
                    next_atom = self.chooser.choose(frame.depth + 1)
                    # Check if next_atom is already assigned,
                    # If not, then switch
                    # If so, then push only one stack frame
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
