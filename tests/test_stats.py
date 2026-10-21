from toolkit.stats import calculate_mean, calculate_median, calculate_variance

def test_mean():
    assert calculate_mean([10, 20, 30]) == 20.0

def test_median():
    assert calculate_median([1, 3, 2]) == 2.0
    assert calculate_median([1, 2, 3, 4]) == 2.5

def test_variance():
    assert calculate_variance([2, 4, 4, 4, 5, 5, 7, 9]) == 4.571428571428571

def test_weighted_mean():
    from toolkit.stats import calculate_weighted_mean
    assert calculate_weighted_mean([10, 20], [1, 3]) == 17.5

def test_harmonic_mean():
    from toolkit.stats import calculate_harmonic_mean
    assert round(calculate_harmonic_mean([2, 6]), 2) == 3.0
