# Initialize population Xi (i = 1 to N)
# Initialize a, A, C coefficients
# Evaluate fitness of each search agent
# Identify Alpha (best), Beta (2nd best), Delta (3rd best)

# While (t < max_iterations):
#     For each wolf i:
#         Update coefficients A, C
#         Compute Dα = |C1*Xα - Xi|
#         Compute Dβ = |C2*Xβ - Xi|
#         Compute Dδ = |C3*Xδ - Xi|
        
#         X1 = Xα - A1*Dα
#         X2 = Xβ - A2*Dβ
#         X3 = Xδ - A3*Dδ
        
#         Update position Xi = (X1 + X2 + X3) / 3
#     End For
    
#     Update a = 2 - (2 * t / max_iterations)
#     Evaluate all fitness values
#     Update Xα, Xβ, Xδ based on new best solutions
#     Increment t
# End While

# Return Xα as the best (optimal) solution

import numpy as np
import matplotlib.pyplot as plt
def f(x) :
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

def gwo(f,n=10, iter = 100, lb=-5, ub=5):

    pos = np.random.uniform(lb,ub,(n,2))
    fit = np.array([f(x) for x in pos])

    alpha , beta, delta = np.zeros(2),np.zeros(2),np.zeros(2)
    fa,fb,fd = np.inf, np.inf, np.inf

    convergence = []  # store best fitness for plotting


    for t in range(iter):
        a = 2 - 2 * (t/iter)
        for i in range(n):
            for j in range(2):

                # For Alpha
                r1 = np.random.rand()
                r2 = np.random.rand()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                d1 = abs(C1*alpha[j] - pos[i][j])
                x1 = alpha[j] - A1 * d1

                # For Beta
                r1 = np.random.rand()
                r2 = np.random.rand()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                d2 = abs(C2*beta[j] - pos[i][j])
                x2 = beta[j] - A2 * d2

                # For Delta
                r1 = np.random.rand()
                r2 = np.random.rand()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                d3 = abs(C3*delta[j] - pos[i,j])
                x3 = delta[j] - A3 * d3

                pos[i][j] = np.clip((x1+x2+x3)/3,lb,ub)

        fit = np.array([f(x) for x in pos])
        for i in range(n):
            if fit[i] < fa:
                fd, delta = fb, beta.copy()
                fb, beta = fa, alpha.copy()
                fa, alpha = fit[i], pos[i].copy()
            elif fit[i] < fb:
                fd, delta = fb, beta.copy()
                fb, beta = fit[i], pos[i].copy()
            elif fit[i] < fd:
                fd, delta = fit[i], pos[i].copy()
        convergence.append(fa)

        if t % 10 == 0 or t == iter - 1:
            print(t+1, alpha, fa, sep='\t')
    print("\nFinal Best Wolf Position:", alpha)
    print("Minimum Value:", fa)

    plt.figure(figsize=(8,5))
    plt.plot(range(1, iter+1), convergence, marker='o', color='purple')
    plt.title("GWO Convergence Curve (Rosenbrock Function)")
    plt.xlabel("Iteration")
    plt.ylabel("Best Fitness (α)")
    plt.grid(True)
    plt.show()

gwo(f)
