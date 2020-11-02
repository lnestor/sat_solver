from context import sat_solver

from sat_solver.not_op import Not
from sat_solver.bool import Bool

def test_constructor_finds_atoms():
    a = Bool("a")

    op = Not(a)

    assert op.atoms == {a}

def test_constructor_finds_nested_atoms():
    a = Bool("a")

    op = Not(Not(a))

    assert op.atoms == {a}

