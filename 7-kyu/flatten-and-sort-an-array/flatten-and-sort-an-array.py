def flatten_and_sort(array):
    result = []
    for i in array:
        result.extend(i)
    return sorted(result)