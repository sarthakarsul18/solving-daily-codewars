def sort_my_string(s):
    even=""
    odd=""
    for indx,i in enumerate(s):
        if indx%2==0:
            even+=i
        else:
            odd+=i
​
    return f"{even} {odd}"