import math

def f(x):
    return math.sin(x)

def CDD(x,h):
    return ((f(x+h) - f(x-h))/(2*h))

x = math.pi/4
h = 0.05

CDD_val = CDD(x,h)

print("CDD value of f(x) is : ", CDD_val)