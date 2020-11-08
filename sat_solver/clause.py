from .satisfy_status import SatisfyStatus

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

    def check(self, model):
        """Check the current status of the clause given a model.

        A clause in "pending" if no literals are true but some are unassigned.
        A clause is "satisfied" if at least one of its literals is true.
        A clause in "unsatisfied" if all of its literals are false.

        Args:
            model: dict with assignments of boolean variables in the form
                of {atom: truth value}

        Returns:
            enum: SatisfyStatus.Pending if the clause is pending
                SatisfyStatus.Satisfied if the clause is satisfied
                SatisfyStatus.Unsatisfied if the clause is unsatisfied

        """
        for atom, literals in self.literals.items():
            if atom in model:
                literal_values = [l.value(model[atom]) for l in literals]

                if True in literal_values:
                    return SatisfyStatus.Satisfied
            else:
                return SatisfyStatus.Pending

        return SatisfyStatus.Unsatisfied

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
