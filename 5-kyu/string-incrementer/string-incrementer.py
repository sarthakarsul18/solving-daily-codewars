def increment_string(string):
    i = len(string) - 1
​
    while i >= 0 and string[i].isdigit():
        i -= 1
​
    letters = string[:i + 1]
    digits = string[i + 1:]
​
    if digits:
        new_num = str(int(digits) + 1)
        new_num = new_num.zfill(len(digits))
        return letters + new_num
​
    return string + "1"