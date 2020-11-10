import pytest

from context import sat_solver

from sat_solver.bool import Bool
from sat_solver.clause import Clause
from sat_solver.literal import Literal
from sat_solver.unit_propagator import UnitPropagator

def test_inspect_when_literal_not_watched_returns_none():
    bools = [Bool(name) for name in "abcd"]
    lits = [Literal(b, negated = False) for b in bools]
    clause = Clause(lits)
    propagator = UnitPropagator([clause])

    for b in bools:
        if not propagator.is_watched(b):
            atom, value = propagator.inspect(bools, {b: False}, b)

            assert atom is None
            assert value is None

            return

    raise RuntimeError("No unwatched literals")

def test_inspect_when_watched_literal_assigned_true_returns_none():
    bools = [Bool(name) for name in "abcd"]
    lits = [Literal(b, negated = False) for b in bools]
    clause = Clause(lits)
    propagator = UnitPropagator([clause])

    for b in bools:
        if propagator.is_watched(b):
            atom, value = propagator.inspect(bools, {b: True}, b)

            assert atom is None
            assert value is None

            return

    raise RuntimeError("No watched literals")

def test_insepct_when_watched_literal_assigned_false_not_unit_clause_returns_none():
    bools = [Bool(name) for name in "abcd"]
    lits = [Literal(b, negated = False) for b in bools]
    clause = Clause(lits)
    propagator = UnitPropagator([clause])

    for b in bools:
        if propagator.is_watched(b):
            # This will capture the first watched literal, so it is sure to
            # not be a unit clause
            atom, value = propagator.inspect(bools, {b: False}, b)

            assert atom is None
            assert value is None

            return

    raise RuntimeError("No watched literals")

def test_insepct_when_watched_literal_assigned_false_not_unit_clause_unwatches_literal():
    bools = [Bool(name) for name in "abcd"]
    lits = [Literal(b, negated = False) for b in bools]
    clause = Clause(lits)
    propagator = UnitPropagator([clause])

    for b in bools:
        if propagator.is_watched(b):
            # This will capture the first watched literal, so it is sure to
            # not be a unit clause
            atom, value = propagator.inspect(bools, {b: False}, b)

            watched = propagator.is_watched(b)
            assert not watched

            return

    raise RuntimeError("No watched literals")

def test_insepct_when_watched_literal_assigned_false_not_unit_clause_watches_another_literal():
    bools = [Bool(name) for name in "abcd"]
    lits = [Literal(b, negated = False) for b in bools]
    clause = Clause(lits)
    propagator = UnitPropagator([clause])

    init_watched = propagator.watched()

    for b in bools:
        if propagator.is_watched(b):
            # This will capture the first watched literal, so it is sure to
            # not be a unit clause
            atom, value = propagator.inspect(bools, {b: False}, b)

            final_watched = propagator.watched()
            assert len(final_watched) == len(init_watched)

            return

    raise RuntimeError("No watched literals")

def test_inspect_when_watched_literal_assigned_false_unit_clause_returns_unit_literal():
    bools = [Bool(name) for name in "abcd"]
    lits = [Literal(b, negated = False) for b in bools]
    clause = Clause(lits)
    propagator = UnitPropagator([clause])

    unassigned = bools.copy()
    model = {}

    for b in unassigned:
        if propagator.is_watched(b):
            # This will capture the first watched literal, so it is sure to
            # not be a unit clause
            model[b] = False
            atom, value = propagator.inspect(unassigned, model, b)
            unassigned.remove(b)
            break

    for b in unassigned:
        if propagator.is_watched(b):
            # This is the second watched literal assigned false, so it is sure
            # to not be a unit clause
            model[b] = False
            atom, value = propagator.inspect(unassigned, model, b)
            unassigned.remove(b)
            break

    for b in unassigned:
        if propagator.is_watched(b):
            # This is the third watched literal assigned false, so it finally
            # a unit clause
            model[b] = False
            atom, value = propagator.inspect(unassigned, model, b)

            unassigned.remove(b)
            last_atom = unassigned[0]

            assert atom == last_atom
            assert value == True

            return

    raise RuntimeError("No watched literals")

