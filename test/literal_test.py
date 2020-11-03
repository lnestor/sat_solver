from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.literal import Literal

def test_assign_atom_value_when_not_negated_sets_value():
    a = Bool("a")
    lit = Literal(a, negated = False)
    lit.assign_atom_value(False)

    assert lit.value == False

def test_assign_atom_value_when_negated_sets_value_to_negation():
    a = Bool("a")
    lit = Literal(a, negated = True)
    lit.assign_atom_value(False)

    assert lit.value == True
