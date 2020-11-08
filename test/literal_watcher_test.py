from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.clause import Clause
from sat_solver.literal import Literal
from sat_solver.literal_watcher import LiteralWatcher

def test_inspect_with_conflicts_returns_conflicts():
    a = Bool("a")
    lit = Literal(a, negated = False)
    clause = Clause([lit])

    watcher = LiteralWatcher([clause])
    assignment = {a: False}
    _, conflicts = watcher.inspect(assignment)

    assert conflicts == {a: False}

def test_inspect_with_propagations_returns_propgations():
    a = Bool("a")
    b = Bool("b")
    lit_a = Literal(a, negated = False)
    lit_b = Literal(b, negated = False)
    clause = Clause([lit_a, lit_b])

    watcher = LiteralWatcher([clause])
    assignment = {a: False}
    propagations, _ = watcher.inspect(assignment)

    assert propagations == {b: True}


