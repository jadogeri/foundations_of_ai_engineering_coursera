from common.utils import print_header, print_toc_entry, print_sub_section
import io
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import ssl
import urllib.request


def load_titanic_data() -> pd.DataFrame:
    if os.path.exists("titanic.csv"):
        return pd.read_csv("titanic.csv")

    url: str = "https://githubusercontent.com"
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as response:
        csv_text: str = response.read().decode("utf-8")

    df: pd.DataFrame = pd.read_csv(io.StringIO(csv_text))
    df.to_csv("titanic.csv", index=False)
    return df


def main():
    print_header("Day 7: Exploratory Data Analysis (EDA) Project - Titanic Dataset")

    # =========================================================================
    # SECTION 1: EDA FUNDAMENTALS & HYPOTHESIS GENERATION
    # =========================================================================
    print_toc_entry(1, "EDA Fundamentals & Hypothesis Generation")

    # Sub-section 1: Core Steps & Hypothesis
    print_sub_section(1, "Core Steps & Hypothesis")
    print("EDA Steps: 1) Data Cleaning (missing values, duplicates) -> 2) Data Transformation -> 3) Aggregation & Filtering -> 4) Visualization & Insights.")
    print("Hypothesis: Passengers in higher Titanic classes (1st Class) had higher survival rates than passengers in lower classes (2nd and 3rd Class).")


    # =========================================================================
    # SECTION 2: TASK 1 - DATA LOADING, CLEANING, AGGREGATION & FILTERING
    # =========================================================================
    print_toc_entry(2, "Task 1: Data Loading, Cleaning, Aggregation & Filtering")

    # Sub-section 1: Load & Inspect Dataset
    print_sub_section(1, "Load & Inspect Dataset")
    df: pd.DataFrame = load_titanic_data()

    print(f"Dataset Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    print("\nSummary Statistics (df.describe()):")
    print(df.describe())

    # Sub-section 2: Handle Missing Values & Remove Duplicates
    print_sub_section(2, "Handle Missing Values & Remove Duplicates")
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df = df.drop_duplicates()

    print("Filled missing 'Age' values with median:", df["Age"].median())
    print("Filled missing 'Embarked' values with mode:", df["Embarked"].mode()[0])
    print("Missing values remaining in Age & Embarked:", df[["Age", "Embarked"]].isnull().sum().to_dict())

    # Sub-section 3: Filtering & Aggregation
    print_sub_section(3, "Filtering & Aggregation")
    first_class: pd.DataFrame = df[df["Pclass"] == 1]
    print("First Class Passengers (Top 5):")
    print(first_class[["PassengerId", "Name", "Sex", "Age", "Fare", "Survived"]].head())

    survival_by_class: pd.Series = df.groupby("Pclass")["Survived"].mean()
    print("\nSurvival Rate by Passenger Class:")
    for pclass, rate in survival_by_class.items():
        print(f"  Class {pclass}: {rate:.2%}")


    # =========================================================================
    # SECTION 3: TASK 2 - GENERATE VISUALIZATIONS
    # =========================================================================
    print_toc_entry(3, "Task 2: Generate Visualizations (Bar, Histogram & Scatter)")

    # Sub-section 1: Survival Rate, Age Distribution & Age vs. Fare Plots
    print_sub_section(1, "Survival Rate, Age Distribution & Age vs. Fare Plots")
    plt.figure(figsize=(15, 4))

    # 1. Bar Chart: Survival Rate by Class
    plt.subplot(1, 3, 1)
    survival_by_class.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Survival Rate by Class")
    plt.xlabel("Passenger Class (Pclass)")
    plt.ylabel("Survival Rate")
    plt.xticks(rotation=0)

    # 2. Histogram: Age Distribution
    plt.subplot(1, 3, 2)
    sns.histplot(df["Age"], kde=True, bins=20, color="purple")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")

    # 3. Scatter Plot: Age vs. Fare
    plt.subplot(1, 3, 3)
    plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="teal")
    plt.title("Age vs. Fare")
    plt.xlabel("Age")
    plt.ylabel("Fare")

    plt.tight_layout()
    plt.show()


    # =========================================================================
    # SECTION 4: TASK 3 & TASK 4 - PATTERNS, ANOMALIES & EDA REPORT
    # =========================================================================
    print_toc_entry(4, "Task 3 & Task 4: Patterns, Anomalies & EDA Summary Report")

    # Sub-section 1: Correlation Matrix & Anomaly Check
    print_sub_section(1, "Correlation Matrix & Anomaly Check")
    numeric_cols: list[str] = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
    corr_matrix: pd.DataFrame = df[numeric_cols].corr()
    print("Correlation Matrix:")
    print(corr_matrix.round(3))

    high_fare_outliers: pd.DataFrame = df[df["Fare"] > 300]
    print(f"\nFare Anomalies (Fare > $300): {len(high_fare_outliers)} passengers found (Max Fare: ${df['Fare'].max():.2f}).")

    # Sub-section 2: Titanic Dataset EDA Summary Report
    print_sub_section(2, "Titanic Dataset EDA Summary Report")
    print("1. OVERVIEW:")
    print(f"   - Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
    print("   - Missing values handled: 'Age' imputed with median; 'Embarked' imputed with mode; duplicates dropped.")
    print("2. KEY INSIGHTS:")
    print(f"   - Survival rates were highest for 1st Class ({survival_by_class[1]:.1%}) and lowest for 3rd Class ({survival_by_class[3]:.1%}), validating the hypothesis.")
    print("   - Majority of passengers were aged between 20 and 40 years (peaking around 25-30 years).")
    print(f"   - Positive correlation exists between Fare and Survival (r = {corr_matrix.loc['Fare', 'Survived']:.2f}), and negative correlation between Pclass and Survival (r = {corr_matrix.loc['Pclass', 'Survived']:.2f}).")


    # =========================================================================
    # SECTION 5: ADDITIONAL PRACTICE (ADVANCED SEABORN VISUALIZATIONS)
    # =========================================================================
    print_toc_entry(5, "Additional Practice: Advanced Seaborn Visualizations")

    # Sub-section 1: Box Plot (Fare by Class) & Correlation Heatmap
    print_sub_section(1, "Box Plot & Correlation Heatmap")
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    sns.boxplot(x="Pclass", y="Fare", hue="Pclass", data=df, palette="Set2", legend=False)
    plt.title("Fare Distribution & Outliers by Class (Box Plot)")
    plt.xlabel("Passenger Class")
    plt.ylabel("Fare")

    plt.subplot(1, 2, 2)
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Heatmap")

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
