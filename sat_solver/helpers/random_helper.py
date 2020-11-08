import random

def sample_or_all(i, n):
    if len(i) < n:
        return i
    else:
        return random.sample(i, n)
