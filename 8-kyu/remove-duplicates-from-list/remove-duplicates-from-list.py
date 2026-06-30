def distinct(seq):
    s = []
    for i in seq:
        if i not in s:
            s.append(i)
    return s
        