\"\"\"Statistical analysis functions.\"\"\"
import math

def calculate_mean(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    if not numbers:
        return 0.0
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return float(s[mid])
    return (s[mid - 1] + s[mid]) / 2.0

def calculate_variance(numbers):
    if len(numbers) < 2:
        return 0.0
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)

def calculate_std(numbers):
    return math.sqrt(calculate_variance(numbers))

def calculate_pearson_correlation(x, y):
    if len(x) != len(y) or len(x) < 2:
        return 0.0
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denom = math.sqrt(sum((xi - mean_x)**2 for xi in x) * sum((yi - mean_y)**2 for yi in y))
    if denom == 0:
        return 0.0
    return numerator / denom

def calculate_summary(numbers):
    if not numbers:
        return {}
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": round(calculate_mean(numbers), 3),
        "median": round(calculate_median(numbers), 3),
        "std": round(calculate_std(numbers), 3),
    }

def calculate_weighted_mean(numbers, weights):
    if len(numbers) != len(weights) or not numbers:
        return 0.0
    total_w = sum(weights)
    if total_w == 0:
        return 0.0
    return sum(n * w for n, w in zip(numbers, weights)) / total_w

def calculate_harmonic_mean(numbers):
    valid = [n for n in numbers if n > 0]
    if not valid:
        return 0.0
    return len(valid) / sum(1.0 / n for n in valid)

def calculate_geometric_mean(numbers):
    valid = [n for n in numbers if n > 0]
    if not valid:
        return 0.0
    log_sum = sum(math.log(n) for n in valid)
    return math.exp(log_sum / len(valid))

def calculate_moving_average(numbers, window_size=3):
    if len(numbers) < window_size or window_size <= 0:
        return []
    return [sum(numbers[i:i+window_size]) / window_size for i in range(len(numbers) - window_size + 1)]
