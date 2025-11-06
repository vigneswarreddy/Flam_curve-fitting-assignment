import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
from scipy.optimize import least_squares

DATA_PATH = "xy_data.csv"

df = pd.read_csv(DATA_PATH)
x_obs = df["x"].to_numpy()
y_obs = df["y"].to_numpy()
n = len(df)

plt.figure()
plt.scatter(x_obs, y_obs, s=6)
plt.xlabel("x"); plt.ylabel("y"); plt.title("Scatter of provided (x, y) points")
plt.show()

t = np.linspace(6.0, 60.0, n)

def model_xy(t, theta, M, X):
    exp_term = np.exp(M * np.abs(t))
    sin03t = np.sin(0.3 * t)
    ct, st = np.cos(theta), np.sin(theta)
    x = t * ct - exp_term * sin03t * st + X
    y = 42 + t * st + exp_term * sin03t * ct
    return x, y

def residuals(params):
    theta, M, X = params
    if not (0 < theta < np.deg2rad(50) and -0.05 < M < 0.05 and 0 < X < 100):
        return np.ones(2*n) * 1e6
    x_hat, y_hat = model_xy(t, theta, M, X)
    return np.concatenate([x_hat - x_obs, y_hat - y_obs])

theta0 = np.deg2rad(25.0)
M0 = 0.0
X0 = 50.0
p0 = np.array([theta0, M0, X0])

lb = np.array([np.deg2rad(0.001), -0.0499, 0.001])
ub = np.array([np.deg2rad(49.999), 0.0499, 99.999])

res = least_squares(
    residuals, p0,
    bounds=(lb, ub),
    loss="soft_l1",
    f_scale=1.0,
    max_nfev=300,
    verbose=1
)

theta_hat, M_hat, X_hat = res.x
theta_deg = np.rad2deg(theta_hat)

x_fit, y_fit = model_xy(t, theta_hat, M_hat, X_hat)
L1_score = np.sum(np.abs(x_fit - x_obs) + np.abs(y_fit - y_obs))

print("\nEstimated parameters")
print(f"theta = {theta_hat:.6f} rad  (~ {theta_deg:.4f} deg)")
print(f"M     = {M_hat:.6f}")
print(f"X     = {X_hat:.6f}")
print(f"L1 objective (sum |dx|+|dy|): {L1_score:.6f}")
print(f"Optimizer message: {res.message}")

plt.figure()
plt.scatter(x_obs, y_obs, s=6, label="Observed")
plt.plot(x_fit, y_fit, linewidth=2, label="Fitted")
plt.xlabel("x"); plt.ylabel("y"); plt.title("Observed vs Fitted Curve")
plt.legend()
plt.show()

plt.figure()
plt.plot(t, np.abs(x_fit - x_obs) + np.abs(y_fit - y_obs))
plt.xlabel("t"); plt.ylabel("|dx| + |dy|")
plt.title("Pointwise L1 Error vs t")
plt.show()
