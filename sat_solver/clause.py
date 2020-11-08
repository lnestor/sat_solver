class Clause():
    """Class representing a disjunction of some literals.

    A disjunction is a collection of literals that are ORed together. For example,
    a OR b OR c is a clause. Note that clauses cannot have ANDs in them, only ORs.
    """

    def __init__(self, literals):
        """Initializes a clause with a given set of literals.

        Args:
            literals: the literals in the clause

        """
        self._assign_literal_dict(literals)
        self.atoms = self.literals.keys()

    def is_satisfied(self, model):
        """Check fi the clause is completely satisfied by a model.

        A clause is satisfied if at least one of its literals is true.

        Args:
            model: dict with assignments of boolean variables in the form
                {atom: true value}

        Returns:
            bool: True if completely satisfied, False otherwise

        """
        for atom, literals in self.literals.items():
            if atom in model:
                literal_values = [l.value(model[atom]) for l in literals]

                if True in literal_values:
                    return True

        return False

    def check(self, assignments):
        """Check if the clause is satisfiable with some assignments

        A clause is satisfiable if at least one of its literals is true (in which
        case it is satisfied) or at least one of its literals is unassigned. A
        clause is not satisfiable if all of its literals are false.

        Args:
            assignments: dictionary in the form {atom: truth value}

        Returns:
            bool: True if satisfiable, False otherwise

        """
        for atom, literals in self.literals.items():
            if atom in assignments:
                literal_values = [l.value(assignments[atom]) for l in literals]

                if True in literal_values:
                    return True
            else:
                # Not all atoms have been assigned yet
                return True

        # No literals were true
        return False

    def _assign_literal_dict(self, literals):
        """Initialize the dictionary from atom to literal.

        A clause may contain multiple literals of the same atom. To handle this,
        a dictionary maps an atom to all literal instances in the clause. This
        function initializes that dictionary.

        Args:
            literals: list of literals in the clause
        """
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
        """Returns if an atom is present in the clause

        Args:
            atom: the atom to search for in the clause

        Returns:
            bool: True if the atom is in the clause, False otherwise
        """
        return atom in self.literals.keys()

    def __str__(self):
        return "(" + " or ".join([str(k) for k in self.literals.keys()]) + ")"

    def __repr__(self):
        return "(" + " or ".join([str(k) for k in self.literals.keys()]) + ")"
