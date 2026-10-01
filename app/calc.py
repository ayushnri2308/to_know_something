def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n):
    return n % 2 == 0

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def power(a, b):
    if b < 0:
        raise ValueError("neg")
    r = 1
    for _ in range(b):
        r *= a
    return r
