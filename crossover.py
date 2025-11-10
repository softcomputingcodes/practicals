import random

# 🔹 Step 1: Take number of genes
n = int(input("Enter number of genes in each parent: "))

# 🔹 Step 2: Take genes for both parents
parent1 = list(map(int, input(f"Enter {n} genes for Parent 1 (space separated): ").split()))
parent2 = list(map(int, input(f"Enter {n} genes for Parent 2 (space separated): ").split()))

# Check if valid input
if len(parent1) != n or len(parent2) != n:
    print("❌ Error: Number of genes entered doesn't match the specified count!")
    exit()

print("\nParent 1:", parent1)
print("Parent 2:", parent2)

# 1️⃣ SINGLE POINT CROSSOVER
def single_point_crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    # Split both parents at the same point and swap tails
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    print(f"👉 Crossover point: {point}")
    return child1, child2

# 2️⃣ TWO POINT CROSSOVER
def two_point_crossover(p1, p2):
    pt1, pt2 = sorted(random.sample(range(1, len(p1) - 1), 2))
    # Swap middle segment
    child1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
    child2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:]
    print(f"👉 Crossover points: {pt1}, {pt2}")
    return child1, child2

# 3️⃣ ORDER CROSSOVER (OX)
def order_crossover(p1, p2):
    start, end = sorted(random.sample(range(len(p1)), 2))
    child = [None] * len(p1)
    child[start:end] = p1[start:end]
    print(f"👉 Order crossover slice: from index {start} to {end}")

    # Fill remaining positions with genes from parent2 in order (no duplicates)
    remaining = [x for x in p2 if x not in child]
    j = 0
    for i in range(len(p1)):
        if child[i] is None:
            child[i] = remaining[j]
            j += 1
    return child

# 4️⃣ UNIFORM CROSSOVER
def uniform_crossover(p1, p2):
    child1, child2 = [], []
    print("👉 Bit mask:", end=" ")
    for i in range(len(p1)):
        bit = random.choice([0, 1])  # 0 means take from p1, 1 means take from p2
        print(bit, end=" ")
        if bit == 0:
            child1.append(p1[i])
            child2.append(p2[i])
        else:
            child1.append(p2[i])
            child2.append(p1[i])
    print()
    return child1, child2

# ✳️ Apply all crossover techniques
print("\n--- SINGLE POINT CROSSOVER ---")
c1, c2 = single_point_crossover(parent1, parent2)
print("Child 1:", c1)
print("Child 2:", c2)

print("\n--- TWO POINT CROSSOVER ---")
c1, c2 = two_point_crossover(parent1, parent2)
print("Child 1:", c1)
print("Child 2:", c2)

print("\n--- ORDER CROSSOVER ---")
c = order_crossover(parent1, parent2)
print("Child:", c)

print("\n--- UNIFORM CROSSOVER ---")
c1, c2 = uniform_crossover(parent1, parent2)
print("Child 1:", c1)
print("Child 2:", c2)
