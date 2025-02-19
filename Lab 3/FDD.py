def f(x):
    return x**3 + 2*x**2 - 5*x + 7

def FDD(x,h):
    return ((f(x+h) - f(x))/h)

x = 2
h = 0.1

FDD_val = FDD(x,h)

print("FDD value of f(x) is : ", FDD_val)