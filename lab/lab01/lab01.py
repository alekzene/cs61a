"""Lab 1: Expressions and Control Structures"""

def both_positive(a, b):
    """Returns True if both a and b are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return a > 0 and b > 0 # You can replace this line! (Update: Line replaced)

def sum_digits(x):
    """Sum all the digits of x.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    final_sum = 0
    length = len((str(x)))
    while length != 0:
        place = 10 ** (length - 1)
        digit = x // place
        x = x - (place * digit)
        final_sum += digit
        length -= 1 # Try removing this line and see if it would still work (a.k.a. while loop condition would also update 'x' value)
    return final_sum
    
print(sum_digits(10))

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    falling_factorial = n
    if k == 0:
        falling_factorial = 1
    else:
        while k > 1:
            falling_factorial *= (n - 1)
            n = n - 1
            k-=1
    return falling_factorial

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    isDoubleEight = True
    nString = str(n)
    if len(nString) == 1:
        isDoubleEight = False;
    else: 
        for i in range(len(nString)):
            if nString[i] == "8" and nString[i] == nString[i + 1]:
                isDoubleEight = True
                break;
            else:
                isDoubleEight = False
    return isDoubleEight