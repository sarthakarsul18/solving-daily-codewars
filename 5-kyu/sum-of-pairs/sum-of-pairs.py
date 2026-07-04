def sum_pairs(ints, s):
    seen = set()
​
    for num in ints:
        if s - num in seen:
            return [s - num, num]
        seen.add(num)
​
    return None