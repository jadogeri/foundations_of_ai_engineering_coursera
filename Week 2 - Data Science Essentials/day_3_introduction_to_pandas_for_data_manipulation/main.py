from common.utils import print_header, print_toc_entry, print_sub_section
import pandas as pd

def main():
    print_header("Day 1: Introduction to Pandas Data Manipulation")
    print_toc_entry(1, "Series")
    print_toc_entry(1, "DataFrame")

    print_sub_section(1, "Series")

    series = pd.Series([1,2,3,4,5,6], index=['A','B','C','D','E','F'])
    print("original: \n","pd.Series([1,2,3,4,5,6], index=['A','B','C','D','E','F'])")
    print(series)

    print_sub_section(2, "DataFrame")
    data = {"Name": ["John", "Joe", "Jack"], "Age":[30, 49, 48]}
    print("original: \n","pd.Series([1,2,3,4,5,6], index=['A','B','C','D','E','F'])")

    df = pd.DataFrame(data)
    print(df)

    print_header("Loading Data from CSV, Excel, and Other Sources")
    print_toc_entry(1, "CSV")
    print_toc_entry(2, "Excel")
    print_toc_entry(3, "Dictionary")

    print_toc_entry(1, "CSV")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

