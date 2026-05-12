from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np

def main(): 
    print_header("Day 1: Introduction to NumPy")
    print_toc_entry(1, "create numpy arrays using list and built-in functions")
    print_toc_entry(2, "array operations")
    print_toc_entry(3, "array indexing and slicing")

    print_sub_section(1, "create numpy arrays using list and built-in functions")
    # Create a 1D array
    num_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array_1d = np.array(num_list)
    print("numpy array created from list:")
    print(array_1d)
    
    print("\ncreate numpy array using built-in functions:")
    print("\nnumpy array of ones:")
    ones = np.ones(5)  
    print(ones) 
    zeroes = np.zeros(5)
    print("numpy array of zeroes:")
    print(zeroes)
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print("\nnumpy array created from matrix:")
    print(matrix)
    print("\nnumpy array of zeroes using 3 x 3 matrix:")
    zeroes_matrix = np.zeros([3,3])
    print(zeroes_matrix)
    print("\nnumpy array of ones using 3 x 3 matrix:")
    ones_matrix = np.ones([1, 1])
    print(ones_matrix)
    print("\nnumpy array using arange:")
    range_array = np.arange(0, 20, 2)
    print(range_array)
    print("\nnumpy array using linsapce:")
    linspace_array = np.linspace(0, 1, 25)
    print(linspace_array)
    print("\nnumpy array using reshape:")
    reshaped_array1 = np.reshape([0, 1, 2, 3 , 4, 5],(2, 3))
    arr1  = np.array ([0, 1, 2, 3 , 4, 5])
    reshaped_array2 = arr1.reshape(2, 3)
    print(reshaped_array1)
    print(reshaped_array2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

