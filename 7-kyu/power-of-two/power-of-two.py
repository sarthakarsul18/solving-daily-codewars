def power_of_two(n):
    if n == 0:
        return False
    else:
        while n % 2 == 0:
            n = n // 2
​
        if n == 1:
            return True
        else:
            return False