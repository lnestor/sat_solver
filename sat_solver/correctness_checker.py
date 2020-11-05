from bool import Bool
from literal import Literal
from clause import Clause
from naive_runner import NaiveRunner
from pruning_runner import PruningRunner

def build_formula():
    b1 = Bool("b1")
    b2 = Bool("b2")
    b3 = Bool("b3")
    b4 = Bool("b4")
    b5 = Bool("b5")
    b6 = Bool("b6")
    b7 = Bool("b7")
    b8 = Bool("b8")
    b9 = Bool("b9")
    b10 = Bool("b10")
    b11 = Bool("b11")
    b12 = Bool("b12")
    b13 = Bool("b13")
    b14 = Bool("b14")
    b15 = Bool("b15")
    b16 = Bool("b16")

    lit_b1 = Literal(b1, negated = False)
    lit_b2 = Literal(b2, negated = False)
    lit_b3 = Literal(b3, negated = False)
    lit_b4 = Literal(b4, negated = False)
    lit_b5 = Literal(b5, negated = False)
    lit_b6 = Literal(b6, negated = False)
    lit_b7 = Literal(b7, negated = False)
    lit_b8 = Literal(b8, negated = False)
    lit_b9 = Literal(b9, negated = False)
    lit_b10 = Literal(b10, negated = False)
    lit_b11 = Literal(b11, negated = False)
    lit_b12 = Literal(b12, negated = False)
    lit_b13 = Literal(b13, negated = False)
    lit_b14 = Literal(b14, negated = False)
    lit_b15 = Literal(b15, negated = False)
    lit_b16 = Literal(b16, negated = False)
    lit_b16_bar = Literal(b16, negated = True)
    lit_b15_bar = Literal(b15, negated = True)
    lit_b14_bar = Literal(b14, negated = True)
    lit_b11_bar = Literal(b11, negated = True)
    lit_b10_bar = Literal(b10, negated = True)
    lit_b9_bar = Literal(b9, negated = True)
    lit_b8_bar = Literal(b8, negated = True)
    lit_b7_bar = Literal(b7, negated = True)
    lit_b6_bar = Literal(b6, negated = True)
    lit_b5_bar = Literal(b5, negated = True)
    lit_b4_bar = Literal(b4, negated = True)
    lit_b2_bar = Literal(b2, negated = True)

    clause0 = Clause([lit_b1, lit_b2])
    clause1 = Clause([lit_b2_bar, lit_b4_bar])
    clause2 = Clause([lit_b3, lit_b4])
    clause3 = Clause([lit_b4_bar, lit_b5_bar])
    clause4 = Clause([lit_b5, lit_b6_bar])
    clause5 = Clause([lit_b6, lit_b7_bar])
    clause6 = Clause([lit_b6, lit_b7])
    clause7 = Clause([lit_b7, lit_b16_bar])
    clause8 = Clause([lit_b8, lit_b9_bar])
    clause9 = Clause([lit_b8_bar, lit_b14_bar])
    clause10 = Clause([lit_b9, lit_b10])
    clause11 = Clause([lit_b9, lit_b10_bar])
    clause12 = Clause([lit_b10_bar, lit_b11_bar])
    clause13 = Clause([lit_b10, lit_b12])
    clause14 = Clause([lit_b11, lit_b12])
    clause15 = Clause([lit_b13, lit_b14])
    clause16 = Clause([lit_b14, lit_b15_bar])
    clause17 = Clause([lit_b15, lit_b16])

    clause_list = [clause0, clause1, clause2, clause3, clause4, clause5, clause6, clause7, clause8, clause9, clause10, clause11, clause12, clause13, clause14, clause15, clause16, clause17]
    atom_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]

    return clause_list, atom_list

if __name__ == "__main__":
    clause_list, atom_list = build_formula()

    naive = NaiveRunner(clause_list, atom_list)
    pruning = PruningRunner(clause_list, atom_list)

    naive.run()
    naive_model = naive.extract()

    print("=== Naive Model ===")

    for atom in sorted(naive_model.keys(), key = lambda k: int(str(k)[1:])):
        print("%s: %s" % (atom, naive_model[atom]))

    pruning.run()
    pruning_model = pruning.extract()

    print("=== Pruning Model ===")
    for atom in sorted(pruning_model.keys(), key = lambda k: int(str(k)[1:])):
        print("%s: %s" % (atom, pruning_model[atom]))

