import statistics

def normalize_and_analyze(data):
    if not all(isinstance(num, (int, float)) for num in data) or not data:
        raise ValueError("Input list must contain only numbers and must not be empty.")
    
    min_val = min(data)
    max_val = max(data)
    
    normalized_data = [(num - min_val) / (max_val - min_val) for num in data]
    
    mean = statistics.mean(normalized_data)
    median = statistics.median(normalized_data)
    variance = statistics.variance(normalized_data)
    
    return normalized_data, mean, median, variance

data = [10, 20, 30, 40, 50]
result = normalize_and_analyze(data)
print(result)  
