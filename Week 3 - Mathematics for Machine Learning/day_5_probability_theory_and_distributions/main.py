from common.utils import print_header, print_toc_entry, print_sub_section
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, multinomial, norm, poisson, uniform


def bayes_theorem_basic(prior: float, likelihood: float, evidence: float) -> float:
    return (likelihood * prior) / evidence


def bayes_theorem_medical(prior: float, sensitivity: float, specificity: float) -> float:
    evidence: float = (sensitivity * prior) + ((1 - specificity) * (1 - prior))
    posterior: float = (sensitivity * prior) / evidence
    return posterior


def main():
    print_header("Day 5: Probability Theory and Distributions")

    # =========================================================================
    # SECTION 1: PROBABILITY BASICS & BAYES' THEOREM
    # =========================================================================
    print_toc_entry(1, "Probability Basics & Bayes' Theorem")

    # Sub-section 1: Conditional Probability & Bayes' Theorem Formula
    print_sub_section(1, "Conditional Probability & Bayes' Theorem Formula")
    print("Conditional Probability: P(A | B) = P(A and B) / P(B) (probability of event A given event B has occurred).")
    print("Bayes' Theorem: P(A | B) = [P(B | A) * P(A)] / P(B)")
    print("Where P(A) = Prior probability, P(B | A) = Likelihood, and P(B) = Evidence.")

    # Sub-section 2: Python Implementation (Bayes' Theorem)
    print_sub_section(2, "Python Implementation (Bayes' Theorem)")
    basic_posterior: float = bayes_theorem_basic(prior=0.2, likelihood=0.8, evidence=0.4)
    print(f"Basic Bayes' Theorem Result: {basic_posterior:.4f}")


    # =========================================================================
    # SECTION 2: COMMON PROBABILITY DISTRIBUTIONS & ML APPLICATIONS
    # =========================================================================
    print_toc_entry(2, "Common Probability Distributions & ML Applications")

    # Sub-section 1: Core Distributions & ML Use Cases
    print_sub_section(1, "Core Distributions & ML Use Cases")
    print("1. Gaussian (Normal) Distribution: Continuous bell-shaped curve parameterized by mean (mu) and std dev (sigma). ML Use: Gaussian Naive Bayes, Kernel Density Estimation.")
    print("2. Bernoulli Distribution: Discrete distribution for a single binary trial (1 = success with prob p, 0 = failure with prob 1-p). ML Use: Binary classification (spam vs. not spam).")
    print("3. Binomial Distribution: Models number of successes in n independent Bernoulli trials. ML Use: Logistic regression modeling binary outcomes.")
    print("4. Poisson Distribution: Models count of events occurring in a fixed interval of time or space (rate lambda). ML Use: Count data (e.g., website clicks per hour).")

    # Sub-section 2: Manual Gaussian PDF & Bernoulli Visualization
    print_sub_section(2, "Manual Gaussian PDF & Bernoulli Distribution")
    mu: float = 0.0
    sigma: float = 1.0
    x_gauss: np.ndarray = np.linspace(-4, 4, 100)
    y_gauss: np.ndarray = (1 / np.sqrt(2 * np.pi * (sigma ** 2))) * np.exp(-0.5 * ((x_gauss - mu) / sigma) ** 2)
    print(f"Manual Gaussian PDF peak at x=0: {np.max(y_gauss):.4f}")

    p_bernoulli: float = 0.6
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(x_gauss, y_gauss, color="purple")
    plt.title("Gaussian Distribution (Manual Formula)")
    plt.xlabel("x")
    plt.ylabel("Probability Density")

    plt.subplot(1, 2, 2)
    plt.bar((0, 1), (1 - p_bernoulli, p_bernoulli), color="blue")
    plt.xticks((0, 1), ("0 (Failure)", "1 (Success)"))
    plt.title("Bernoulli Distribution (p = 0.6)")
    plt.ylabel("Probability")

    plt.tight_layout()
    plt.show()


    # =========================================================================
    # SECTION 3: HANDS-ON EXERCISES
    # =========================================================================
    print_toc_entry(3, "Hands-on Exercises")

    # Sub-section 1: Exercise 1 - Medical Diagnosis with Bayes' Theorem
    print_sub_section(1, "Exercise 1: Medical Diagnosis with Bayes' Theorem")
    prior_prevalence: float = 0.01      # 1% disease prevalence
    sensitivity_tpr: float = 0.95       # 95% true positive rate
    specificity_tnr: float = 0.90       # 90% true negative rate

    prob_disease_given_positive: float = bayes_theorem_medical(
        prior_prevalence,
        sensitivity_tpr,
        specificity_tnr
    )
    print(f"Prior Prevalence: {prior_prevalence:.2%} | Sensitivity: {sensitivity_tpr:.2%} | Specificity: {specificity_tnr:.2%}")
    print(f"Probability of having the disease given a positive test: {prob_disease_given_positive:.4f} ({prob_disease_given_positive:.2%})")

    # Sub-section 2: Exercise 2 - Plotting Gaussian, Binomial & Poisson Distributions
    print_sub_section(2, "Exercise 2: Plotting Gaussian, Binomial & Poisson Distributions")
    plt.figure(figsize=(14, 4))

    # 1. Gaussian Distribution (scipy.stats.norm)
    x_norm: np.ndarray = np.linspace(-4, 4, 100)
    y_norm: np.ndarray = norm.pdf(x_norm, loc=0, scale=1)
    plt.subplot(1, 3, 1)
    plt.plot(x_norm, y_norm, label="Gaussian", color="navy")
    plt.title("Gaussian Distribution")
    plt.legend()

    # 2. Binomial Distribution (scipy.stats.binom)
    n_trials: int = 10
    p_success: float = 0.5
    x_binom: np.ndarray = np.arange(0, n_trials + 1)
    y_binom: np.ndarray = binom.pmf(x_binom, n_trials, p_success)
    plt.subplot(1, 3, 2)
    plt.bar(x_binom, y_binom, label="Binomial", color="green")
    plt.title("Binomial Distribution (n=10, p=0.5)")
    plt.legend()

    # 3. Poisson Distribution (scipy.stats.poisson)
    lam: float = 3.0
    x_poisson: np.ndarray = np.arange(0, 10)
    y_poisson: np.ndarray = poisson.pmf(x_poisson, lam)
    plt.subplot(1, 3, 3)
    plt.bar(x_poisson, y_poisson, label="Poisson", color="orange")
    plt.title("Poisson Distribution (lambda=3)")
    plt.legend()

    plt.tight_layout()
    plt.show()


    # =========================================================================
    # SECTION 4: ADDITIONAL PRACTICE
    # =========================================================================
    print_toc_entry(4, "Additional Practice")

    # Sub-section 1: Multinomial Distribution (Multiclass Data)
    print_sub_section(1, "Multinomial Distribution (Multiclass Data)")
    multi_dist = multinomial(n=10, p=(0.2, 0.5, 0.3))
    sample_outcome: tuple[int, int, int] = (2, 5, 3)
    print(f"Multinomial PMF for outcome {sample_outcome} with p=(0.2, 0.5, 0.3): {multi_dist.pmf(sample_outcome):.4f}")

    # Sub-section 2: Comparing Gaussian vs. Uniform Distribution
    print_sub_section(2, "Comparing Gaussian vs. Uniform Distribution")
    x_comp: np.ndarray = np.linspace(-3, 3, 200)
    y_norm_comp: np.ndarray = norm.pdf(x_comp, loc=0, scale=1)
    y_unif_comp: np.ndarray = uniform.pdf(x_comp, loc=-2, scale=4)  # Uniform on [-2, 2]

    plt.figure(figsize=(7, 4))
    plt.plot(x_comp, y_norm_comp, label="Gaussian (mu=0, sigma=1)", color="blue")
    plt.plot(x_comp, y_unif_comp, label="Uniform [-2, 2]", color="red", linestyle="--")
    plt.title("Gaussian vs. Uniform Distribution")
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
