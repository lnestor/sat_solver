import collections

from .helpers.random_helper import sample_or_all

# Check if latest assignment is in watched literals
# If it isn't, then assign and continue
# If it is, then inspect those literals

# Q: how to handle unit propagation?
    # Right now all stack frames use the same atom chooser
    # But if with unit propagation atoms can be chosen by something other than the atom chooser
    # So options:
        # The atom choser is told what the next atom will be for everybody based on the unit propagation
        # The atom chosen from the chooser is compared with the current assignments.
            # If it is already assigned, push it on the stack, but with the value assigned

# How to detect if everything has been assigned?
class LiteralWatcher():
    def __init__(self, clauses):
        self.watched = collections.defaultdict(list)
        for clause in clauses:
            to_watch = sample_or_all(clause.atoms, 2)

            for atom in to_watch:
                self.watched[atom].append(clause)

    def inspect(self, assignment):
        if list(assignment.keys())[0] in self.watched:

            print("aa")
        return

    def _map_atoms(self, clauses):
        mappings = {}
        for clause in clauses:
            for atom in clause.atoms:
                if atom in mappings:
                    mappings[atom].append(clause)
                else:
                    mappings[atom] = [clause]
        return mappings
