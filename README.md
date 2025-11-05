# 📌 Parametric Curve Parameter Estimation Assignment

This repository contains my solution to the curve-fitting assignment where the goal is to estimate the unknown parameters **θ, M, X** in a given parametric equation using real sample data.

---

## ✅ Problem Overview

We are given the following parametric curve:

\[
x(t) = \left( t \cdot \cos(\theta) - e^{M|t|} \cdot \sin(0.3t)\sin(\theta) + X \right)
\]

\[
y(t) = \left( 42 + t \cdot \sin(\theta) + e^{M|t|} \cdot \sin(0.3t)\cos(\theta) \right)
\]

The unknown parameters to estimate are:

\[
\theta,\; M,\; X
\]

with constraints:

| Parameter | Range |
|-----------|--------|
| \(0^\circ < \theta < 50^\circ\) |
| \(-0.05 < M < 0.05\) |
| \(0 < X < 100\) |
| Data sampled over \(6 < t < 60\) |

Input data file: **`xy_data.csv`**

---

## 🧠 Final Estimated Parameters

Using constrained optimization (SciPy `least_squares` with soft-L1 loss):

Estimated parameters
theta = 0.485100 rad  (~ 27.7942 deg)
M     = 0.020252
X     = 54.809307
L1 objective (sum |dx|+|dy|): 37867.660754


### ✅ Final Parametric Curve (Latex Format — required by assignment)

x(t) = ( tcos(0.485100) - e^(0.020252|t|) * sin(0.3t) * sin(0.485100) + 54.809307 )
y(t) = ( 42 + tsin(0.485100) + e^(0.020252|t|) * sin(0.3t) * cos(0.485100) )


---

## 🔍 Desmos Verification (optional but recommended)

🔗 **Live Desmos Graph:** *(replace this placeholder with your link)*  
`https://www.desmos.com/calculator/XXXXXXXXXX`

---

## 📊 Results & Visualizations

| Plot | File |
|-------|------|
| Observed data vs fitted curve | `results/fitted_curve.png` |
| Pointwise L1 error vs t | `results/l1_error_plot.png` |

Example preview:

#### ✅ Observed vs Fitted Curve  
*(insert image in repo)*

#### ✅ L1 Error vs t  
*(insert image in repo)*

---

## 🛠️ Method / Approach

1. Loaded the observed (x, y) points from `xy_data.csv`
2. Visualized the data to confirm shape and continuity
3. Mapped the row index to a parametric value `t ∈ [6, 60]`
4. Defined `x(t)` and `y(t)` functions in Python using NumPy
5. Minimized the following L1-based objective:

\[
\sum_{i=1}^{N} \left( |x_i - \hat{x_i}| + |y_i - \hat{y_i}| \right)
\]

6. Used `scipy.optimize.least_squares` with:
   - bounded parameters
   - soft-L1 loss (robust to outliers)
7. Computed true L1 after optimization
8. Plotted fitted curve and residuals

---

## ▶️ How to Run the Code

```bash
git clone https://github.com/<your-username>/curve-fitting-assignment
cd curve-fitting-assignment
pip install -r requirements.txt
python fit_curve.py
