# 📌 Parametric Curve Parameter Estimation Assignment

This repository contains my solution to the curve-fitting assignment where the goal is to estimate the unknown parameters **θ, M, X** in a given parametric equation using real sample data.

---

## ✅ Problem Overview

We are given the following **parametric curve equations**:

$$
x(t) = \left( t \cdot \cos(\theta) - e^{M|t|} \cdot \sin(0.3t)\sin(\theta) + X \right)
$$

$$
y(t) = \left( 42 + t \cdot \sin(\theta) + e^{M|t|} \cdot \sin(0.3t)\cos(\theta) \right)
$$

The unknown parameters to estimate are:

$$
\theta,\; M,\; X
$$

with the following bounds:

| Parameter | Range |
|-----------|--------|
| $$0^\circ < \theta < 50^\circ$$ |
| $$-0.05 < M < 0.05$$ |
| $$0 < X < 100$$ |
| Data sampled over: $$6 < t < 60$$ |

Input data file: **`xy_data.csv`**

---

## 🧠 Final Estimated Parameters

Using constrained optimization (`scipy.optimize.least_squares` with soft-L1 loss), the estimated parameters are:


θ = 0.485100 rad ≈ 27.7942°

M = 0.020252

X = 54.809307

L1 objective = 37867.660754



---

## ✅ Final Parametric Curve (Required LaTeX Submission Format)

$$
x(t) = \left( t\cos(0.485100) \;-\; e^{0.020252|t|}\sin(0.3t)\sin(0.485100) \;+\; 54.809307 \right)
$$

$$
y(t) = \left( 42 \;+\; t\sin(0.485100) \;+\; e^{0.020252|t|}\sin(0.3t)\cos(0.485100) \right)
$$

---


## 📊 Results & Visualizations

| Plot | Preview |
|-------|---------|
| **Observed data vs fitted curve** | <img src="https://github.com/user-attachments/assets/731f7bca-a3d9-4d63-8fbf-3baa2fcdb802" width="400"/> |
| **Pointwise L1 error vs t** | <img src="https://github.com/user-attachments/assets/855248cb-8576-4755-8e90-388f960d41b2" width="400"/> |

---

### ✅ Example Output

#### 🔹 Observed vs Fitted Curve  
<img src="https://github.com/user-attachments/assets/575688a0-949a-453f-a046-0c6421196a93" width="600"/>

#### 🔹 L1 Error vs t  
<img src="https://github.com/user-attachments/assets/8990b075-03ea-4f5b-83a1-0528ec7e5260" width="600"/>


---


## 🛠️ Method / Approach (Summary)

1. Loaded the observed `(x, y)` points from `xy_data.csv`
2. Visualized the dataset to confirm consistency
3. Mapped data row index → parametric variable `t ∈ [6, 60]`
4. Implemented the model functions:

   ```python
   x(t) = t*cos(theta) - exp(M*abs(t))*sin(0.3*t)*sin(theta) + X

   y(t) = 42 + t*sin(theta) + exp(M*abs(t))*sin(0.3*t)*cos(theta)

5. **Defined optimization objective**

The goal is to minimize the total L1 distance between observed data points \((x_i, y_i)\) and model-predicted points \((\hat{x_i}, \hat{y_i})\):

$$
\min \sum_{i=1}^{N} \left( |x_i - \hat{x_i}| + |y_i - \hat{y_i}| \right)
$$

6. **Used `least_squares()` with:**
   - bounded parameters  
   - soft-L1 loss (robust to outliers)  
   - numeric gradients  

7. Computed final true L1 score after fitting  

8. Plotted fitted vs observed curve + L1 error vs t  




How to Run the Code
git clone https://github.com/<your-username>/curve-fitting-assignment
cd curve-fitting-assignment
pip install -r requirements.txt
python fit_curve.py
