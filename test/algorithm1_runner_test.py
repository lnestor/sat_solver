import pytest

from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.clause import Clause
from sat_solver.literal import Literal
from sat_solver.algorithm1_runner import Algorithm1Runner

def test_check_when_satisfiable_returns_true():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])
    runner = Algorithm1Runner([clause], [a])

    value = runner.check()
    assert value == True

def test_check_when_unsatisfiable_returns_false():
    a = Bool("a")
    lit = Literal(a, negated = False)
    lit_bar = Literal(a, negated = True)
    clause = Clause([lit])
    clause_bar = Clause([lit_bar])
    runner = Algorithm1Runner([clause, clause_bar], [a])

    value = runner.check()
    assert value == False

def test_check_when_satisfiable_with_many_inputs_returns_true():
    a = Bool("a")
    b = Bool("b")
    c = Bool("c")
    d = Bool("d")
    e = Bool("e")

    lit_a = Literal(a, negated = True)
    lit_b = Literal(b, negated = False)
    lit_c = Literal(c, negated = False)
    lit_d = Literal(d, negated = True)
    lit_e = Literal(e, negated = True)

    clause1 = Clause([lit_a, lit_b])
    clause2 = Clause([lit_c, lit_d])
    clause3 = Clause([lit_e])
    runner = Algorithm1Runner([clause1, clause2, clause3], [a, b, c, d, e])

    value = runner.check()
    assert value == True

def test_model_returns_valid_model():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    runner = Algorithm1Runner([clause], [a])
    runner.check()

    model = runner.model()
    assert model == {a: True}

def test_model_when_not_satisfiable_raises():
    a = Bool("a")
    lit = Literal(a, negated = False)
    lit_bar = Literal(a, negated = True)
    clause = Clause([lit])
    clause_bar = Clause([lit_bar])

    runner = Algorithm1Runner([clause, clause_bar], [a])
    runner.check()

    with pytest.raises(RuntimeError):
        runner.model()

def test_model_when_not_checked_raises():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    runner = Algorithm1Runner([clause], [a])

    with pytest.raises(RuntimeError):
        runner.model()
