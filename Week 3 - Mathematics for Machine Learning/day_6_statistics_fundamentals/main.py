from common.utils import print_header, print_toc_entry, print_sub_section
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind
from statistics import mode


def main():
    print_header("Day 6: Statistics Fundamentals")

    # =========================================================================
    # SECTION 1: MEASURES OF CENTRAL TENDENCY & DISPERSION
    # =========================================================================
    print_toc_entry(1, "Measures of Central Tendency & Dispersion")

    # Sub-section 1: Central Tendency (Mean, Median, Mode)
    print_sub_section(1, "Central Tendency (Mean, Median, Mode)")
    print("Mean: Average value of a dataset (sum / count).")
    print("Median: Middle value when data is sorted.")
    print("Mode: Most frequently occurring value.")

    data: tuple[int, ...] = (10, 20, 30, 40, 50)
    mean_val: float = sum(data) / len(data)

    sorted_data: list[int] = sorted(data)
    n: int = len(data)
    if n % 2 != 0:
        median_val: float = float(sorted_data[n // 2])
    else:
        median_val = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    mode_val: int = mode(data)
    print(f"Dataset: {data}")
    print(f"Mean = {mean_val}")
    print(f"Median = {median_val}")
    print(f"Mode = {mode_val}")

    # Sub-section 2: Dispersion (Variance & Standard Deviation)
    print_sub_section(2, "Dispersion (Variance & Standard Deviation)")
    print("Variance: Average squared deviation from the mean.")
    print("Standard Deviation: Square root of variance, indicating data spread.")

    variance_val: float = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev_val: float = variance_val ** 0.5
    print(f"Variance = {variance_val}")
    print(f"Standard Deviation = {std_dev_val:.4f}")


    # =========================================================================
    # SECTION 2: HYPOTHESIS TESTING & CONFIDENCE INTERVALS
    # =========================================================================
    print_toc_entry(2, "Hypothesis Testing & Confidence Intervals")

    # Sub-section 1: Hypothesis Testing Concepts
    print_sub_section(1, "Hypothesis Testing Concepts")
    print("Null Hypothesis (H0): Assumes no effect or difference exists.")
    print("Alternative Hypothesis (Ha): Assumes a statistically significant effect or difference exists.")
    print("P-Value & Significance Level (alpha): If p-value < alpha (e.g., 0.05), reject H0.")

    # Sub-section 2: Confidence Intervals (95% CI)
    print_sub_section(2, "Confidence Intervals (95% CI)")
    print("Formula: CI = x_bar +/- Z * (s / sqrt(n)) | For 95% confidence, Z = 1.96")

    z_score: float = 1.96
    margin_of_error: float = z_score * (std_dev_val / (len(data) ** 0.5))
    ci_lower: float = mean_val - margin_of_error
    ci_upper: float = mean_val + margin_of_error
    print(f"95% Confidence Interval = ({ci_lower:.2f}, {ci_upper:.2f})")


    # =========================================================================
    # SECTION 3: HANDS-ON EXERCISES
    # =========================================================================
    print_toc_entry(3, "Hands-on Exercises")

    # Sub-section 1: Exercise 1 - Mean, Variance & Std Dev with NumPy
    print_sub_section(1, "Exercise 1: Mean, Variance & Std Dev with NumPy")
    np_data: np.ndarray = np.array((10, 20, 30, 40, 50))
    np_mean: float = float(np.mean(np_data))
    np_var: float = float(np.var(np_data))
    np_std: float = float(np.std(np_data))
    print(f"NumPy Mean = {np_mean}")
    print(f"NumPy Variance = {np_var}")
    print(f"NumPy Standard Deviation = {np_std:.4f}")

    # Sub-section 2: Exercise 2 - Two-Sample T-Test
    print_sub_section(2, "Exercise 2: Two-Sample T-Test")
    group_1: tuple[float, ...] = (2.1, 2.5, 2.8, 3.0, 3.2)
    group_2: tuple[float, ...] = (1.8, 2.0, 2.4, 2.7, 2.9)

    t_stat, p_value = ttest_ind(group_1, group_2)
    alpha: float = 0.05
    print(f"Group 1: {group_1}")
    print(f"Group 2: {group_2}")
    print(f"T-Statistic = {t_stat:.4f}")
    print(f"P-Value = {p_value:.4f}")

    if p_value < alpha:
        print("Result: Reject the null hypothesis (statistically significant difference).")
    else:
        print("Result: Fail to reject the null hypothesis (no significant difference).")


    # =========================================================================
    # SECTION 4: ADDITIONAL PRACTICE
    # =========================================================================
    print_toc_entry(4, "Additional Practice")

    # Sub-section 1: Confidence Interval for Proportions
    print_sub_section(1, "Confidence Interval for Proportions")
    n_trials: int = 200
    successes: int = 120
    p_hat: float = successes / n_trials
    se_prop: float = (p_hat * (1 - p_hat) / n_trials) ** 0.5
    prop_ci_low: float = p_hat - 1.96 * se_prop
    prop_ci_high: float = p_hat + 1.96 * se_prop
    print(f"Sample Proportion (p_hat) = {p_hat:.2f} ({successes}/{n_trials})")
    print(f"95% Confidence Interval for Proportion = ({prop_ci_low:.4f}, {prop_ci_high:.4f})")

    # Sub-section 2: Visualizing Data Distribution with Mean, Median & Mode
    print_sub_section(2, "Visualizing Data Distribution with Mean, Median & Mode")
    exam_scores: np.ndarray = np.array((72, 78, 80, 82, 85, 85, 85, 88, 90, 95))
    score_mean: float = float(np.mean(exam_scores))
    score_median: float = float(np.median(exam_scores))
    score_mode: int = int(mode(exam_scores))

    plt.figure(figsize=(8, 4))
    plt.hist(exam_scores, bins=6, color="skyblue", edgecolor="black", alpha=0.7)
    plt.axvline(score_mean, color="red", linestyle="--", linewidth=2, label=f"Mean ({score_mean:.1f})")
    plt.axvline(score_median, color="green", linestyle="-.", linewidth=2, label=f"Median ({score_median:.1f})")
    plt.axvline(score_mode, color="purple", linestyle=":", linewidth=2, label=f"Mode ({score_mode})")
    plt.title("Exam Scores Distribution: Mean vs. Median vs. Mode")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
