def merge_arrays(arr1, arr2):
    if arr1 is None and arr2 is None:
        return []
    else:
        arr1.extend(arr2)
        return sorted(set(arr1))