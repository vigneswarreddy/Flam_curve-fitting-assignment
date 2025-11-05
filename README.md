# Flam_curve-fitting-assignment
Parametric Curve Parameter Estimation Assignment
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

