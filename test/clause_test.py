import pytest

from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.clause import Clause
from sat_solver.literal import Literal
from sat_solver.satisfy_status import SatisfyStatus

def test_when_given_zero_literals_raises():
    with pytest.raises(ValueError):
        clause = Clause([])

def test_check_when_satisfiable_returns_satisfied():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])
    model = {a: True}

    value = clause.check(model)
    assert value == SatisfyStatus.Satisfied

def test_check_when_not_satisfiable_returns_unsatisfied():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])
    model = {a: False}

    value = clause.check(model)
    assert value == SatisfyStatus.Unsatisfied

def test_check_when_not_fully_defined_returns_pending():
    a = Bool("a")
    b = Bool("b")
    lit_a = Literal(a, negated = False)
    lit_b = Literal(b, negated = False)
    clause = Clause([lit_a, lit_b])
    model = {a: False}

    value = clause.check(model)
    assert value == SatisfyStatus.Pending

def test_str():
    a = Bool("a")
    b = Bool("b")
    lit_a = Literal(a, negated = False)
    lit_b = Literal(b, negated = False)
    clause = Clause([lit_a, lit_b])

    assert str(clause) == "(a or b)"

