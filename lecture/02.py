# importing modules and functions
from math import pi, sin, pow

pi * 71 / 223
sin( pi / 2 )

# assigning variables
radius = 10
2 * radius
area, circ = pi * pow( radius, 2 ), 2 * pi * radius
# area: 314.159265359 circ: 62.8318530718
radius = 20

# function values
max # --> function name; different from max() which is a function call
max( 3, 4, 5 )
# f = max() --> doesn't work because the function needs arguments
f = max # works because i'm only using the function name to assign its value to f, not calling the actual function
f
f( 3, 4 )
max = 7
f( 3, 4 )
f( 3, max )
f = 2
# f( 3, 4 ) --> no longer works because f is no longer a function and is now an integer 2
max = __builtins__.max
max( 3, 2 ) # it works because i reassigned max to its original builtin max function

# user-defined functions
from operator import add, mul

def square( x ):
    return mul( x, x )

square( 21 )
square( add( 2, 5 ) )
square( square( 3 ) )

def sum_squares( x, y ):
    return add( square( x ), square( y ) )
    # a function can use other [user-defined] functions in its code-block

sum_squares( 3, 4 )
sum_squares( 5, 12 )

# area function
def area():
    return pi * radius * radius

area()
radius = 20
area()
radius = 10
area()
# the value of area() changes here it is a function
# it doesn't store values unlike area which does
# instead, the area() function returns values to variables like area to accommodate for more, upcoming values

# name conflicts
def square( square ) :
    return mul( square, square ) # changing this to square( square ) will throw an error [see line 64]

square( 4 ) # output: 16
# previous def square( x ) was overwritten by def square( square )
# function name can have the same name as the parameter name
