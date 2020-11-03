import pytest

from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.clause import Clause
from sat_solver.literal import Literal

def test_when_given_zero_literals_raises():
    with pytest.raises(ValueError):
        clause = Clause([])

def test_update_assigns_value_to_literal():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    clause.update(a, True)
    assert lit.value == True

def test_update_assigns_values_to_all_literals_of_same_atom():
    a = Bool("a")
    lit = Literal(a, negated = False)
    lit_bar = Literal(a, negated = True)
    clause = Clause([lit, lit_bar])

    clause.update(a, True)
    assert lit.value == True
    assert lit_bar.value == False

def test_is_satisfied_when_a_literal_is_true_returns_true():
    a = Bool("a")
    a_lit = Literal(a, negated = False)
    clause = Clause([a_lit])

    clause.update(a, True)
    assert clause.is_satisfied == True

def test_is_satisfied_when_no_assignments_returns_false():
    a = Bool("a")
    a_lit = Literal(a, negated = False)
    clause = Clause([a_lit])

    assert clause.is_satisfied == False

def test_is_satisfied_when_no_true_literals_returns_false():
    a = Bool("a")
    a_lit = Literal(a, negated = False)
    clause = Clause([a_lit])

    clause.update(a, False)
    assert clause.is_satisfied == False

def test_still_satisfiable_when_all_literals_false_returns_false():
    a = Bool("a")
    a_lit = Literal(a, negated = False)
    clause = Clause([a_lit])

    clause.update(a, False)
    assert clause.still_satisfiable == False

def test_still_satisfiable_when_no_assignments_returns_true():
    a = Bool("a")
    a_lit = Literal(a, negated = False)
    clause = Clause([a_lit])

    assert clause.still_satisfiable == True

def test_still_satisfiable_when_remaining_literals_returns_true():
    a = Bool("a")
    b = Bool("b")
    a_lit = Literal(a, negated = False)
    b_lit = Literal(b, negated = False)
    clause = Clause([a_lit, b_lit])

    clause.update(a, False)
    assert clause.still_satisfiable == True
