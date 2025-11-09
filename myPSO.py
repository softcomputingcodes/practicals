"""
===============================================
   PARTICLE SWARM OPTIMIZATION (PSO) Algorithm
   Example: Minimizing the Rosenbrock Function
===============================================

# --- Algorithm Steps ---
1. Initialize a swarm of particles with:
   - Random positions p[i] within bounds.
   - Random velocities v[i].
2. Evaluate fitness f[i] for each particle using the objective function (Rosenbrock).
3. Set each particle’s best-known position (pbest) to its initial position.
4. Identify the global best particle (gbest) having the lowest fitness.
5. Repeat for a fixed number of iterations:
   a. For each particle:
      - Update velocity:
        v = w*v + c1*r1*(pbest - pos) + c2*r2*(gbest - pos)
      - Update position:
        pos = pos + v
      - Clip positions within bounds.
   b. Evaluate new fitness values.
   c. Update personal best (pbest) and global best (gbest).
6. Return the best position (solution) and its fitness value.

# --- Pseudocode ---
Initialize w, c1, c2, bounds, and number of particles N
For each particle i:
    Randomly initialize position p[i] and velocity v[i]
    Evaluate fitness f[i] = F(p[i])
    pbest[i] = p[i]
Set gbest = best(pbest)

For iteration t = 1 to max_iter:
    For each particle i:
        v[i] = w*v[i] + c1*r1*(pbest[i]-p[i]) + c2*r2*(gbest-p[i])
        p[i] = p[i] + v[i]
        Keep p[i] within bounds
        Evaluate fitness f[i]
        If f[i] < pbest_fitness[i]:
            pbest[i] = p[i]
    Update gbest as best of pbest
Output gbest and its fitness
"""
import numpy as np
import matplotlib.pyplot  as plt
def rosenbrock(x,y):
    return (1 - x)**2 + 100*(y - x**2)**2
    # return (1 - x)**2 + 100*(y - x**2)**2

w = 0.4
iter = 50
n = 20
c1 , c2 = 1.5, 1.5
b = (-5,5)

p = np.random.uniform(b[0],b[1],(n,2))
v = np.random.uniform(-1,1,(n,2))

pb = p.copy()
pf = np.array([rosenbrock(*x) for x in p])
best_index = np.argmin(pf)

gb = pb[best_index]
gf = np.min(pf)
best_fitness_each_iter = []

for t in range(iter):
    r1, r2 = np.random.rand(n,2), np.random.rand(n,2)
    v = w * v + c1*r1*(pb - p) + c2*r2*(gb - p)
    # v = w*v + c1*r1*(pb - p) + c2*r2*(gb - p)
    p = np.clip(p+v, b[0],b[1])

    fitness = np.array([rosenbrock(*x) for x in p])
    for i in range(n):
        if(fitness[i] < pf[i]):
            pf[i] = fitness[i]
            pb[i] = p[i].copy()
    
    best = np.argmin(pf)
    gb, gf = pb[best], pf[best]
    best_fitness_each_iter.append(gf)


    print(f"Iter {t+1}: Best = {gb}, Fitness = {gf:.6f}")

# --- Visualization: Convergence Graph ---
plt.figure(figsize=(8,5))
plt.plot(range(1, iter+1), best_fitness_each_iter, marker='o', color='blue')
plt.title("PSO Convergence Curve on Rosenbrock Function")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness Value")
plt.grid(True)
plt.show()
