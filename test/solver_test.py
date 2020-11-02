from context import sat_solver

from sat_solver.solver import Solver
from sat_solver.bool import Bool
from sat_solver.and_op import And
from sat_solver.not_op import Not

def test_check_when_unsatisfiable_returns_unsat():
    a = Bool("a")

    s = Solver()
    s.add(And(a, Not(a)))

    assert s.check() == "unsat"

def test_check_when_satisfiable_returns_sat():
    a = Bool("a")

    s = Solver()
    s.add(And(a, a))

    assert s.check() == "sat"

# Test multiple atoms
