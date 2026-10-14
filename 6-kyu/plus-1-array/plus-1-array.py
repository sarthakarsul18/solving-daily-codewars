def up_array(arr):
    if not arr or any(type(x) != int or x < 0 or x > 9 for x in arr):
        return None
    arr = arr.copy()
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0
    return [1] + arr