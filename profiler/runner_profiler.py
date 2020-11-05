import timeit

def read_formula():
    with open("profiler/formula.txt") as f:
        return f.read()

def profile_algorithm1_runner():
    formula = read_formula()

    SETUP_CODE = """
from context import sat_solver
from sat_solver.algorithm1_runner import Algorithm1Runner
from sat_solver.bool import Bool
from sat_solver.literal import Literal
from sat_solver.clause import Clause
%s""" % (formula)


    TEST_CODE = """
runner = Algorithm1Runner(clause_list, atom_list)
runner.run()"""

    times = timeit.timeit(setup = SETUP_CODE, stmt = TEST_CODE, number = 1000)
    print(times)

def profile_algorithm2_runner():
    formula = read_formula()

    SETUP_CODE = """
from context import sat_solver
from sat_solver.algorithm2_runner import Algorithm2Runner
from sat_solver.bool import Bool
from sat_solver.literal import Literal
from sat_solver.clause import Clause
%s""" % (formula)


    TEST_CODE = """
runner = Algorithm2Runner(clause_list, atom_list)
runner.run()"""

    time = timeit.timeit(setup = SETUP_CODE, stmt = TEST_CODE, number = 1000)
    print(time)

if __name__ == "__main__":
    profile_algorithm1_runner()
    profile_algorithm2_runner()
