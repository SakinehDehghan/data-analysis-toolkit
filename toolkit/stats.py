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
