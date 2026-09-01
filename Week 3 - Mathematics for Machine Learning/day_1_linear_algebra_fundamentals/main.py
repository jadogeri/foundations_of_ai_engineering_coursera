
from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np

def main(): 
    print_header("Day 1: Introduction to Linear Algebra Fundamentals")
    print_toc_entry(1, "examples of vector and matrix")

    print_sub_section(1, "vector")
    vector = np.array([1, 2, 3])
    print("vector =", vector)

    print_sub_section(2, "matrix")
    matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
    matrix_b = np.array([[7, 8, 9], [10, 11, 12]])
    print("matrix =", matrix_a)
    print("matrix b =", matrix_b)

    print_toc_entry(2, "Matrix Operations")
    print_sub_section(1, "Addition")
    print(matrix_a + matrix_b)
    print_sub_section(2, "Subtraction")
    print(matrix_a - matrix_b)
    print_sub_section(2, "Multiplication")
    print(matrix_a * matrix_b)
    print_sub_section(2, "Division")
    print(matrix_a / matrix_b)
    print_sub_section(2, "Modulo")
    print(matrix_a % matrix_b)

    print_toc_entry(1, "Scalar Operations")
    print_sub_section(1, "multiplication")
    matrix_c = 2 * matrix_a
    print("multiplied by 2 =", matrix_c)

    print_sub_section(2, "matrix multiplication")
    matrix_d = np.array([[1, 2], [3 , 4]])
    matrix_e = np.array([[5, 6], [7, 8]])
    print("matrix_e =", matrix_e)
    print("matrix_d =", matrix_d)
    matrix_mul = np.dot(matrix_e, matrix_d)
    print("matrix_mul =", matrix_mul)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

