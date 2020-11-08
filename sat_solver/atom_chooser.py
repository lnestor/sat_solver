import random

class AtomChooser():
    def __init__(self, atoms):
        self.unchosen = atoms.copy()
        self.chosen = []

    def choose(self, frame_depth):
        """Choose an atom from a list of atoms randomly.

        Once an atom is chosen, it will not be chosen again.

        Args:
            frame_depth: The depth of the current frame in the search tree.
                This depth maps to an atom chosen. If an atom has already
                been chosen for this depth, then that atom is returned. If not,
                then a new atom is chosen.

        Returns:
            atom: The next atom to be explored. If an atom has been chosen for
                the depth already, that atom is returned. If an atom has not
                been chosen for the depth, a new atom is chosen. If there are
                no more atoms to be chosen, None is returned.

        """
        if len(self.chosen) > frame_depth:
            return self.chosen[frame_depth]
        elif len(self.unchosen) == 0:
            return None
        else:
            atom = random.sample(self.unchosen, 1)[0]
            self.unchosen.remove(atom)
            self.chosen.append(atom)
            return atom
