import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# Initial point
# -----------------------------------------------------
P = np.array([0.5, 0])

# -----------------------------------------------------
# Iterations and arrays
# -----------------------------------------------------
N = 1000000
x = np.zeros(N)
y = np.zeros(N)

# -----------------------------------------------------
# Barnsley fern algorithm
# -----------------------------------------------------
for n in range(N):
    r = np.random.random()
    xn = P[0]
    yn = P[1]
    if r < 0.5:
        P = np.array([(xn - yn)/2, (xn + yn)/2])
    else:
        P = np.array([1 - (xn + yn)/2, (xn - yn)/2])
    x[n] = P[0]
    y[n] = P[1]

# -----------------------------------------------------
# Scatter Plot
# -----------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x, y, s=0.05, color='blue', linewidths=0, rasterized=True)
ax.text(0.03, 0.97, rf'$N = {N}$', transform=ax.transAxes,
         ha='left', va='top', fontsize=12)
ax.tick_params(axis='both', labelsize=14)
ax.set_aspect('equal')
plt.tight_layout()

# ----------------------------------------------------
# Figure format
# -----------------------------------------------------
plt.savefig("dragon.pdf", format="pdf", bbox_inches="tight", dpi=800)
plt.show()