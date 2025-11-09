# --- ALGORITHM (Simplified) ---

1. Initialize:
   - Set parameters α (pheromone importance), β (heuristic importance),
     ρ (evaporation rate), Q (pheromone quantity), number of ants, iterations.
   - Initialize pheromone levels τ on all paths.

2. For each iteration:
   a. For each ant:
      - Start from a random position.
      - Construct a solution by moving step by step using
        probability:
           P(i,j) = [τ(i,j)]^α * [η(i,j)]^β / Σ([τ(i,k)]^α * [η(i,k)]^β)
        where η(i,j) = heuristic value (e.g., 1 / cost(i,j)).
      - Evaluate the fitness (quality) of the solution.
   b. Update pheromones:
        τ(i,j) = (1 - ρ)*τ(i,j) + Σ(Δτ(i,j))
        where Δτ(i,j) = Q / fitness if path (i,j) is used by ant.
   c. Keep track of the best solution found so far.

3. After all iterations, return the best solution.

-----------------------------------------------
# --- PSEUDOCODE (Generic ACO) ---

Initialize parameters α, β, ρ, Q
Initialize pheromone levels τ[i][j]

For t = 1 to MaxIterations:
    For each ant k:
        Initialize empty solution
        While solution not complete:
            Compute transition probabilities P(i,j)
            Choose next state j based on P(i,j)
        Evaluate fitness of solution

    For each path (i,j):
        Evaporate pheromone: τ[i][j] = (1 - ρ) * τ[i][j]
        Add pheromone: τ[i][j] += Σ(Q / fitness_k) for all ants using (i,j)

    Update best solution if a better one is found
End For

Return best solution found


import numpy as np
import matplotlib.pyplot as plt

# Distance matrix between 5 cities
dist = np.array([
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
])

n = len(dist)
alpha = 1
beta = 2
rho = 0.5
Q = 100
iterations = 30
ants = 8

pheromone = np.ones((n, n))

best_length_track = []

def tour_length(tour):
    return sum(dist[tour[i]][tour[(i+1)%n]] for i in range(n))

for it in range(iterations):
    all_tours = []
    for _ in range(ants):
        unvisited = list(range(n))
        start = np.random.choice(unvisited)
        tour = [start]
        unvisited.remove(start)

        while unvisited:
            current = tour[-1]
            probs = []
            for city in unvisited:
                tau = pheromone[current][city] ** alpha
                eta = (1 / dist[current][city]) ** beta
                probs.append(tau * eta)

            probs = np.array(probs) / sum(probs)
            next_city = np.random.choice(unvisited, p=probs)
            tour.append(next_city)
            unvisited.remove(next_city)

        all_tours.append(tour)

    # Pheromone Evaporation
    pheromone *= (1 - rho)

    # Pheromone Update
    best_tour = min(all_tours, key=tour_length)
    best_len = tour_length(best_tour)
    best_length_track.append(best_len)

    for i in range(n):
        a, b = best_tour[i], best_tour[(i+1) % n]
        pheromone[a][b] += Q / best_len
        pheromone[b][a] += Q / best_len

print("Best Tour:", best_tour)
print("Shortest Distance:", best_len)

# Plotting convergence
plt.plot(best_length_track, marker='o')
plt.title("ACO Convergence")
plt.xlabel("Iteration")
plt.ylabel("Best Tour Length")
plt.grid(True)
plt.show()
