import random
from scipy.stats import ttest_1samp, binom, norm
from statistics import mean, median, mode

def generate_mean_median_mode_problem():
    data = random.sample(range(1, 100), 10)  # Generate a random dataset of 10 values
    solution = {
        "mean": round(mean(data), 2),
        "median": median(data),
        "mode": mode(data) if len(set(data)) < len(data) else "No mode"
    }
    return {
        "problem": f"Find the mean, median, and mode of the dataset: {data}",
        "solution": solution
    }

def generate_probability_problem():
    outcomes = random.randint(2, 10)
    event = random.randint(1, outcomes)
    solution = event / outcomes
    return {
        "problem": f"What is the probability of an event occurring with {event} favorable outcomes out of {outcomes} total outcomes?",
        "solution": round(solution, 2)
    }

def generate_std_variance_problem():
    data = random.sample(range(1, 100), 10)
    mean_value = mean(data)
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return {
        "problem": f"Find the standard deviation and variance of the dataset: {data}",
        "solution": {"variance": round(variance, 2), "standard_deviation": round(std_dev, 2)}
    }

def generate_hypothesis_testing_problem():
    sample_data = random.sample(range(50, 100), 10)  # Random sample data
    population_mean = random.randint(40, 60)
    t_stat, p_value = ttest_1samp(sample_data, population_mean)
    return {
        "problem": f"Given the sample data {sample_data}, perform a t-test to test the hypothesis that the population mean is {population_mean}.",
        "solution": {"t_stat": round(t_stat, 2), "p_value": round(p_value, 4)}
    }

def generate_binomial_distribution_problem():
    trials = random.randint(5, 10)  # Number of trials
    prob_success = round(random.uniform(0.2, 0.8), 2)  # Probability of success
    successes = random.randint(0, trials)  # Number of successes to calculate probability for
    solution = binom.pmf(successes, trials, prob_success)  # Probability mass function
    return {
        "problem": f"In a binomial distribution with {trials} trials and a probability of success {prob_success}, what is the probability of exactly {successes} successes?",
        "solution": round(solution, 4)
    }

def generate_normal_distribution_problem():
    mean_value = random.randint(50, 100)
    std_dev = random.randint(5, 15)
    z_score = round(random.uniform(-3, 3), 2)
    prob = 1 - norm.cdf(z_score)  # Probability that a value is above the Z-score
    return {
        "problem": f"For a normal distribution with mean {mean_value} and standard deviation {std_dev}, what is the probability that a value is greater than {z_score} standard deviations above the mean?",
        "solution": round(prob, 4)
    }