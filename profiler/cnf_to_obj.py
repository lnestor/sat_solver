"""
This file converts a .cnf file into the format expected by our SAT solver
"""

if __name__ == "__main__":
    literals = set()
    clauses = []

    with open("profiler/formula.cnf") as f:
        for i in range(3):
            # Skip header
            f.readline()

        clauses = [l.rstrip().split()[0:-1] for l in f.readlines()]

        for clause in clauses:
            for literal in clause:
                literals.add(int(literal))

    atoms = set()

    for literal in literals:
        atoms.add(abs(literal))

    with open("profiler/formula.txt", "w") as f:
        for atom in atoms:
            f.write('b%s = Bool("b%s")\n' % (atom, atom))

        f.write("\n")

        for literal in literals:
            if literal > 0:
                f.write('lit_b%s = Literal(b%s, negated = False)\n' % (literal, literal))
            else:
                f.write('lit_b%s_bar = Literal(b%s, negated = True)\n' % (abs(literal), abs(literal)))

        f.write("\n")

        clause_names = []
        for i, clause in enumerate(clauses):
            l_str = []
            for l in clause:
                if int(l) > 0:
                    l_str.append("lit_b%s" % (l))
                else:
                    l_str.append("lit_b%s_bar" % (abs(int(l))))

            f.write("clause%i = Clause([%s])\n" % (i, ", ".join(l_str)))
            clause_names.append("clause%i" % (i))

        f.write("\n")

        to_write = "clause_list = %s\n" % (clause_names)
        f.write(to_write.replace("'", ""))

        to_write_atoms = "atom_list = %s" % (["b%s" % (a) for a in atoms])
        f.write(to_write_atoms.replace("'", ""))
