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
    # Current point
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
ax.scatter(x, y, s=0.1)
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


# =====================================================
# FRACTAL DIMENSION: BOX COUNTING
# =====================================================

# -----------------------------------------------------
# Points
# -----------------------------------------------------
points = np.column_stack((x, y))

# -----------------------------------------------------
# Normalize the point cloud
# -----------------------------------------------------
points = points - np.min(points, axis=0)
Lx = np.max(points[:, 0])
Ly = np.max(points[:, 1])
L = max(Lx, Ly)
points = points / L

# -----------------------------------------------------
# Box sizes
# -----------------------------------------------------
epsilon = 1 / 2**np.arange(2, 9)
N_boxes = np.zeros(len(epsilon))

# -----------------------------------------------------
# Box counting algorithm
# -----------------------------------------------------
for j in range(len(epsilon)):
    eps = epsilon[j]
    # Box occupied by each point
    boxes = np.floor(points / eps).astype(int)
    # Number of different occupied boxes
    occupied_boxes = np.unique(boxes, axis=0)
    N_boxes[j] = len(occupied_boxes)

# -----------------------------------------------------
# Logarithmic variables
# -----------------------------------------------------
log_scale = np.log(1 / epsilon)
log_boxes = np.log(N_boxes)

# -----------------------------------------------------
# Linear fit
# -----------------------------------------------------
coefficients = np.polyfit(log_scale, log_boxes, 1)
df = coefficients[0]
intercept = coefficients[1]
fit = df*log_scale + intercept
print("Fractal dimension =", df)

# -----------------------------------------------------
# Box-counting plot
# -----------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(log_scale, log_boxes, s=20)
ax.plot(log_scale, fit, linewidth=1.5, label=rf'$d_f = {df:.4f}$')
ax.set_xlabel(r'$\ln(1/\varepsilon)$', fontsize=18)
ax.set_ylabel(r'$\ln N(\varepsilon)$', fontsize=18)
ax.tick_params(axis='both', labelsize=14)
ax.legend(fontsize=14)
plt.tight_layout()

# -----------------------------------------------------
# Figure format
# -----------------------------------------------------
plt.savefig("D(fern).pdf", format="pdf", bbox_inches="tight")
plt.show()