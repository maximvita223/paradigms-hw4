def max_reducer(acc, value):
    return acc * value

numbers = [1, 2, 3, 4]
result = reduce(max_reducer, numbers)
print(result)