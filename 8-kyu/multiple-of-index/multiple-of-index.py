def multiple_of_index(arr):
    result = []
​
    if arr and arr[0] == 0:
        result.append(0)
​
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            result.append(arr[i])
​
    return result