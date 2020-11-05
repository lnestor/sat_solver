# This function below maps atoms to clauses, but we can probably know this earlier when
# clauses are added to the solver. Should we move this functionality up to the solver?
# Then the solver would maintain a list of atoms -> clause relationships
def _assign_atom_appearances(self, atoms, clauses):
    self.atom_appearances = {}

    for atom in atoms:
        self.atom_appearances[atom] = []

        for clause in clauses:
            if atom in clause:
                self.atom_appearances[atom].append(clause)
