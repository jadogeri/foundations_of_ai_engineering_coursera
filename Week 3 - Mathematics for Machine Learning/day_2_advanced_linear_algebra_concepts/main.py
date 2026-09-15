from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np


def main():
    print_header("Day 2: Advanced Linear Algebra Concepts")

    # =========================================================================
    # SECTION 1: DETERMINANTS & INVERSE OF A MATRIX
    # =========================================================================
    print_toc_entry(1, "Determinants & Inverse of a Matrix")

    # Sub-section 1: Determinants
    print_sub_section(1, "Determinants")
    print("A determinant is a scalar value that provides information about a matrix's properties such as invertibility. It is calculated only for square matrices.")
    print("If a determinant of a matrix A equal to 0, the matrix A is singular, which means it is not invertible. Whereas if determinant of A is not equal to 0, then A is invertible.")
    print("For a 2 by 2 matrix, the determinant represents the scaling factor of the area formed by its column vectors. Formula: det(A) = A*D - B*C")

    # Sub-section 2: Python Implementation (Determinants)
    print_sub_section(2, "Python Implementation (Determinants)")
    matrix_a = np.array([,
        [1, 4]
    ])
    print("Matrix A =\n", matrix_a)
    det_a = np.linalg.det(matrix_a)
    print("Determinant of A (np.linalg.det(A)) =", det_a)

    # Sub-section 3: Inverse of a Matrix
    print_sub_section(3, "Inverse of a Matrix")
    print("The inverse of a matrix A is denoted as A raised to minus 1. The product of a matrix and its inverse is the identity matrix. A matrix is invertible only if the determinant of A is not equal to 0.")
    print("Formula for a 2 by 2 matrix: A^-1 = 1 / det(A) * [[D, -B], [-C, A]]")

    # Sub-section 4: Python Implementation (Inverse)
    print_sub_section(4, "Python Implementation (Inverse)")
    inverse_a = np.linalg.inv(matrix_a)
    print("Inverse of A (np.linalg.inv(A)) =\n", inverse_a)


    # =========================================================================
    # SECTION 2: EIGENVALUES AND EIGENVECTORS
    # =========================================================================
    print_toc_entry(2, "Eigenvalues and Eigenvectors")

    # Sub-section 1: Core Concepts & Equations
    print_sub_section(1, "Core Concepts & Mathematical Equation")
    print("Eigenvalues and eigenvectors are properties of square matrices that describe transformations.")
    print("Equation: A * V = lambda * V (where V is the eigenvector and lambda is the eigenvalue).")
    print("Eigenvectors point in the direction where the matrix transformation stretches or compresses vectors. Eigenvalues indicate the factor of stretching or compression.")
    print("An n by n matrix has n eigenvalues and eigenvectors. Eigenvalues can be real or complex. For a symmetric matrix, eigenvalues are always real.")

    # Sub-section 2: Python Implementation (Matrix A & Matrix B)
    print_sub_section(2, "Python Implementation (Matrix A & B)")
    eigenvalues_a, eigenvectors_a = np.linalg.eig(matrix_a)
    print("Eigenvalues (A) =\n", eigenvalues_a)
    print("Eigenvectors (A) =\n", eigenvectors_a)

    matrix_b = np.array([,
        [1, 1]
    ])
    print("Matrix B =\n", matrix_b)
    eigenvalues_b, eigenvectors_b = np.linalg.eig(matrix_b)
    print("Eigenvalues (B) =", eigenvalues_b)
    print("Eigenvectors (B) =\n", eigenvectors_b)


    # =========================================================================
    # SECTION 3: INTRODUCTION TO MATRIX DECOMPOSITION
    # =========================================================================
    print_toc_entry(3, "Introduction to Matrix Decomposition")

    # Sub-section 1: Singular Value Decomposition (SVD)
    print_sub_section(1, "Singular Value Decomposition (SVD)")
    print("Matrix decomposition is a process of breaking a matrix into smaller components to analyze or solve problems.")
    print("SVD decomposes a matrix A into three matrices: A = U * Sigma * V^T")
    print("U: Left singular vectors (orthogonal matrix).")
    print("Sigma: Diagonal matrix of singular values (non-negative).")
    print("V^T: Right singular vectors / V transpose (orthogonal matrix).")
    print("Applications include dimensionality reduction (PCA), noise reduction, and image compression.")

    # Sub-section 2: Python Implementation (SVD)
    print_sub_section(2, "Python Implementation (SVD)")
    U, S, VT = np.linalg.svd(matrix_a)
    print("U (Left Singular Vectors) =\n", U)
    print("S (Singular Values) =", S)
    print("VT (V Transpose) =\n", VT)


    # =========================================================================
    # SECTION 4: HANDS-ON EXERCISES
    # =========================================================================
    print_toc_entry(4, "Hands-on Exercises")

    # Sub-section 1: Exercise 1 - 3x3 Determinant and Inverse
    print_sub_section(1, "Exercise 1: 3x3 Determinant and Inverse")
    ex1_matrix = np.array([,
 ,
        [7, 8, 9]
    ])
    print("3x3 Matrix =\n", ex1_matrix)
    print("Determinant =", np.linalg.det(ex1_matrix))
    print("Inverse =\n", np.linalg.inv(ex1_matrix))

    # Sub-section 2: Exercise 2 - 2x2 Eigenvalues and Eigenvectors
    print_sub_section(2, "Exercise 2: 2x2 Eigenvalues & Eigenvectors")
    ex2_matrix = np.array([
        [4, -2],
        [1, 1]
    ])
    ex2_vals, ex2_vecs = np.linalg.eig(ex2_matrix)
    print("Eigenvalues =", ex2_vals)
    print("Eigenvectors =\n", ex2_vecs)

    # Sub-section 3: Exercise 3 - SVD Matrix Reconstruction
    print_sub_section(3, "Exercise 3: SVD Reconstruction Matrix")
    ex3_matrix = np.array([,
        [-1, 3, 1],
        [1, 1, 3]
    ])
    ex3_U, ex3_S, ex3_VT = np.linalg.svd(ex3_matrix)
    print("U Matrix =\n", ex3_U)
    print("Singular Values (S) =", ex3_S)
    print("V Transpose (VT) =\n", ex3_VT)

    # Reconstruct Matrix
    sigma = np.zeros((3, 3))
    np.fill_diagonal(sigma, ex3_S)
    reconstructed = np.dot(ex3_U, np.dot(sigma, ex3_VT))
    print("Reconstructed Matrix =\n", reconstructed)


if __name__ == '__main__':
    main()
