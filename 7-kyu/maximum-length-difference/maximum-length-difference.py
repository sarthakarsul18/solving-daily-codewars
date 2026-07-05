def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
​
    min_a1 = min(len(s) for s in a1)
    max_a1 = max(len(s) for s in a1)
​
    min_a2 = min(len(s) for s in a2)
    max_a2 = max(len(s) for s in a2)
​
    return max(abs(max_a1 - min_a2), abs(min_a1 - max_a2))