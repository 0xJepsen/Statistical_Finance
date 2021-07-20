def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)

    numerator = 0

    for data in dataset:
        numerator += (data - mean) ** 2

    return numerator / len(dataset)
