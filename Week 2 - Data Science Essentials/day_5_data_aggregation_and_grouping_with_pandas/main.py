from common.utils import print_header, print_toc_entry, print_sub_section
import pandas as pd
import numpy as np

def main():
    # Table of Contents
    print_header("Data Aggregation and Grouping")
    print_toc_entry(1, "Iterating Over Groups")
    print_toc_entry(2, "Combining Grouping with Aggregation Methods")
    print_toc_entry(3, "Reshaping Data with Pivot Tables")
    print_toc_entry(4, "Custom Aggregation Using .agg()")
    print_toc_entry(5, "Calculating Summary Statistics")
    print_toc_entry(6, "Multi-Aggregation")
    print("\n")

    # Our starting DataFrame setup
    # Hands-on setup: loading a dataset with categorical and numeric columns
    data = {
        'category_column': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics'],
        'numeric_column': [100, 50, 300, 150, 200]
    }
    df = pd.DataFrame(data)

    print("Original Data Setup:")
    print(df)
    print("\n")

    # Grouping the dataframe by a categorical column to create the group object
    group = df.groupby('category_column')

    print("group by category_column:")
    print(group)

    print_sub_section(1, "Iterating Over Groups")
    # Loop through the group object by name and its subset group data
    for name, group_df in group:
        print(f"Group Name: {name}")
        print(group_df)
        print("---")
    print("\n")

    print_sub_section(2, "Combining Grouping with Aggregation Methods")
    # Directly apply built-in operations like mean() and sum() to columns
    print("Calculate Mean for each group directly:")
    mean_result = df.groupby('category_column')['numeric_column'].mean()
    print(mean_result)
    print("\n")

    print("Calculate Sum for each group directly:")
    sum_result = df.groupby('category_column')['numeric_column'].sum()
    print(sum_result)
    print("\n")

    print_sub_section(3, "Reshaping Data with Pivot Tables")
    # Reshape the table using pivot_table() with values, index, and an aggfunc
    pivot = df.pivot_table(values='numeric_column', index='category_column', aggfunc='mean')
    print(pivot)
    print("\n")

    print_sub_section(4, "Custom Aggregation Using .agg()")

    # Define custom logic to calculate the range (Max - Min)
    def range_function(x):
        return x.max() - x.min()

    print("Apply custom range function (.agg):")
    custom_agg = df.groupby('category_column')['numeric_column'].agg(range_function)
    print(custom_agg)
    print("\n")

    print_sub_section(5, "Calculating Summary Statistics")
    # Pull standard descriptive statistics cleanly from the grouped dataset
    print("Grouped Max values:")
    print(df.groupby('category_column')['numeric_column'].max())
    print("\n")

    print("Grouped Min values:")
    print(df.groupby('category_column')['numeric_column'].min())
    print("\n")

    print_sub_section(6, "Multi-Aggregation")
    # Pass a structured list to compute multiple metrics simultaneously
    print("Group by category and compute mean, max, and min at once:")
    multi_agg = df.groupby('category_column')['numeric_column'].agg(['mean', 'max', 'min'])
    print(multi_agg)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

