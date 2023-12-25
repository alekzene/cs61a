"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

# FIXME What is the difference between four_sided and four_sided()
print("Four-sided: ", four_sided) 
print("Four-sided: ", four_sided()) 

def make_test_dice(*outcomes): #FIXME What is a tuple?
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():  
        nonlocal index # FIXED What does the 'nonlocal' keyword mean? The 'nonlocal' keyword is attached to a variable name in the inner function that inherits the value of the same variable name from the outer function of the nested function.
        index = (index + 1) % len(outcomes) # FIXME I don't understand this part. LOGIC
        return outcomes[index] # FIXED I don't understand this part. SYNTAX: outcomes[index] The function returns the Nth item from the 'outcomes' list. N is represented by the 'index' variable. If the value of 'index' is 0, the dice() function wil return the first element in the 'outcomes' list due to zero-based indexing.
    return dice

# FIXME Quiz
# Why is the outcome for Case 1:
# test_case() 4?
# test_case() 1?
# test_case() 2?
# test_case() 4?
# Why is six_sided() the correct way to roll a fair six-sided dice and not make_fair_dice(6)?