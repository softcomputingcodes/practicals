import numpy as np
import matplotlib.pyplot as plt

# Define x-axis
x = np.linspace(0, 10, 1000)

# 1. Triangular Membership Function
def trimf(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

# 2. Trapezoidal Membership Function
def trapmf(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x - a)/(b - a), 1), (d - x)/(d - c)), 0)

# 3. Gaussian Membership Function
def gaussmf(x, c, sigma):
    return np.exp(-((x - c)**2) / (2 * sigma**2))

# 4. Sigmoidal Membership Function
def sigmf(x, a, c):
    return 1 / (1 + np.exp(-a * (x - c)))

# 5. Bell-shaped Membership Function
def gbellmf(x, a, b, c):
    return 1 / (1 + np.abs((x - c) / a)**(2*b))

# 1️⃣ Triangular
plt.figure()
plt.plot(x, trimf(x, 2, 5, 8))
plt.title("Triangular Membership Function")
plt.xlabel("x")
plt.ylabel("μ(x)")
plt.grid(True)

# 2️⃣ Trapezoidal
plt.figure()
plt.plot(x, trapmf(x, 2, 4, 6, 8))
plt.title("Trapezoidal Membership Function")
plt.xlabel("x")
plt.ylabel("μ(x)")
plt.grid(True)

# 3️⃣ Gaussian
plt.figure()
plt.plot(x, gaussmf(x, 5, 1))
plt.title("Gaussian Membership Function")
plt.xlabel("x")
plt.ylabel("μ(x)")
plt.grid(True)

# 4️⃣ Sigmoidal
plt.figure()
plt.plot(x, sigmf(x, 1, 5))
plt.title("Sigmoidal Membership Function")
plt.xlabel("x")
plt.ylabel("μ(x)")
plt.grid(True)

# 5️⃣ Bell-shaped
plt.figure()
plt.plot(x, gbellmf(x, 2, 4, 5))
plt.title("Bell-shaped Membership Function")
plt.xlabel("x")
plt.ylabel("μ(x)")
plt.grid(True)

plt.show()
