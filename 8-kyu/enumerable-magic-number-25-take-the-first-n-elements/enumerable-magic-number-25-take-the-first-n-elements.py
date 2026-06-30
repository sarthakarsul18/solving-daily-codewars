def take(arr,n):
    l = []
    if n<=0 or len(arr)==0:
        return l
    else:
        if n>len(arr):
            n = len(arr)
        for i in range(n):
            l.append(arr[i])
    return l