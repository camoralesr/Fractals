import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# Vertices of the equilateral triangle 
# -----------------------------------------------------
V = np.array([[0, 0], [300, 0], [150, 300*np.sqrt(3)/2]])

# -----------------------------------------------------
# Initial point
# -----------------------------------------------------
P = np.array([0.25, 0.25])

# -----------------------------------------------------
# Iterations and arrays
# -----------------------------------------------------
N = 1000000
x = np.zeros(N)
y = np.zeros(N)

# -----------------------------------------------------
# Chaos game algorithm
# -----------------------------------------------------
for k in range(N):
    i = np.random.randint(0, 3)
    P = P/2 + V[i]/2
    x[k] = P[0]
    y[k] = P[1]

# -----------------------------------------------------
# Scatter Plot
# -----------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x, y, s=1, color='black', linewidths=0, rasterized=True)
ax.text(0.03, 0.97, rf'$N = {N}$', transform=ax.transAxes,
         ha='left', va='top', fontsize=12)
ax.tick_params(axis='both', labelsize=14)
ax.set_aspect('equal')
plt.tight_layout()

# ----------------------------------------------------
# Figure format
# -----------------------------------------------------
plt.savefig("TS.pdf", format="pdf", bbox_inches="tight", dpi=800)
plt.show()