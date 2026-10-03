def words_to_marks(s):
    total=0
    for i in s:
        total+=(ord(i)-97+1)
    return total