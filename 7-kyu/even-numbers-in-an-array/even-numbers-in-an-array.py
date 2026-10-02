def even_numbers(arr,n):
    even=[]
    for i in arr:
        if i%2==0:
            even.append(i)
    return even[-n:]