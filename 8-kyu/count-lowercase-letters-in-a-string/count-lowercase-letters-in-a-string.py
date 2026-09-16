def lowercase_count(strng):
    count = 0
    for i in strng:
        if i.islower():
            count+=1
    return count
            