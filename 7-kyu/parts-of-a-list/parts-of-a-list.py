def partlist(a):
    out = []
​
    for i in range(1, len(a)):
        left = " ".join(a[:i])
        right = " ".join(a[i:])
​
        out.append((left, right))
​
    return out