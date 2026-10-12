def number_to_pwr(number, p): 
    result = 1
    for i in range(p):
        result*=number
    return result