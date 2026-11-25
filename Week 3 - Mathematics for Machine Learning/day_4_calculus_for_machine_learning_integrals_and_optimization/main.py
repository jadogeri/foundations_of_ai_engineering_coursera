from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np
import sympy as sp


def stochastic_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    theta: np.ndarray,
    learning_rate: float,
    n_epochs: int
) -> np.ndarray:
    m: int = len(y)
    for _ in range(n_epochs):
        for _ in range(m):
            random_index: int = np.random.randint(m)
            xi: np.ndarray = X[random_index:random_index + 1]
            yi: np.ndarray = y[random_index:random_index + 1]
            gradients: np.ndarray = 2 * xi.T @ (xi @ theta - yi)
            theta = theta - learning_rate * gradients
    return theta


def mini_batch_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    theta: np.ndarray,
    learning_rate: float,
    n_epochs: int,
    batch_size: int = 20
) -> np.ndarray:
    m: int = len(y)
    for _ in range(n_epochs):
        shuffled_indices: np.ndarray = np.random.permutation(m)
        X_shuffled: np.ndarray = X[shuffled_indices]
        y_shuffled: np.ndarray = y[shuffled_indices]
        for i in range(0, m, batch_size):
            xi: np.ndarray = X_shuffled[i:i + batch_size]
            yi: np.ndarray = y_shuffled[i:i + batch_size]
            gradients: np.ndarray = (2 / len(xi)) * (xi.T @ (xi @ theta - yi))
            theta = theta - learning_rate * gradients
    return theta


def main():
    print_header("Day 4: Calculus for Machine Learning (Integrals and Optimization)")

    # =========================================================================
    # SECTION 1: UNDERSTANDING INTEGRALS & ML APPLICATIONS
    # =========================================================================
    print_toc_entry(1, "Understanding Integrals & ML Applications")

    # Sub-section 1: Core Concepts & ML Applications
    print_sub_section(1, "Core Concepts & ML Applications")
    print("Integrals compute the area under a curve, representing the total accumulation across an interval.")
    print("Definite Integral: int_a^b f(x) dx computes the exact area between limits a and b.")
    print("ML Applications: Computing probabilities under Probability Density Functions (PDFs) and regularization/Bayesian weight integration in cost functions.")

    # Sub-section 2: Python Implementation with SymPy
    print_sub_section(2, "Python Implementation with SymPy")
    x = sp.Symbol('x')
    f = x ** 2
    definite_integral = sp.integrate(f, (x, 0, 2))
    indefinite_integral = sp.integrate(f, x)
    print("Function f(x) =", f)
    print("Definite Integral from 0 to 2 (sp.integrate(f, (x, 0, 2))) =", definite_integral)
    print("Indefinite Integral (sp.integrate(f, x)) =", indefinite_integral)

    # =========================================================================
    # SECTION 2: OPTIMIZATION CONCEPTS (MINIMA & CONVEXITY)
    # =========================================================================
    print_toc_entry(2, "Optimization Concepts (Minima & Convexity)")

    # Sub-section 1: Local vs. Global Minima & Convex Functions
    print_sub_section(1, "Local vs. Global Minima & Convex Functions")
    print("Local Minimum: A point where the function has a lower value than neighboring points.")
    print("Global Minimum: The absolute lowest point of the function across its entire domain.")
    print("Convex Function: f(lambda*x1 + (1 - lambda)*x2) <= lambda*f(x1) + (1 - lambda)*f(x2) for lambda in. Any local minimum is guaranteed to be the global minimum.")
    print("Non-Convex Function: Most neural network loss functions are non-convex, containing multiple local minima and saddle points.")

    # =========================================================================
    # SECTION 3: STOCHASTIC GRADIENT DESCENT (SGD) & VARIANTS
    # =========================================================================
    print_toc_entry(3, "Stochastic Gradient Descent (SGD) & Variants")

    # Sub-section 1: SGD & Modern Optimizers
    print_sub_section(1, "SGD & Modern Optimizers")
    print("Stochastic Gradient Descent (SGD): Updates parameters using random single samples or subsets instead of the entire dataset for faster convergence on large data.")
    print("Mini-Batch SGD: Updates parameters using small batches (e.g., 32 or 64 samples) to balance speed and stability.")
    print("Momentum: Adds a fraction of the previous parameter update to the current update to accelerate convergence.")
    print("Adam Optimizer: Combines Momentum with adaptive per-parameter learning rates for fast, reliable training.")

    # =========================================================================
    # SECTION 4: HANDS-ON EXERCISES
    # =========================================================================
    print_toc_entry(4, "Hands-on Exercises")

    # Sub-section 1: Exercise 1 - Calculating Integrals of Simple Functions
    print_sub_section(1, "Exercise 1: Calculating Integrals of Simple Functions")
    ex1_x = sp.Symbol('x')
    ex1_func = sp.exp(-ex1_x)
    ex1_indefinite = sp.integrate(ex1_func, ex1_x)
    ex1_definite = sp.integrate(ex1_func, (ex1_x, 0, sp.oo))
    print("Function f(x) =", ex1_func)
    print("Indefinite Integral =", ex1_indefinite)
    print("Definite Integral from 0 to infinity =", ex1_definite)

    # Sub-section 2: Exercise 2 - Implement Stochastic Gradient Descent (SGD)
    print_sub_section(2, "Exercise 2: Stochastic Gradient Descent for Linear Model")
    np.random.seed(42)
    X: np.ndarray = 2 * np.random.rand(100, 1)
    y: np.ndarray = 4 + 3 * X + np.random.randn(100, 1)
    X_b: np.ndarray = np.column_stack((np.ones((100, 1)), X))

    initial_theta: np.ndarray = np.random.randn(2, 1)
    learning_rate: float = 0.01
    n_epochs: int = 50

    theta_optimized: np.ndarray = stochastic_gradient_descent(
        X_b,
        y,
        initial_theta.copy(),
        learning_rate,
        n_epochs
    )
    print("True Parameters: Intercept = 4.0, Slope = 3.0")
    print("SGD Optimized Parameters (theta) =\n", theta_optimized.ravel())

    # =========================================================================
    # SECTION 5: ADDITIONAL PRACTICE
    # =========================================================================
    print_toc_entry(5, "Additional Practice")

    # Sub-section 1: Mini-Batch Gradient Descent Comparison
    print_sub_section(1, "Mini-Batch Gradient Descent Comparison")
    theta_mini_batch: np.ndarray = mini_batch_gradient_descent(
        X_b,
        y,
        initial_theta.copy(),
        learning_rate=0.05,
        n_epochs=50,
        batch_size=20
    )
    print("Mini-Batch GD Optimized Parameters (theta) =\n", theta_mini_batch.ravel())


if __name__ == '__main__':
    main()
