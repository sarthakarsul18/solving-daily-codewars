def vowel_indices(word):
    count=[]
    for indx,i in enumerate(word):
        if i in "aeiouyAEIOUY":
            count.append(indx+1)
    return count