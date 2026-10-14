import re
​
def is_digit(n):
    return bool(re.fullmatch(r"[0-9]", n))