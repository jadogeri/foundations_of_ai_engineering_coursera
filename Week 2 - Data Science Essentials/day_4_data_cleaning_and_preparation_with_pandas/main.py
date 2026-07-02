from common.utils import print_header, print_toc_entry, print_sub_section
import pandas as pd
import numpy as np

def main():
    print_header("Day 4: Data cleaning and preparation with Pandas")
    print_header("Methods to Handling Missing Values")
    print_toc_entry(1, "Drop Missing Values")
    print_toc_entry(2, "Fill Missing Values")
    print_toc_entry(3, "Interpolate Missing Values")

    # Our starting DataFrame
    data = {'Sales': [10, np.nan, 30, np.nan, 50]}
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)
    print("\n\n")
    print_sub_section(1, "Drop Missing Values")

    # Remove all rows with missing values
    clean_df = df.dropna()
    print(clean_df)
    print("\n\n")

    print_sub_section(2, "Fill Missing Values")
    # Fill missing values with a specific number (like 0)
    filled_df = df.fillna(0)
    print(filled_df)
    print("\n\n")

    print_sub_section(2, "Interpolate Missing Values")

    # Guess the missing values based on surrounding numbers
    interpolated_df = df.interpolate()
    print(interpolated_df)

    print_header("Data Transformation")
    print_toc_entry(1, "Renaming Columns")
    print_toc_entry(2, "Changing Data Types")
    print_toc_entry(3, "Creating or Modifying Columns")
    # Our starting DataFrame
    data = {
        'item_name': ['Shoes', 'Shirt', 'Hat'],
        'cost': ['50', '25', '15'],
        'count': [2, 5, 3]
    }
    df = pd.DataFrame(data)
    print("\n\n")

    print("Original data:\n", data)
    print("\n\n")

    print("Original DataFrame:\n", df)

    print_sub_section(1, "Renaming Columns")
    renamed_df = df.rename(columns={'item_name': 'Product'})
    print(renamed_df)
    print("\n\n")

    print_sub_section(2, "Changing Data Types")
    # Change the 'cost' column from text to whole numbers (integers)
    df['cost'] = df['cost'].astype(int)
    print(df.dtypes)
    print("\n\n")

    print_sub_section(3, "Creating or Modifying Columns")
    #This step adds a brand new column or overwrites an old one. You usually do this by combining or changing columns you already have. [4, 5, 6]

    # Make sure 'cost' is converted to numbers first, then calculate Total Spend
    df['cost'] = df['cost'].astype(int)
    # Create a new column named 'total_spend'
    df['total_spend'] = df['cost'] * df['count']
    print(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

