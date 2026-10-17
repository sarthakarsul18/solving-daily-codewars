def sum_triangular_numbers(n):
    total = 0
    triangle = 0
    if n<0:
        return 0
    for i in range(1,n+1):
        triangle = triangle+i
        total = total + triangle
    return total