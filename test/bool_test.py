from context import sat_solver

from sat_solver.bool import Bool

def test_bool_name_properly_assigned():
    a = Bool("a")

    assert a.name == "a"
