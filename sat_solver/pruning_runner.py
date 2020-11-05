import random
from .stack_frame import StackFrame

class PruningRunner():
    """
    Class to perform the SAT solving algorithm. This class will
    perform a single instance of the algorithm, while the Solver
    class will create runners each time solver.create() is called.
    """

    def __init__(self, clauses, atoms):
        self.clauses = clauses.copy()
        self.unassigned_atoms = atoms.copy()
        self.assigned_atoms = []
        self.stack = []
        self.atom_assignments = {}
        # This function below maps atoms to clauses, but we can probably know this earlier when
        # clauses are added to the solver. Should we move this functionality up to the solver?
        # Then the solver would maintain a list of atoms -> clause relationships
        self._assign_atom_appearances(atoms, clauses)
        self.model = None

    def run(self):
        """Runs a DFS to find input patterns that satisfy the clauses given"""
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
        if self.model is not None:
            return self.model
        else:
            raise

    def _switch_on_atom(self, next_atom, old_frame):
        next_assignments = [True, False]
        random.shuffle(next_assignments)

        for assignment in next_assignments:
            new_assignments = old_frame.assignments.copy()
            new_assignments[old_frame.atom] = assignment

            next_frame = StackFrame(next_atom, new_assignments, old_frame.depth + 1)
            self.stack.append(next_frame)

    def _get_next_atom(self, frame_depth):
        """Extracts the next atom to assign a value to. The current implementation chooses randomly."""
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
        """Checks if the assignments passed in cause any conflicts"""
        clause_satisfies = [c.check(assignments) for c in self.clauses]
        return not (False in clause_satisfies)

    def _assign_atom_appearances(self, atoms, clauses):
        self.atom_appearances = {}

        for atom in atoms:
            self.atom_appearances[atom] = []

            for clause in clauses:
                if atom in clause:
                    self.atom_appearances[atom].append(clause)
