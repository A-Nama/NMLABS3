import math

def f(x):
    return math.exp(x)

def BDD(x,h):
    return ((f(x) - f(x-h))/h)

x = 1
h = 0.01

BDD_val = BDD(x,h)

print("BDD value of f(x) is : ", BDD_val)