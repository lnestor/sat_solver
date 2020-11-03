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
  - Need to figure out which atoms are in the equation
  - Choose at random
2. Assign that variable a value
  - Assign at random
3. Repeat until no variables left
4. Check if this satisfies the condition
