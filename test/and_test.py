from context import sat_solver

from sat_solver.and_op import And
from sat_solver.bool import Bool

def test_constructor_finds_atoms():
    a = Bool("a")
    b = Bool("b")

    op = And(a, b)

    assert op.atoms == {a, b}

def test_constructor_finds_nested_atoms():
    a = Bool("a")
    b = Bool("b")
    c = Bool("c")

    op = And(a, And(b, c))

    assert op.atoms == {a, b, c}
