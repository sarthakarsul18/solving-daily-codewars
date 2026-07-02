import math
​
def list_squared(m, n):
    result = []
​
    for num in range(m, n + 1):
        sum_sq = 0
​
        
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum_sq += i * i
​
                other = num // i
                if other != i:  
                    sum_sq += other * other
​
        
        if math.isqrt(sum_sq) ** 2 == sum_sq:
            result.append([num, sum_sq])
​
    return result