import math
# First example
def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm arguments must be positive")
    return math.log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)