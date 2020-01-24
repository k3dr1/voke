from math import *
from sympy import *

while True:
    l = input("Your function (like x**2; 2**x; 1/x + 1; etc): \n")
    x = symbols("x")
    funct = Lambda(x, l)
    deriv = Lambda(x, diff(l))

    n = float(input("Give us any arbitrary value (x0): \n"))

    for w in range(100):
        n = n - (funct(n)/deriv(n))

    print(n)