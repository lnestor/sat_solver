class Clause():
    """
    Class representing a disjunction of some literals.
    For example, a OR b OR c is a clause. Note that
    clauses cannot have ANDs in them, only ORs.
    """

    def __init__(self, literals):
        self._assign_literal_dict(literals)
        self.atoms = self.literals.keys()

    def check(self, assignments):
        for atom, literals in self.literals.items():
            if atom in assignments:
                literal_values = [l.value(assignments[atom]) for l in literals]

                if True in literal_values:
                    return True

        # No literals were true
        return False

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

    def __contains__(self, atom):
        return atom in self.literals.keys()
