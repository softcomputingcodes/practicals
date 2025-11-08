import numpy as np
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

    print(f"Iter {t+1}: Best = {gb}, Fitness = {gf:.6f}")

