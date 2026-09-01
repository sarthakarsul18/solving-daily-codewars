def capitals(word):
    new = []
    for idx, i in enumerate(word):
        if i.isupper():
            new.append(idx)
    return new