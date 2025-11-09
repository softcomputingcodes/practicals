import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Step 1: Define Fuzzy Relations
# ----------------------------

# Relation R: Temperature (A) → Soil Moisture (B)
R = np.array([
    [0.9, 0.7, 0.2],  # Low temp → mostly dry/normal
    [0.4, 0.8, 0.6],  # Medium temp → balanced
    [0.1, 0.5, 0.9]   # High temp → tends to wet
])

# Relation S: Soil Moisture (B) → Crop Suitability (C)
S = np.array([
    [0.8, 0.2, 0.6],  # Dry soil best for Wheat/Maize
    [0.7, 0.5, 0.7],  # Normal soil moderate for all
    [0.3, 0.9, 0.5]   # Wet soil best for Rice
])

# ----------------------------
# Step 2: Max–Min Composition
# ----------------------------

rows_R, cols_R = R.shape
rows_S, cols_S = S.shape

T_maxmin = np.zeros((rows_R, cols_S))

for i in range(rows_R):
    for j in range(cols_S):
        mins = [min(R[i][k], S[k][j]) for k in range(cols_R)]
        T_maxmin[i][j] = max(mins)

# ----------------------------
# Step 3: Min–Max Composition
# ----------------------------

T_minmax = np.zeros((rows_R, cols_S))

for i in range(rows_R):
    for j in range(cols_S):
        maxs = [max(R[i][k], S[k][j]) for k in range(cols_R)]
        T_minmax[i][j] = min(maxs)

# ----------------------------
# Step 4: Display Results
# ----------------------------
print("Fuzzy Relation R (Temperature → Moisture):")
print(R)
print("\nFuzzy Relation S (Moisture → Crop):")
print(S)
print("\nResultant Relation (Max–Min Composition):")
print(T_maxmin)
print("\nResultant Relation (Min–Max Composition):")
print(T_minmax)

labels_A = ["Low Temp", "Medium Temp", "High Temp"]
labels_C = ["Wheat", "Rice", "Maize"]

print("\nInterpretation (Crop suitability based on temperature):")
for i in range(len(labels_A)):
    print(f"{labels_A[i]} → Wheat={T_maxmin[i][0]:.2f}, Rice={T_maxmin[i][1]:.2f}, Maize={T_maxmin[i][2]:.2f}")

# ----------------------------
# Step 5: Graph Visualization
# ----------------------------
x = np.arange(len(labels_A))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, T_maxmin[:, 0], 'o-', label="Wheat")
plt.plot(x, T_maxmin[:, 1], 'o-', label="Rice")
plt.plot(x, T_maxmin[:, 2], 'o-', label="Maize")
plt.xticks(x, labels_A)
plt.title("Max–Min Composition")
plt.xlabel("Temperature")
plt.ylabel("Membership Value")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, T_minmax[:, 0], 'o--', label="Wheat")
plt.plot(x, T_minmax[:, 1], 'o--', label="Rice")
plt.plot(x, T_minmax[:, 2], 'o--', label="Maize")
plt.xticks(x, labels_A)
plt.title("Min–Max Composition")
plt.xlabel("Temperature")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
