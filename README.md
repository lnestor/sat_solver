# A Poor Person's SAT Solver

This repository contains a basic implementation of a SAT solver. It uses the DPLL ( Davis–Putnam–Logemann–Loveland) algorithm

## Installation

[Python](https://www.python.org) is required to run this SAT attack.

Install all dependencies using the package manager [pip](https://pip.pypa.io/en/stable/).

```
pip install -r requirements.txt
```

## Description

A boolean satisfiability problem seeks to find inputs of a boolean formula
that produce a desired set of outputs. The primary algorithm used to do this
in modern SAT solvers is the DPLL algorithm. This is a modified depth-first
search of a tree where each edge represents an assignement to a variable
and each node represents the next variable to be assigned.

The distinguishing features of the DPLL algorithm from a depth-first search
are unit propagation and pure-literals. When a clause of the CNF formula has
all but one literal assigned false, it is called a unit clause. The remaining,
unassigned literal must be true in order for the formula to be satisfied.
This result can be propagated through the rest of the clauses. A pure literal
is when an atom appears in the formula in only one polarity. This atom can be
assigned such that the one polarity is always true.

The DPLL algorithm iterative assigns values to variables while looking for
unit clauses and pure literals. If a satisfying set of inputs is found, the
solver can return sat. If there is no such satisfying set, then the solver
can return unsat.

## Future Improvements

* Finish implementing all 5 algorithms
* Add timing analysis to easily determine when an algorithm is faster
* Support different atom selection schemes
* Convert traditional circuit elemnts (AND, XOR, etc.) to CNF
