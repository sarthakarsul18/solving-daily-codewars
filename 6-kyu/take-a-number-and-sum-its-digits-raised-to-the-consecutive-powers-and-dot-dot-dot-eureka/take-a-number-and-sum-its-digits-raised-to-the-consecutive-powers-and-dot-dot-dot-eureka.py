def sum_dig_pow(a, b):
    result = []
​
    for num in range(a, b + 1):
        total = 0
        digits = str(num)
​
        for i in range(len(digits)):
            total += int(digits[i]) ** (i + 1)
​
        if total == num:
            result.append(num)
​
    return result