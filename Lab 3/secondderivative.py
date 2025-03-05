import math

def f(x):
    return math.exp(x)

def CDD(x,h):
    return ((f(x+h) - 2*f(x) + f(x-h))/(h**2))

x = 1
h = 0.01

CDD_val = CDD(x,h)

print("CDD value of f(x) is : ", CDD_val)