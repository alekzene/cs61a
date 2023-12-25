from math import pi, sqrt
from operator import add
name = "Alexene"
print(3 * name)

# DOCTESTS & DEFAULT VALUES
def deliver(x, z, y=2):
    """Adds three input numbers.

    >>> deliver(2, 3, 4)
    9
    >>> deliver(4, 5)
    11
    """
    assert deliver(2, 3, 4) == 1, 'Number 2, 3, and 4 must deliver 1.'
    return add(y, x, z)

# HIGHER ORDER FUNCTIONS - Input
def square(r):
    return r * r

def area(r, constant):
    return square(r) * constant

def summation_identity(n):
    i, sum = 1, 0
    while i <= n:
        i, sum += 1, i
    return sum

def summation_cube(n):
    i, sum = 1, 0
    while i <= n:
        i = n * n * n
        i, sum += 1, i
    return sum

def identity(k):
    return k

def cube(k):
    return k * k * k

def summation(n, term_property):
    i, sum = 1, 0
    # while i <= n:

# HIGHER ORDER FUNCTIONS - Output
