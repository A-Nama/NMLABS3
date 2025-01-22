import sympy as sp

def newton_raphson():
    equation = input("Enter the funvtion (in terms of x) : ")
    
    x = sp.symbols('x')
    f = sp.sympify(equation)
    
    f_prime = sp.diff(f, x)
    
    guess = float(input("Enter initial guess : "))
    tolerance = float(input("Enter tolerance : "))
    max_iter = int(input("Enter the max no. of iterations : "))
    
    x_n = guess
    for i in range(max_iter):
        f_x = f.subs(x, x_n)
        f_prime_x = f_prime.subs(x, x_n)
        
        if abs(f_prime_x) < 1e-12:
            print("derivative too small ; method may not work.")
            return
        
        next_x = x_n - f_x / f_prime_x
        
        if abs(next_x - x_n) < tolerance:
            print(f"Root: {next_x}, found in {i+1} iterations.")
            return
        
        x_n = next_x
        
    print("Newton-Raphson method did not converge within no. of iterations.")
    
newton_raphson()