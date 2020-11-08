import pytest

from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.clause import Clause
from sat_solver.literal import Literal

def test_when_given_zero_literals_raises():
    with pytest.raises(ValueError):
        clause = Clause([])

def test_satisfied_when_satisfied_returns_true():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])
    model = {a: True}

    value = clause.is_satisfied(model)
    assert value == True

def test_satisfied_when_not_satisfied_returns_false():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])
    model = {a: False}

    value = clause.is_satisfied(model)
    assert value == False

def test_check_when_satisfiable_returns_true():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    assignment = {a: True}

    assert clause.check(assignment) == True

def test_check_when_not_satisfiable_returns_false():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    assignment = {a: False}

    assert clause.check(assignment) == False

def test_check_when_not_fully_defined_returns_true():
    a = Bool("a")
    b = Bool("b")
    lit_a = Literal(a, negated = False)
    lit_b = Literal(b, negated = False)
    clause = Clause([lit_a, lit_b])

    assignment = {a: False}

    assert clause.check(assignment) == True

def test_str():
    a = Bool("a")
    b = Bool("b")
    lit_a = Literal(a, negated = False)
    lit_b = Literal(b, negated = False)
    clause = Clause([lit_a, lit_b])

    assert str(clause) == "(a or b)"

