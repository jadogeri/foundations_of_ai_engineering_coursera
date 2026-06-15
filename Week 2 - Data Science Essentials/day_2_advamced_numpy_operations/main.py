from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np

def main(): 
    print_header("Day 2: Advanced NumPy Operations")
    print_toc_entry(1, "Broadcasting")
    print_toc_entry(2, "array operations")
    print_toc_entry(3, "array indexing and slicing")

    print_sub_section(1, "Broadcasting")
    print("Broadcasting is a powerful mechanism in NumPy that allows operations to be performed on arrays of different shapes. It automatically expands the smaller array to match the shape of the larger array, enabling element-wise operations without the need for explicit loops.")
    print("For example, if we have a 2D array and a 1D array, we can add them together, and NumPy will automatically broadcast the 1D array across the 2D array.")
    a = np.array([[1, 2, 3], [4, 5, 6]])


    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Original array:")
    print(arr)
    print_sub_section(1, "Array and scalar broadcasting")
    print_sub_section(2, "Original array")
    print("arr + 10:")
    print(arr + 10)
    print("arr * 2:")
    print(arr * 2)
    print("arr ** 2:")
    print(arr ** 2)
    print("arr / 2:")
    print(arr / 2)
    print("arr - 5:")
    print(arr - 5)
    
    print("vectors and matrices:")
    vector= np.array([1, 2, 3])
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    
    print("Original vector:")
    print(vector)
    print("Original matrix:")
    print(matrix)
    print("vector + matrix:")
    print(vector + matrix)
    print("vector * matrix:")
    print(vector * matrix)  
    print("vector ** 2:")
    print(vector ** 2)
    print("vector / 2:")
    print(vector / 2)
    print("matrix - vector:")
    print(matrix - vector)
    print_header("Aggregation functions")
    print("Aggregation functions are used to compute summary statistics of an array. Some common aggregation functions include:")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

