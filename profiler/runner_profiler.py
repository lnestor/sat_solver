import timeit

def read_formula():
    with open("profiler/formula.txt") as f:
        return f.read()

def profile_naive_runner():
    formula = read_formula()

    SETUP_CODE = """
from context import sat_solver
from sat_solver.naive_runner import NaiveRunner
from sat_solver.bool import Bool
from sat_solver.literal import Literal
from sat_solver.clause import Clause
%s""" % (formula)


    TEST_CODE = """
runner = NaiveRunner(clause_list, atom_list)
runner.run()"""

    times = timeit.timeit(setup = SETUP_CODE, stmt = TEST_CODE, number = 1000)
    print(times)

def profile_pruning_runner():
    formula = read_formula()

    SETUP_CODE = """
from context import sat_solver
from sat_solver.pruning_runner import PruningRunner
from sat_solver.bool import Bool
from sat_solver.literal import Literal
from sat_solver.clause import Clause
%s""" % (formula)


    TEST_CODE = """
runner = PruningRunner(clause_list, atom_list)
runner.run()"""

    time = timeit.timeit(setup = SETUP_CODE, stmt = TEST_CODE, number = 1000)
    print(time)

if __name__ == "__main__":
    profile_naive_runner()
    profile_pruning_runner()
