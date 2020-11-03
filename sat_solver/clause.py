class Clause():
    """
    Class representing a disjunction of some literals.
    For example, a OR b OR c is a clause. Note that
    clauses cannot have ANDs in them, only ORs.
    """

    def __init__(self, literals):
        self._assign_literal_dict(literals)
        self.is_satisfied = False
        self.still_satisfiable = True
        self.assigned_atom_count = 0

    def update(self, atom, atom_value):
        """
        Updates the values of an atom in this clause. Also assigns flags indicating this clause is
        satisfied (one literal is True) or unsatisfiable (all literals are False)
        """
        if self.is_satisfied:
            return

        self._assign_literal_values(atom, atom_value)

        self.assigned_atom_count += 1
        if self.assigned_atom_count == len(self.literals.keys()):
            self.still_satisfiable = False

    def _assign_literal_values(self, atom, atom_value):
        changed_literals = self.literals[atom]

        for literal in changed_literals:
            literal_value = literal.assign_atom_value(atom_value)

            if literal_value:
                self.is_satisfied = True


    def _assign_literal_dict(self, literals):
        if len(literals) == 0:
            raise ValueError

        self.literals = {}

        for lit in literals:
            atom = lit.atom
            if atom in self.literals:
                self.literals[atom].append(lit)
            else:
                self.literals[atom] = [lit]

