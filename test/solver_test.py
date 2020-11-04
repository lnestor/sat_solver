import pytest

from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.clause import Clause
from sat_solver.literal import Literal
from sat_solver.solver import Solver

def test_check_when_unsatisfiable_returns_unsat():
    a = Bool("a")
    lit = Literal(a, negated = False)
    lit_bar = Literal(a, negated = True)
    clause = Clause([lit])
    clause_bar = Clause([lit_bar])

    s = Solver()
    s.add_clause(clause)
    s.add_clause(clause_bar)

    assert s.check() == "unsat"

def test_check_when_satisfiable_returns_sat():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    s = Solver()
    s.add_clause(clause)

    assert s.check() == "sat"

def test_model_when_unsatisfiable_raises():
    a = Bool("a")
    lit = Literal(a, negated = False)
    lit_bar = Literal(a, negated = True)
    clause = Clause([lit])
    clause_bar = Clause([lit_bar])

    s = Solver()
    s.add_clause(clause)
    s.add_clause(clause_bar)

    s.check()

    with pytest.raises(RuntimeError):
        s.model()

def test_model_when_not_checked_raises():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    s = Solver()
    s.add_clause(clause)

    with pytest.raises(RuntimeError):
        s.model()


def test_model_when_satisifiable_returns_model():
    a = Bool("a")
    lit = Literal(a, negated = True)
    clause = Clause([lit])

    s = Solver()
    s.add_clause(clause)

    s.check()
    assert s.model() == {a: False}

