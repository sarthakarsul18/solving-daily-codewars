def replace_exclamation(st):
    ov = "aeiouAEIOU"
    result = ""
    for i in st:
        if i in ov:
            result+="!"
        else:
            result+=i
    return result
        