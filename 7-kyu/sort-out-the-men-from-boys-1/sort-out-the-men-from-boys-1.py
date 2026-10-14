def men_from_boys(arr):
    even = []
    odd = []
    arr = set(arr)
    for i in arr:
        if abs(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    return sorted(even)+ sorted(odd,reverse=True)