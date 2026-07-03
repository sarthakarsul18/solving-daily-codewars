def race(v1, v2, g):
    if v1 >= v2:
        return None
​
    total_seconds = (g * 3600) // (v2 - v1)
​
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
​
    return [hours, minutes, seconds]