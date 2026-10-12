def find_digit(num, nth):
    if nth<=0:
        return -1
    elif len(str(abs(num)))<nth:
        return 0
    else:
        reversed_num = (str(abs(num))[::-1])
        return int(reversed_num[nth-1]) 