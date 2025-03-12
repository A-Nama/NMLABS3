import numpy as np
def trapezoidal_rule(f,a,b,n):
    h = (b - a )/n
    x = np.linspace(a,b,n+1)
    y = f(x)
    
    integral = (h/2)*(y[0]+2*sum(y[1:n])+y[n])
    return integral

def f(x):
    return x**2 - 2*x

a=0
b=2
n=10

result = trapezoidal_rule(f,a,b,n)
print(f"Approximate integral: {result}")