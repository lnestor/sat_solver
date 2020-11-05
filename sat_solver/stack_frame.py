class StackFrame():
    """Class representing a node of the DFS search tree.

    All algorithms in this project are based on a depth-first
    search. These are implemented using a stack. This class is
    a data wrapper that captures the necessary information that
    needs stored on each iteration.

    Attributes:
        atom: The next atom that will be searched. "Searching" in
            this case means branching into true and false values
            in the next iteration of the search algorithm.
        assignments: The current list of atom assignments at the
            time of this node in the search tree.
        depth: The depth of the search tree at the time of this node.

    """

    def __init__(self, atom, assignments, depth):
        """Initializes a stack frame."""
        self.atom = atom
        self.assignments = assignments
        self.depth = depth
