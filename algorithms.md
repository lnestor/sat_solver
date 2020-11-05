This documents contains the algorithms implemented in this
repository.

Atoms
Literals
Clauses - Maybe saying obj == True creates a clause and that is what is passed
          then checking if something satisfies just iterates through every clause
          and checks if there is at least one that is true
Formula

# Algorithm 1: Naive Search

```
stack = Stack()
stack.push({choose_atom(), no assignments})

while stack is not empty:
  atom, assignments = stack.pop()

  if atom is nil:
    check_satisfiability()
  else:
    next_atom = choose_atom()
    stack.push(next_atom, assignments.merge(atom: True))
    stack.push(next_atom, assignments.merge(atom: False))
```

1. Decide on an atom to switch on
2. Assign that variable a value
3. Repeat until no variables left
4. Check if this satisfies the condition

# Algorithm 2: Actively checking satisfiability

```
stack = Stack()
stack.push({choose_atom(), no assignments})

while stack is not empty:
  atom, assignments = stack.pop()

  if check_satisfiability() == False:
    continue

  if atom is nil:
    check_satisfiability()
  else:
    next_atom = choose_atom()
    stack.push(next_atom, assignments.merge(atom: True))
    stack.push(next_atom, assignments.merge(atom: False))
```

1. Decide on an atom to switch on
2. Assign that variable a value
3. Check if the current model is satisfiable
4. If is is not, do not continue down that path
5. Repeat until no variables left

# Algorithm 3: Unit propagation

Do the same as algorithm 2, but do the double watched literal thing
