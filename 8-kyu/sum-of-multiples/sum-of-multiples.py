def sum_mul(n, m):
    total = 0
    if n<=0 or m<=0:
        return "INVALID"
    for i in range(n,m,n):
        total+=i
    return total