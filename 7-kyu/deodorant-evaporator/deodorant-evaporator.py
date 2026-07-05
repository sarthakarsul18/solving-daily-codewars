def evaporator(content, evap_per_day, threshold):
    day = 0
    limit = content * threshold / 100
​
    while content > limit:
        content *= (1 - evap_per_day / 100)
        day += 1
​
    return day