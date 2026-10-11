def same_case(a, b): 
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    elif (a.isupper() and b.islower()) or (a.islower() and b.isupper()):
        return 0
    else:
        return -1
    