import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    n=len(b)
    x=np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    
    for iteration in range(max_iter):
        x_new = np.copy(x)
        
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j]*x[j] for j in range(i+1, n))
            x_new[i] = (b[i] - sum1 - sum2)/A[i][i]
            
        if np.linalg.norm(x_new -x, ord = np.inf) <tol:
            return x_new
        
        x = x_new
    raise ValueError("Gauss Seidel did not converge within maximum number of itearations.")


n = int(input("Enter the number of variables: "))

print("Enter the coefficient matrix (A) row wise: ")
A = [list(map(float, input().split())) for _ in range(n)]

print("Enter the constant terms (b): ")  
b = [int(input()) for _ in range(n)]

solution = gauss_seidel(A,b)    
print("Solution : ", solution) 
        
         