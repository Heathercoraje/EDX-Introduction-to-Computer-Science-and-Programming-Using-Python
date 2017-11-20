# function polysum takes 2 arguments and return the sum of area and square of the perimeter
# s is length n is number of sides
# make sure to import pan and pi from math library
from math import tan, pi


def square(l):
    return l*l

def polysum(n, s):
    p = s*n
    a = 0.25*n*square(s)/tan(pi/n)
    return round(square(p) + a, 4)
