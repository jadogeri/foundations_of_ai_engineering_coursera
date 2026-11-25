from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np


# =============================================================================
# TASK 1: MATHEMATICAL FORMULA FOR LINEAR REGRESSION (PREDICTION)
# =============================================================================
def predict(X: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return np.dot(X, theta)


# =============================================================================
# TASK 2: GRADIENT DESCENT FOR PARAMETER OPTIMIZATION
# =============================================================================
def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    theta: np.ndarray,
    learning_rate: float,
    iterations: int
) -> np.ndarray:
    m: int = len(y)
    for _ in range(iterations):
        gradients: np.ndarray = (1 / m) * np.dot(X.T, (np.dot(X, theta) - y))
        theta = theta - learning_rate * gradients
    return theta


# =============================================================================
# TASK 3: EVALUATION METRICS (MSE & R-SQUARED)
# =============================================================================
def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


def r_squared(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    ss_res: float = float(np.sum((y_true - y_pred) ** 2))
    ss_tot: float = float(np.sum((y_true - np.mean(y_true)) ** 2))
    return 1.0 - (ss_res / ss_tot)


def main():
    print_header("Day 7: Math-Driven Mini Project - Linear Regression from Scratch")

    # =========================================================================
    # SECTION 1: MATHEMATICAL FOUNDATIONS
    # =========================================================================
    print_toc_entry(1, "Mathematical Foundations (Linear Algebra, Calculus & Statistics)")

    # Sub-section 1: Linear Algebra, Calculus & Statistics Overview
    print_sub_section(1, "Linear Algebra, Calculus & Statistics Overview")
    print("Linear Algebra Model: y_hat = X * theta (where X includes the bias column and theta holds weights & bias).")
    print("Calculus Loss Function (MSE Cost): J(theta) = (1 / 2m) * sum((y_hat_i - y_i)^2)")
    print("Gradient Vector: nabla J(theta) = (1 / m) * X^T * (X * theta - y)")
    print("Gradient Descent Update Rule: theta = theta - alpha * nabla J(theta)")
    print("Evaluation Metrics: MSE = (1 / m) * sum((y_hat_i - y_i)^2) | R^2 = 1 - (SS_res / SS_tot)")


    # =========================================================================
    # SECTION 2: DATA GENERATION & FEATURE PREPARATION
    # =========================================================================
    print_toc_entry(2, "Synthetic Data Generation & Bias Term Preparation")

    # Sub-section 1: Generate Synthetic Dataset
    print_sub_section(1, "Generate Synthetic Dataset")
    np.random.seed(42)
    X: np.ndarray = 2 * np.random.rand(100, 1)
    y: np.ndarray = 4 + 3 * X + np.random.randn(100, 1)
    X_b: np.ndarray = np.column_stack((np.ones((100, 1)), X))

    print(f"Feature matrix shape with bias (X_b): {X_b.shape}")
    print(f"Target vector shape (y): {y.shape}")
    print("True underlying relationship: y = 4 + 3x + Gaussian noise")


    # =========================================================================
    # SECTION 3: MODEL TRAINING & EVALUATION FROM SCRATCH
    # =========================================================================
    print_toc_entry(3, "Model Training & Evaluation from Scratch")

    # Sub-section 1: Task 1 & Task 2 - Gradient Descent Optimization
    print_sub_section(1, "Task 1 & Task 2: Gradient Descent Optimization")
    theta_init: np.ndarray = np.random.randn(2, 1)
    learning_rate: float = 0.1
    iterations: int = 2000

    theta_optimized: np.ndarray = gradient_descent(
        X_b,
        y,
        theta_init,
        learning_rate,
        iterations
    )
    print(f"Initial Parameters (theta_init): {theta_init.ravel()}")
    print(f"Optimized Parameters (theta_optimized): {theta_optimized.ravel()}")

    # Sub-section 2: Task 3 - Predictions & Evaluation Metrics (MSE & R^2)
    print_sub_section(2, "Task 3: Predictions & Evaluation Metrics (MSE & R^2)")
    y_pred: np.ndarray = predict(X_b, theta_optimized)
    mse_score: float = mean_squared_error(y, y_pred)
    r2_score: float = r_squared(y, y_pred)

    print(f"Mean Squared Error (MSE): {mse_score:.4f}")
    print(f"R-Squared (R^2): {r2_score:.4f}")


if __name__ == '__main__':
    main()
