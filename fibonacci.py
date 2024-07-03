def fibonacci(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series
n = 15
print(fibonacci(n))
