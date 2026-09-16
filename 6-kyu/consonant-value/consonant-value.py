import re
​
def solve(s):
    groups = re.split("[aeiou]", s)
    max_value = 0
​
    for group in groups:
        total = 0
​
        for char in group:
            total += ord(char) - ord('a') + 1
​
        max_value = max(max_value, total)
​
    return max_value