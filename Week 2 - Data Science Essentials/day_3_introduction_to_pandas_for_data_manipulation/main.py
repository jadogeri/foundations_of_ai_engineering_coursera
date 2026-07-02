from common.utils import print_header, print_toc_entry, print_sub_section
import pandas as pd

def main():
    print_header("Day 3: Introduction to Pandas Data Manipulation")
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

    print_sub_section(1, "CSV")
    print("loading animals data from csv.............")
    df = pd.read_csv("./animals.csv")
    print("animals dataframe")
    print(df)
    print("Saving animals data to a new csv file.............")
    df.to_csv("./saved_animals.csv", index=False)
    print("Saving animals data to a new excel file.............")
    df.to_csv("./saved_animals.xlsx", index=False)

    print_header("Basic DataFrame Operations")
    print_toc_entry(1, "Viewing Data")
    print("df.head() the first 5 rows:\n", df.head())
    print("df.tail() the last 5 rows:\n", df.tail())

    print("df.info() information summary of dataframe:\n", df.info())
    print("df.describe() detail statistics :\n", df.describe())

    print_toc_entry(2, "Selecting and Indexing")
    print("printing single column example 'species' column")
    print(df["species"])
    print("printing multiple columns example 'species' and 'animal_id' column")
    print(df[["species","animal_id"]])

    print_toc_entry(3, "Filtering Rows")
    print(df[df["animal_id"] <= 3])

    print_toc_entry(4, "Selection by Position")
    print_sub_section(1, "First row by position")
    print(df.iloc[0])
    print_sub_section(2, "First column by position")
    print(df.iloc[:,0])

    print_toc_entry(4, "Selection by Label")
    print_sub_section(1, "First row by index label")
    print(df.loc[0])
    print_sub_section(2, "First Name column by Label")
    print(df.loc[:,"diet"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

