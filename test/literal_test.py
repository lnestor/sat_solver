from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.literal import Literal

def test_value_when_not_negated_sets_value():
    a = Bool("a")
    lit = Literal(a, negated = False)
    assert lit.value(False) == False

def test_value_when_negated_sets_value_to_negation():
    a = Bool("a")
    lit = Literal(a, negated = True)
    assert lit.value(False) == True

def test_str_when_not_negated():
    a = Bool("a")
    lit = Literal(a, negated = False)
    assert str(lit) == "a"

def test_str_when_negated():
    a = Bool("a")
    lit = Literal(a, negated = True)
    assert str(lit) == "a_bar"
