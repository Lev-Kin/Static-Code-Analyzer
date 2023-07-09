def average_mark(*scores):
    if len(scores) == 0:
        return 0.0
    total = sum(scores)
    average = total / len(scores)
    return round(average, 1)