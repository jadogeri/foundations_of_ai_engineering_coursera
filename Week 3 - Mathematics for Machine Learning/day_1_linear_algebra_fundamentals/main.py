from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np


def main():
    print_header("Day 1: Introduction to Linear Algebra Fundamentals")

    # =========================================================================
    # SECTION 1: EXAMPLES OF VECTOR AND MATRIX
    # =========================================================================
    print_toc_entry(1, "Examples of Vector and Matrix")

    # Sub-section 1: Vector
    print_sub_section(1, "Vector")
    vector = np.array([2, 3, 4])
    print("vector =", vector)

    # Sub-section 2: Matrix
    print_sub_section(2, "Matrix")
    matrix_transcript = np.array([
        [2, -3, 1],
        [2, 0, -1],
        [1, 4, 5]
    ])
    print("3x3 matrix from transcript =\n", matrix_transcript)

    # =========================================================================
    # SECTION 2: ELEMENT-WISE MATRIX OPERATIONS
    # =========================================================================
    print_toc_entry(2, "Element-wise Matrix Operations")

    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    print("matrix A =\n", matrix_a)
    print("matrix B =\n", matrix_b)

    # Sub-section 1: Addition (A + B)
    print_sub_section(1, "Addition (A + B)")
    print("Addition =\n", matrix_a + matrix_b)

    # Sub-section 2: Subtraction (B - A)
    print_sub_section(2, "Subtraction (B - A)")
    print("Subtraction =\n", matrix_b - matrix_a)

    # Sub-section 3: Supplemental Element-wise Operations
    print_sub_section(3, "Element-wise Multiplication & Division")
    print("Element-wise Mul =\n", matrix_a * matrix_b)
    print("Element-wise Div =\n", matrix_a / matrix_b)

    # =========================================================================
    # SECTION 3: SCALAR OPERATIONS & MATRIX MULTIPLICATION
    # =========================================================================
    print_toc_entry(3, "Scalar & Matrix Multiplication")

    # Sub-section 1: Scalar Multiplication (C = 2 * A)
    print_sub_section(1, "Scalar Multiplication")
    matrix_c = 2 * matrix_a
    print("Scalar multiplication (2 * A) =\n", matrix_c)

    # Sub-section 2: Matrix Dot Product
    print_sub_section(2, "Matrix Multiplication (Dot Product)")
    result_dot = np.dot(matrix_a, matrix_b)
    print("Matrix Multiplication (np.dot(A, B)) =\n", result_dot)

    # =========================================================================
    # SECTION 4: SPECIAL MATRICES
    # =========================================================================
    print_toc_entry(4, "Special Matrices")

    # Sub-section 1: Identity Matrix (np.eye)
    print_sub_section(1, "Identity Matrix")
    I = np.eye(3)  # Instructor notes passing one number creates a square matrix
    print("Identity matrix =\n", I)

    # Sub-section 2: Zero Matrix (np.zeros)
    print_sub_section(2, "Zero Matrix")
    Z = np.zeros((2, 3))  # Not strictly square, requires (rows, columns) shape tuple
    print("Zero matrix =\n", Z)

    # Sub-section 3: Diagonal Matrix (np.diag)
    print_sub_section(3, "Diagonal Matrix")
    d = np.diag([1, 2, 3])
    print("Diagonal matrix =\n", d)

    # =========================================================================
    # SECTION 5: HANDS-ON EXERCISES
    # =========================================================================
    print_toc_entry(5, "Hands-on Exercises")

    # Sub-section 1: Exercise 1 - Basic Operations Practice
    print_sub_section(1, "Exercise 1: Matrix Operations")
    ex1_A = np.array([[1, 2], [3, 4]])
    ex1_B = np.array([[9, 8], [7, 6]])

    print("Addition:\n", ex1_A + ex1_B)
    print("Subtraction:\n", ex1_A - ex1_B)
    print("Scalar Multiplication (3 * A):\n", 3 * ex1_A)

    # Sub-section 2: Exercise 2 - Matrix-Vector Multiplication
    print_sub_section(2, "Exercise 2: Matrix Vector Multiplication")
    m = np.array([,
    ,
        [7, 8, 9]
    ])
    v = np.array([1, 0, -1])

    ex2_result = np.dot(m, v)
    print("Matrix-Vector Multiplication (np.dot(m, v)) =\n", ex2_result)


if __name__ == '__main__':
    main()
