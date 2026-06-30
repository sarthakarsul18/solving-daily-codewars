def add_length(str_):
    l = []
    for i in str_.split():
        l.append(f"{i} {len(i)}")
    return l
        