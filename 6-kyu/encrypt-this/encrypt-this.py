def encrypt_this(text):
    tx = text.split()
    new = []
    for i in tx:
        if len(i)==1:
            i = str(ord(i))
            new.append(i)
        else:
            i = list(i)
            i[0] = str(ord(i[0]))
            i[1], i[-1] = i[-1], i[1]
            new.append("".join(i))
​
    return " ".join(new)