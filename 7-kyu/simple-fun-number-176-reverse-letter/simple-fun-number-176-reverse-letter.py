def reverse_letter(st):
    clean=""
    for i in st:
        if i.isalpha():
            clean+=i
    return clean[::-1]