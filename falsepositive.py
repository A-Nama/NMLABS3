import sympy as sp

def falseposition(equation, a, b, max_iter):
    x = sp.symbols('x')
    f = sp.sympify(equation)
    
    if f.subs(x, a) * f.subs(x, b) > 0:
        print("The function must have opposite signs at a and b.")
        return None
    
    print(f"\nEquation: {equation}")
    print(f"Initial interval: [{a}, {b}]\n")
    
    for iteration in range(1, max_iter + 1):
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        
        c = (a * fb - b * fa) / (fb - fa)
        fc = f.subs(x, c)
        
        if abs(fc) < 1e-6 or abs(b - a)/2 < 1e-6:
            print(f"\nRoot found at x = {c:.6f}")
            return c
        
        if fa * fc < 0:
            b = c
        else:
            a = c

    print("\nMaximum iterations reached. Approximate root:")
    return (a * f.subs(x, b) - b * f.subs(x, a)) / (f.subs(x, b) - f.subs(x, a))


equation = input("Enter equation in terms of x: ")
a = float(input("Enter lower bound of the interval (a) : "))
b = float(input("Enter upper bound of the interval (b) : "))
max_iter = int(input("Enter maximum no. of iterations : "))

root = falseposition(equation, a, b, max_iter)
if root is not None:
    print(f"\nAPPROXIMATE ROOT: {root:.6f}")
