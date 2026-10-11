from collections import Counter
def highest_rank(arr):
    count = Counter(arr)
    return max(count, key=lambda x: (count[x], x))