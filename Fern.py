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
    if r < 0.02:
        P = np.array([0.5, 0.27*yn])
    elif r < 0.17:
        P = np.array([-0.139*xn + 0.263*yn + 0.57, 0.246*xn + 0.224*yn - 0.036])
    elif r < 0.30:
        P = np.array([0.17*xn - 0.215*yn + 0.408, 0.222*xn + 0.176*yn + 0.0893])
    else:
        P = np.array([0.781*xn + 0.034*yn + 0.1075, -0.032*xn + 0.739*yn + 0.27])
    x[n] = P[0]
    y[n] = P[1]

# -----------------------------------------------------
# Scatter Plot
# -----------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 9))
ax.scatter(x, y, s=0.1, color='green', linewidths=0, rasterized=True)
ax.text(0.03, 0.97, rf'$N = {N}$', transform=ax.transAxes,
         ha='left', va='top', fontsize=12)
ax.tick_params(axis='both', labelsize=14)
ax.set_aspect('equal')
plt.tight_layout()

# ----------------------------------------------------
# Figure format
# -----------------------------------------------------
plt.savefig("ferm.pdf", format="pdf", bbox_inches="tight", dpi=800)
plt.show()