def printer_error(s):
    error=0
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    for i in s:
        if i not in alpha:
            error+=1
    return f"{error}/{len(s)}"
            