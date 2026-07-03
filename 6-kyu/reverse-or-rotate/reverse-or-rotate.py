def rev_rot(strng, sz):
    result = ""
​
    if sz <= 0 or strng is None or sz > len(strng):
        return ""
​
    chunks = [strng[i:i+sz] for i in range(0, len(strng), sz)]
​
    for chunk in chunks:
        if len(chunk) < sz:
            continue
​
        if sum(int(i) for i in chunk) % 2 == 0:
            result += chunk[::-1]
        else:
            result += chunk[1:] + chunk[0]
​
    return result