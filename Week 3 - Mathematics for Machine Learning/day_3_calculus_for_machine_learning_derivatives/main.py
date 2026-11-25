from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np
import sympy as sp


def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    theta: np.ndarray,
    learning_rate: float,
    iterations: int
) -> np.ndarray:
    m: int = len(y)
    for _ in range(iterations):
        predictions: np.ndarray = np.dot(X, theta)
        errors: np.ndarray = predictions - y
        gradients: np.ndarray = (1 / m) * np.dot(X.T, errors)
        theta = theta - learning_rate * gradients
    return theta


def main():
    print_header("Day 3: Calculus for Machine Learning (Derivatives)")

    # =========================================================================
    # SECTION 1: INTRODUCTION TO DERIVATIVES & OPTIMIZATION
    # =========================================================================
    print_toc_entry(1, "Introduction to Derivatives & Optimization")

    # Sub-section 1: Core Concepts & Common Derivatives
    print_sub_section(1, "Core Concepts & Common Derivatives")
    print("A derivative measures the rate at which a function changes with respect to its input.")
    print("For a function f(x), the first derivative f'(x) indicates the slope of the tangent line at point x.")
    print("Role in Optimization: Derivatives are used to minimize or maximize a function, which is critical in ML for optimizing loss functions (e.g., finding the direction to adjust parameters to minimize error in linear regression).")
    print("Common Derivatives: d/dx (x^2) = 2x | d/dx (sin(x)) = cos(x)")

    # Sub-section 2: Python Implementation with SymPy
    print_sub_section(2, "Python Implementation with SymPy")
    x = sp.Symbol('x')
    f = x ** 2
    derivative_f = sp.diff(f, x)
    print("Function f(x) =", f)
    print("Derivative f'(x) (sp.diff(f, x)) =", derivative_f)

    f_sin = sp.sin(x)
    print("Function g(x) =", f_sin)
    print("Derivative g'(x) =", sp.diff(f_sin, x))


    # =========================================================================
    # SECTION 2: PARTIAL DERIVATIVES & GRADIENTS
    # =========================================================================
    print_toc_entry(2, "Partial Derivatives & Gradients")

    # Sub-section 1: Core Concepts & Gradient Vector
    print_sub_section(1, "Core Concepts & Gradient Vector")
    print("A partial derivative measures how a multivariable function changes with respect to one variable while keeping all other variables constant.")
    print("The gradient (nabla f) is a vector of all partial derivatives indicating the direction of steepest ascent.")
    print("For f(x, y) = x^2 + y^2: df/dx = 2x, df/dy = 2y, and Gradient = [2x, 2y]^T.")

    # Sub-section 2: Python Implementation (Partial Derivatives)
    print_sub_section(2, "Python Implementation (Partial Derivatives)")
    x_sym, y_sym = sp.symbols('x y')
    f_multi = x_sym ** 2 + y_sym ** 2
    grad_x = sp.diff(f_multi, x_sym)
    grad_y = sp.diff(f_multi, y_sym)
    print("Multivariable Function f(x, y) =", f_multi)
    print("Partial Derivative wrt x (grad_x) =", grad_x)
    print("Partial Derivative wrt y (grad_y) =", grad_y)


    # =========================================================================
    # SECTION 3: GRADIENT DESCENT OPTIMIZATION ALGORITHM
    # =========================================================================
    print_toc_entry(3, "Gradient Descent Optimization Algorithm")

    # Sub-section 1: Core Concepts & Update Rule
    print_sub_section(1, "Core Concepts & Update Rule")
    print("Gradient descent is an iterative optimization algorithm used to minimize a function (such as a loss function).")
    print("It updates parameters in the direction of the negative gradient to find the minimum.")
    print("Update Rule: theta = theta - alpha * nabla J(theta)")
    print("Where theta = model parameters, alpha = learning rate (step size), and nabla J(theta) = gradient of the loss function.")


    # =========================================================================
    # SECTION 4: HANDS-ON EXERCISES
    # =========================================================================
    print_toc_entry(4, "Hands-on Exercises")

    # Sub-section 1: Exercise 1 - Compute Derivative of Basic Functions
    print_sub_section(1, "Exercise 1: Compute Derivative of Basic Functions")
    ex1_x = sp.Symbol('x')
    ex1_func = ex1_x ** 3 - 5 * ex1_x + 7
    ex1_deriv = sp.diff(ex1_func, ex1_x)
    print("Function f(x) =", ex1_func)
    print("First Derivative f'(x) =", ex1_deriv)

    # Sub-section 2: Exercise 2 - Compute Gradients of Multivariable Function
    print_sub_section(2, "Exercise 2: Compute Gradients of Multivariable Function")
    ex2_x, ex2_y = sp.symbols('x y')
    ex2_func = ex2_x ** 2 + 3 * (ex2_y ** 2) - 4 * ex2_x * ex2_y
    ex2_grad_x = sp.diff(ex2_func, ex2_x)
    ex2_grad_y = sp.diff(ex2_func, ex2_y)
    print("Function f(x, y) =", ex2_func)
    print("Gradient wrt x (grad_x) =", ex2_grad_x)
    print("Gradient wrt y (grad_y) =", ex2_grad_y)

    # Sub-section 3: Exercise 3 - Implement Gradient Descent for Linear Regression
    print_sub_section(3, "Exercise 3: Gradient Descent for Linear Regression")
    bias: np.ndarray = np.ones(3)
    features: np.ndarray = np.array((1.0, 2.0, 3.0))
    X_data: np.ndarray = np.column_stack((bias, features))

    y_data: np.ndarray = np.array([2.0, 2.5, 3.5])
    initial_theta: np.ndarray = np.array([0.1, 0.1])
    learning_rate: float = 0.1
    iterations: int = 1000

    optimized_theta: np.ndarray = gradient_descent(
        X_data,
        y_data,
        initial_theta,
        learning_rate,
        iterations
    )
    print("Initial Parameters (theta) =", initial_theta)
    print("Optimized Parameters (theta) =", optimized_theta)


    # =========================================================================
    # SECTION 5: ADDITIONAL PRACTICE
    # =========================================================================
    print_toc_entry(5, "Additional Practice")

    # Sub-section 1: Second-Order Derivatives (Hessian Matrix)
    print_sub_section(1, "Second-Order Derivatives (Hessian Matrix)")
    hessian_matrix = sp.hessian(ex2_func, (ex2_x, ex2_y))
    print("Function f(x, y) =", ex2_func)
    print("Hessian Matrix =\n", hessian_matrix)

    # Sub-section 2: Comparing Multiple Learning Rates
    print_sub_section(2, "Comparing Multiple Learning Rates")
    for lr in [0.01, 0.05, 0.1]:
        theta_test: np.ndarray = gradient_descent(
            X_data,
            y_data,
            np.array([0.1, 0.1]),
            lr,
            1000
        )
        print(f"Learning Rate = {lr:<4} -> Optimized Theta = {theta_test}")


if __name__ == '__main__':
    main()
