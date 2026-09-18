def remainder(n, m):
    larger = max(n, m)
    smaller = min(n, m)
​
    if smaller == 0:
        return None
​
    return larger % smaller