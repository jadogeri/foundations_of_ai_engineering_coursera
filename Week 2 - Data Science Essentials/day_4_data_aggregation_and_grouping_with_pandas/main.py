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
    print("\n")
    print_sub_section(1, "Drop Missing Values")

    # Remove all rows with missing values
    clean_df = df.dropna()
    print(clean_df)
    print("\n")

    print_sub_section(2, "Fill Missing Values")
    # Fill missing values with a specific number (like 0)
    filled_df = df.fillna(0)
    print(filled_df)
    print("\n")

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
    print("\n")

    print("Original data:\n", data)
    print("\n")

    print("Original DataFrame:\n", df)

    print_sub_section(1, "Renaming Columns")
    renamed_df = df.rename(columns={'item_name': 'Product'})
    print(renamed_df)
    print("\n")

    print_sub_section(2, "Changing Data Types")
    # Change the 'cost' column from text to whole numbers (integers)
    df['cost'] = df['cost'].astype(int)
    print(df.dtypes)
    print("\n")

    print_sub_section(3, "Creating or Modifying Columns")
    #This step adds a brand new column or overwrites an old one. You usually do this by combining or changing columns you already have. [4, 5, 6]

    # Make sure 'cost' is converted to numbers first, then calculate Total Spend
    df['cost'] = df['cost'].astype(int)
    # Create a new column named 'total_spend'
    df['total_spend'] = df['cost'] * df['count']
    print(df)

    # Table of Contents
    print_header("Combining and Merging DataFrames")
    print_toc_entry(1, "Concatenation")
    print_toc_entry(2, "Merging")
    print_toc_entry(3, "Joining")
    print("\n")

    # Our starting DataFrames setup
    # 1. Setup for Concatenation
    store_a = pd.DataFrame({'Product': ['Apple', 'Banana'], 'Sales': [10, 15]})
    store_b = pd.DataFrame({'Product': ['Cherry', 'Dates'], 'Sales': [8, 12]})

    # 2. Setup for Merging (Updated with unmatched rows to show how left/right/inner work)
    prices = pd.DataFrame({'Item': ['Apple', 'Banana', 'Cherry'], 'Price': [1.0, 0.5, 2.0]})
    sales = pd.DataFrame({'Item': ['Banana', 'Apple', 'Elderberry'], 'Quantity': [10, 5, 3]})

    # 3. Setup for Joining (Updated with unmatched indexes to show how left/right/inner work)
    users = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']}, index=[101, 102, 103])
    emails = pd.DataFrame({'Email': ['alice@email.com', 'bob@email.com', 'david@email.com']}, index=[101, 102, 104])

    print("Original Data Setup:")
    print("Store A:\n", store_a)
    print("Store B:\n", store_b)
    print("Prices:\n", prices)
    print("Sales:\n", sales)
    print("Users:\n", users)
    print("Emails:\n", emails)
    print("\n")

    print_sub_section(1, "Concatenation")
    # Stacking DataFrames vertically (Rows)
    print("Combine rows and ignore index:")
    combined_rows_ignored = pd.concat([store_a, store_b], ignore_index=True)
    print(combined_rows_ignored)
    print("\n")

    print("Combine rows using axis=0 (Keeps original indices):")
    combined_rows_axis0 = pd.concat([store_a, store_b], axis=0)
    print(combined_rows_axis0)
    print("\n")

    # Gluing DataFrames horizontally (Columns)
    print("Combine columns using axis=1:")
    combined_cols_axis1 = pd.concat([store_a, store_b], axis=1)
    print(combined_cols_axis1)
    print("\n")

    print_sub_section(2, "Merging")
    # Merging combines data using a shared column name
    print("Merge using how='inner' (Only items in BOTH dataframes):")
    merged_inner = pd.merge(prices, sales, on='Item', how='inner')
    print(merged_inner)
    print("\n")

    print("Merge using how='left' (All items from Prices, matches from Sales):")
    merged_left = pd.merge(prices, sales, on='Item', how='left')
    print(merged_left)
    print("\n")

    print("Merge using how='right' (All items from Sales, matches from Prices):")
    merged_right = pd.merge(prices, sales, on='Item', how='right')
    print(merged_right)
    print("\n")

    print_sub_section(3, "Joining")
    # Joining combines data side-by-side using the row index numbers
    print("Join using how='inner' (Only indexes in BOTH dataframes):")
    joined_inner = users.join(emails, how='inner')
    print(joined_inner)
    print("\n")

    print("Join using how='left' (All indexes from Users, matches from Emails):")
    joined_left = users.join(emails, how='left')
    print(joined_left)
    print("\n")

    print("Join using how='right' (All indexes from Emails, matches from Users):")
    joined_right = users.join(emails, how='right')
    print(joined_right)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

