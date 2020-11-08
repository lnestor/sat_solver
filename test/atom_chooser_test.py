from context import sat_solver

from sat_solver.atom_chooser import AtomChooser
from sat_solver.bool import Bool

def test_choose_returns_atom():
    atoms = [Bool("a"), Bool("b"), Bool("c")]
    chooser = AtomChooser(atoms)
    chosen = chooser.choose(0)
    assert chosen in atoms

def test_choose_when_given_same_depth_returns_same_atom():
    atoms = [Bool("a"), Bool("b"), Bool("c")]
    chooser = AtomChooser(atoms)
    chosen = chooser.choose(0)
    next_chosen = chooser.choose(0)
    assert next_chosen == chosen

def test_choose_when_no_atoms_left_returns_none():
    atoms = [Bool("a")]
    chooser = AtomChooser(atoms)
    chooser.choose(0)
    chosen = chooser.choose(1)
    assert chosen is None






