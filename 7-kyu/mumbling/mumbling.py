def accum(s):
    result = []
​
    for i, ch in enumerate(s):
        result.append(ch.upper() + ch.lower() * i)
​
    return "-".join(result)