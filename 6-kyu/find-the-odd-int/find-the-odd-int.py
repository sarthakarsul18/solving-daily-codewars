def find_it(seq):
    freq = {}
​
    for num in seq:
        freq[num] = freq.get(num, 0) + 1
​
    for num, count in freq.items():
        if count % 2 != 0:
            return num