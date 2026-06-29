from common.utils import print_header, print_toc_entry, print_sub_section
import numpy as np

def main(): 
    print_header("Day 3: Introduction to Pandas Data Manipulation")
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
    vector = np.array([1, 2, 3])
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
    agg_arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("Original array:", agg_arr)
    print("Sum():", np.sum(agg_arr))
    print("Mean():", np.mean(agg_arr))
    print("Median():", np.median(agg_arr))
    vals, counts = np.unique(agg_arr, return_counts=True)
    print('mode():', vals[np.argmax(counts)])
    print("Min():", np.min(agg_arr))
    print("Max():", np.max(agg_arr))
    print("Standard Deviation():", np.std(agg_arr))
    print("Variance():", np.var(agg_arr))
    print("Sum along rows:", np.sum(agg_arr, axis=1))
    print("Sum along columns:", np.sum(agg_arr, axis=0))

    print_header("Boolean Indexing and Filtering")
    filter_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print("Original array:", filter_arr)

    evens = filter_arr[filter_arr % 2 == 0]
    print('evens:', evens)
    odds = filter_arr[filter_arr % 2 == 1]
    print('odds:', odds)
    print("Modify elements based on conditions:")
    arr[(arr > 3) & (arr < 7)] = 0
    print("Original modified:", arr)

    print_header("Random Number Generation and Setting Seeds")
    print_toc_entry(1, "Random Number Generation using np.random")
    random_arr = np.random.rand(3,3)
    print("Random array:", random_arr)
    random_array = np.random.randint(low=0, high=100, size=10)
    print("random_array:", random_array)
    random_integers = np.random.randint(low=0, high=100, size=(2,3))
    print("random_integers:", random_integers)

    print_toc_entry(2, "Setting Random Seeds")
    np.random.seed(42)
    random_arr = np.random.rand(3, 3)
    print("Random seed: array the same:", random_arr)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

