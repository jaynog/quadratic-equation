# -*- coding: utf-8 -*-
"""
The program should print two roots of the quadratic equation of the form

a x² + b x + c = 0

The roots must be stored in a tuple named 'solutions' and printed at the very end of the program.
"""

# This is sample input data

a = 1
b = 3
c = 2

# This is a tuple for results. You should override it with actual results

solutions = ()

# DO NOT CHANGE ANYTHING ABOVE THIS LINE!!!


# Put your here...
delta = b**2 - (4 * a * c)
if( a == 0 ):
    x0 = (-c / b)
    solutions = (x0, )
else:
    if delta > 0:
        sqdelta = delta**0.5
        x1 = (sqdelta - b) / (2 * a)
        x2 = (-sqdelta - b) / (2 * a)
        solutions = (x1, x2)
    elif delta < 0:
        solutions = ()
    else:
        x = -b / (2 * a)
        solutions = (x, )
# napisane na iPhone 


# At the end, the results are printed to the screen
print(*solutions)
