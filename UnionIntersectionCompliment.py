
# # --- 1️⃣ UNION (A ∪ B) ---
# Used to combine two fuzzy sets (e.g., Slow speed & Fast speed).
# Union takes the **maximum** membership value at each element.

# Algorithm:
# 1. Define two fuzzy sets with membership functions μA(x) and μB(x).
# 2. For each element x in the universe:
#       μ(A ∪ B)(x) = max( μA(x), μB(x) )
# 3. Classify elements based on which membership is higher.
# 4. Plot all three:
#       - μA(x): Set A
#       - μB(x): Set B
#       - μ(A ∪ B)(x): Union (dashed line)

# Pseudocode:
# ----------------------------------
# for each x in X:
#     a = μA(x)
#     b = μB(x)
#     μ_union(x) = max(a, b)
# Display or plot μ_union(x)
# ----------------------------------


# # --- 2️⃣ INTERSECTION (A ∩ B) ---
# Used to find the common region between two fuzzy sets.
# Intersection takes the **minimum** membership value at each element.

# Algorithm:
# 1. Define two fuzzy sets with membership functions μA(x) and μB(x).
# 2. For each element x in the universe:
#       μ(A ∩ B)(x) = min( μA(x), μB(x) )
# 3. Identify which set (A or B) dominates for each x.
# 4. Plot μA(x), μB(x), and μ(A ∩ B)(x).

# Pseudocode:
# ----------------------------------
# for each x in X:
#     a = μA(x)
#     b = μB(x)
#     μ_intersection(x) = min(a, b)
# Display or plot μ_intersection(x)
# ----------------------------------


# # --- 3️⃣ COMPLEMENT (A') ---
# Shows the degree to which an element does **not belong** to a fuzzy set.
# Complement takes the **1 minus membership** of each element.

# Algorithm:
# 1. Define fuzzy set A with membership function μA(x).
# 2. For each element x:
#       μ(A')(x) = 1 - μA(x)
# 3. Plot both:
#       - μA(x): Original set
#       - μ(A')(x): Complement (A’)

# Pseudocode:
# ----------------------------------
# for each x in X:
#     μ_complement(x) = 1 - μA(x)
# Display or plot μA(x) and μ_complement(x)
# ----------------------------------
# Union 

def muSlow(s):
    if s<=20:
        return 1
    elif s <= 60:
        return (60-s) / 40
    else:
        return 0

def muFast(s):
    if s<60:
        return 0
    elif s < 100:
        return (s-60) / 40
    else:
        return 1

def getClass(a,b):
    if a>b:
        return 'Slow'
    elif a<b:
        return 'fast'
    else:
        return 'Neutral'

speeds = [20,30,40,50,60,70,80]

for s in speeds:
    a = muSlow(s)
    b = muFast(s)
    print(s,round(a,2),round(b,2),round(max(a,b),2),getClass(a,b),sep='\t')


import matplotlib.pyplot as plt

x = range(0,101)
plt.plot(x, [muSlow(i) for i in x])
plt.plot(x, [muFast(i) for i in x])
plt.plot(x, [min(muSlow(i), muFast(i)) for i in x], '--')
plt.show()



# Intersection 
import matplotlib.pyplot as plt
import numpy as np

# Membership function for "Slow Speed" fuzzy set (Set A)
def mu_slow(speed):
    if speed <= 20:
        return 1.0
    elif 20 < speed <= 60:
        return (60.0 - speed) / 40.0
    else:
        return 0.0

# Membership function for "Fast Speed" fuzzy set (Set B)
def mu_fast(speed):
    if speed < 60:
        return 0.0
    elif 60 <= speed < 100:
        return (speed - 60.0) / 40.0
    else:
        return 1.0

# Main
if __name__ == "__main__":
    speeds = [20, 40, 60, 80, 100]

    # Print table
    print("Speed\tMF(A) (Slow)\tMF(B) (Fast)\tMF(Intersection)")
    for s in speeds:
        muA = mu_slow(s)
        muB = mu_fast(s)
        muIntersection = min(muA, muB)  # Intersection mai min
        print(f"{s}km/h\t{muA:.2f}\t\t{muB:.2f}\t\t{muIntersection:.2f}")

    # Generate smooth values for graph
    x = np.linspace(0, 120, 200)
    muA_vals = [mu_slow(i) for i in x]
    muB_vals = [mu_fast(i) for i in x]
    muIntersection_vals = [min(a, b) for a, b in zip(muA_vals, muB_vals)]

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(x, muA_vals, label="Slow Speed (Set A)", linewidth=2)
    plt.plot(x, muB_vals, label="Fast Speed (Set B)", linewidth=2)
    plt.plot(x, muIntersection_vals, label="Intersection (A ∩ B)", linestyle="--", linewidth=2)

    plt.title("Fuzzy Intersection of Speed")
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Membership Value")
    plt.legend()
    plt.grid(True)
    plt.show()


# Compliment
import numpy as np
import matplotlib.pyplot as plt

# Define blood sugar range (mg/dL)
x = np.linspace(70, 200, 300)

# --- Fuzzy set: "High Blood Sugar" ---
# Using a smooth membership function (sigmoid)
def high_blood_sugar(x):
    return 1 / (1 + np.exp(-0.1 * (x - 130)))  # midpoint ~130 mg/dL

# --- Complement fuzzy set: "Not High Blood Sugar" ---
def not_high_blood_sugar(x):
    return 1 - high_blood_sugar(x)

# Calculate memberships
mu_high = high_blood_sugar(x)
mu_not_high = not_high_blood_sugar(x)

# --- Visualization ---
plt.figure(figsize=(8, 5))
plt.plot(x, mu_high, label="High Blood Sugar (A)", color='red', linewidth=2)
plt.plot(x, mu_not_high, label="Not High Blood Sugar (A')", color='green', linewidth=2, linestyle='--')

plt.title("Fuzzy Complement Operation: Medical Diagnosis System", fontsize=12)
plt.xlabel("Blood Sugar Level (mg/dL)")
plt.ylabel("Membership Value (μ)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
