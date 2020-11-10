import collections

from .helpers.random_helper import sample_or_all
from .satisfy_status import SatisfyStatus

class UnitPropagator:
    def __init__(self, clauses):
        self.clauses = clauses

        self.watch_list = collections.defaultdict(list)
        for clause in clauses:
            to_watch = sample_or_all(clause.atoms, 2)

            for atom in to_watch:
                self.watch_list[atom].append(clause)

    def inspect(self, atoms, model, prev_atom):
        if not prev_atom in self.watch_list:
            return None, None

        if model[prev_atom] == True:
            return None, None

        clauses = self.watch_list[prev_atom]
        statuses = [c.check(model) for c in self.clauses]

        for i in range(len(statuses)):
            status = statuses[i]
            clause = clauses[i]

            if status == SatisfyStatus.Unit:
                unit_atom = list(self._remaining_atoms(clause, model))[0]
                literals = clause.literal(unit_atom)

                return unit_atom, literals[0].negated == False

        del self.watch_list[prev_atom]
        self._choose_new_watched(clauses, model)

        return None, None

    def is_watched(self, atom):
        return atom in self.watch_list

    def watched(self):
        return self.watch_list.copy()

    def _choose_new_watched(self, clauses, model):
        # I think atom has unassigned atoms
        # So we can probably just use that
        for clause in clauses:
            remaining_atoms = self._remaining_atoms(clause, model)

            for atom in remaining_atoms:
                if self._can_watch(clause, atom):
                    self.watch_list[atom].append(clause)
                    break

    def _can_watch(self, clause, atom):
        return not (atom in self.watch_list and clause in self.watch_list[atom])

    def _remaining_atoms(self, clause, model):
        return set(clause.atoms) - set(model.keys())
