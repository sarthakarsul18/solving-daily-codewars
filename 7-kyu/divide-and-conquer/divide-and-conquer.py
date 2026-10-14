def div_con(x):
    num = 0
    for i in x:
        if isinstance(i,int):
            num+=i
        else:
            num-=int(i)
    return num