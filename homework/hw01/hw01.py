""" Homework 1: Control """

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = add # correct: binds h to the add function itself
        # neither ( a + b ) nor add( a, b ) worked because they bind h to the integer 2
        # and an integer cannot be used as an operator [ see line 24 ]
    else:
        h = sub
        # ( a + -b ) doesn't work for the same reasons mentioned above
    return h(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return ( ( x * x ) + ( y * y ) + ( z * z ) ) - ( max( x, y, z ) * max( x, y, z ) )

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i = x - 1
    while ( i > 0 ):
        if ( x % i == 0 ):
            print( i )
            break
        else:
            i -= 1 # if this is i = i - 1, why does the minus (-) operator come first instead of =-

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
    
# QUESTION : How did with_if_function return both 5 and 6?

def with_if_statement():
    """
    >>> result = with_if_statement()
    6
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    5
    6
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    3 > 5

def t():
    "*** YOUR CODE HERE ***"
    print( 5 )

    # QUESTION: What happens when I return a value to a function?

def f():
    "*** YOUR CODE HERE ***"
    print( 6 )

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    print( x )
    while( x > 1 ):
        if( x % 2 == 0 ):
            x = x // 2 # TIP : use floor division ( // ) instead of true division ( / ) to remove decimal points
        else:
            x = ( x * 3 ) + 1
        count += 1
        print( x )

    return count
