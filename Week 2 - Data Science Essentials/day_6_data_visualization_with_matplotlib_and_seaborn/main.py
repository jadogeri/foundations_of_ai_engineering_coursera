from common.utils import print_header, print_toc_entry, print_sub_section
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def main():
    # Table of Contents
    print_header("Data Visualization with Matplotlib and Seaborn")
    print_toc_entry(1, "Basic Plot & Line Plot")
    print_toc_entry(2, "Bar Chart for Categorical Data")
    print_toc_entry(3, "Histogram for Distributions")
    print_toc_entry(4, "Scatterplot for Relationships")
    print_toc_entry(5, "Advanced Plot Customization")
    print_toc_entry(6, "Advanced Visualization with Seaborn (Heatmap)")
    print("\n")

    # Our starting Data Setup
    # Static mockup arrays to simulate our visualization data inputs
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [10, 12, 25, 30, 45]
    categories = ['A', 'B', 'C']
    bar_values = [10, 15, 7]
    dist_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    matrix_data = np.array([[1, 2], [3, 4]])

    print("Original Data Setup:")
    print("X Values:", x_vals)
    print("Y Values:", y_vals)
    print("Categories:", categories, "with Values:", bar_values)
    print("Distribution Data Sample:", dist_data)
    print("Matrix Grid Data:\n", matrix_data)
    print("\n")

    print_sub_section(1, "Basic Plot & Line Plot")
    # Visualizes simple coordinate mappings or sequential trends over time
    print("Displaying Line Plot...")
    plt.plot(x_vals[:4], [10, 20, 25, 30], label='trend')
    plt.title("Line Plot")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.legend()
    plt.show()  # Pauses execution until you close the pop-up window
    print("\n")

    print_sub_section(2, "Bar Chart for Categorical Data")
    # Displays vertical rectangular columns to visually contrast independent labels
    print("Displaying Bar Chart...")
    plt.bar(categories, bar_values, color='blue')
    plt.title("Bar Chart Original")
    plt.show()
    print("\n")

    print_sub_section(3, "Histogram for Distributions")
    # Groups individual numerical data values into distinct spans or 'bins'
    print("Displaying Histogram...")
    plt.hist(dist_data, bins=4, color='green', edgecolor='black')
    plt.title("Histogram")
    plt.show()
    print("\n")

    print_sub_section(4, "Scatterplot for Relationships")
    # Isolates independent coordinate points onto a clean visual layout matrix
    print("Displaying Scatterplot...")
    plt.scatter(x_vals, y_vals, color='red')
    plt.title("Scatterplot")
    plt.show()
    print("\n")

    print_sub_section(5, "Advanced Plot Customization")
    # Alters default straight lines into custom dashes and markers for presentation
    print("Displaying Customized Line Plot...")
    plt.plot([1, 2, 3], [10, 20, 30], label='trend', color='orange', linestyle='--', marker='x')
    plt.title("Line Plot Custom")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.legend()
    plt.show()
    print("\n")

    print_sub_section(6, "Advanced Visualization with Seaborn (Heatmap)")
    # Transforms multi-dimensional matrices into a progressive color-shaded grid layout
    print("Displaying Seaborn Heatmap...")
    sns.heatmap(matrix_data, annot=True, cmap='coolwarm')
    plt.title("Seaborn Heatmap")
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

