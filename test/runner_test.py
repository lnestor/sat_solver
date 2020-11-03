from context import sat_solver

from sat_solver.and_op import And
from sat_solver.bool import Bool
from sat_solver.not_op import Not
from sat_solver.runner import Runner

def test_run_when_unsatisfiable_returns_false():
    a = Bool("a")
    constraints = [And(a, Not(a))]
    atoms = constraints[0].atoms

    runner = Runner(constraints, atoms)

    assert runner.run() == False
