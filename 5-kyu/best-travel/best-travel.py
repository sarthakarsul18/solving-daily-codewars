from itertools import combinations
​
def choose_best_sum(t, k, ls):
    sums = []
​
    for combination in combinations(ls, k):
        total = sum(combination)
​
        if total <= t:
            sums.append(total)
​
    if sums:
        return max(sums)
​
    return None