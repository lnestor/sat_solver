This documents contains the algorithms implemented in this
repository.

Atoms
Literals
Clauses - Maybe saying obj == True creates a clause and that is what is passed
          then checking if something satisfies just iterates through every clause
          and checks if there is at least one that is true
Formula

# Algorithm 1: Naive Search

1. Decide on an atom to switch on
2. Assign that variable a value
3. Repeat until no variables left
4. Check if this satisfies the condition

# Algorithm 2: Actively checking satisfiability

1. Decide on an atom to switch on
2. Assign that variable a value
3. Check if the current model is satisfiable
4. If is is not, do not continue down that path
5. Repeat until no variables left
